# src/poster.py
import os
import subprocess
import time
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, UserShort
import config
from utils_excel import leer_excel, marcar_publicado
from moviepy.editor import VideoFileClip

# --- Funciones de ayuda ---
def ensure_compatible_video(input_path):
    output_path = input_path.replace(".mp4", "_safe.mp4")
    if os.path.exists(output_path):
        return output_path
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-c:v", "libx264", "-crf", "23", "-preset", "fast",
        "-c:a", "aac", "-b:a", "128k",
        output_path
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path

def trim_video(file_path, max_duration=15):
    clip = VideoFileClip(file_path)
    if clip.duration <= max_duration:
        return file_path
    trimmed_path = file_path.replace(".mp4", "_trimmed.mp4")
    clip.subclip(0, max_duration).write_videofile(trimmed_path, codec='libx264', audio_codec='aac', verbose=False, logger=None)
    clip.close()
    return trimmed_path

def get_video_duration(file_path):
    clip = VideoFileClip(file_path)
    duration = clip.duration
    clip.close()
    return duration

def remove_file(file_path):
    """Elimina un archivo si existe"""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"[OK] Archivo eliminado: {file_path}")
    except Exception as e:
        print(f"[WARN] No se pudo eliminar {file_path}: {e}")

# --- Clase manager ---
class InstagramManagerWrapper:
    def __init__(self):
        self.client = Client()
        self.session_file = os.path.join(config.CURRENT_DIR, "session.json")

    def load_session(self):
        if os.path.exists(self.session_file):
            try:
                self.client.load_settings(self.session_file)
                print("[OK] Sesion cargada desde archivo")
                return True
            except Exception as e:
                print("[ERROR] Error cargando sesion:", e)
        return False

    def save_session(self):
        try:
            self.client.dump_settings(self.session_file)
            print("[OK] Sesion guardada")
        except Exception as e:
            print("[ERROR] Error guardando sesion:", e)

    def validate_session(self):
        try:
            self.client.user_info_by_username(config.USERNAME)
            return True
        except Exception as e:
            print("[ERROR] Sesion invalida o expirada:", e)
            return False

    def login(self):
        if self.load_session() and self.validate_session():
            print("[OK] Sesion valida")
            return True
        print("[INFO] Iniciando login completo...")
        self.client.login(config.USERNAME, config.PASSWORD)
        self.save_session()
        print("[OK] Login completo")
        return True

# --- Subida de historias vinculadas al Reel ---
def post_to_story(manager, media_pk, media_path):
    safe_path = trim_video(media_path)
    user_info = manager.client.user_info_by_username(config.USERNAME)
    user_short = UserShort(
        pk=user_info.pk,
        username=user_info.username,
        full_name=user_info.full_name,
        is_private=user_info.is_private,
        profile_pic_url=user_info.profile_pic_url,
        is_verified=user_info.is_verified
    )

    try:
        manager.client.video_upload_to_story(
            safe_path,
            mentions=[StoryMention(user=user_short, x=0.5, y=0.5, width=0.4, height=0.1)],
            medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)]
        )
        print("[OK] Reel compartido en historia correctamente")
    except Exception as e:
        print("[ERROR] No se pudo subir la historia:", e)
    # NO eliminar archivo aqui

# --- Main ---
def main():
    df = leer_excel(config.REELS_EXCEL)
    pendientes = df[df["publicado"] == 0]

    if pendientes.empty:
        print("[INFO] No hay reels pendientes")
        return

    fila = pendientes.iloc[0]
    media_id = str(fila["media_id"])
    media_path = os.path.join(config.DOWNLOAD_DIR, f"{media_id}.mp4")

    if not os.path.exists(media_path):
        print("[WARN] Archivo no encontrado:", media_path)
        marcar_publicado(config.REELS_EXCEL, media_id)
        return

    manager = InstagramManagerWrapper()
    if not manager.login():
        print("[ERROR] No se pudo iniciar sesion")
        return

    safe_video = ensure_compatible_video(media_path)

    try:
        print(f"[INFO] Preparando reel {media_id} para subir...")
        print(f"[INFO] Subiendo reel {media_id} a Reels...")
        media_obj = manager.client.clip_upload(safe_video, caption=config.HASHTAGS)
        print(f"[OK] Publicacion en Reels exitosa: {media_obj.code}")

        # Marcar como publicado SOLO si la subida tuvo exito
        marcar_publicado(config.REELS_EXCEL, media_id)

        # Subir historia si corresponde
        if int(config.IS_POST_TO_STORY) == 1:
            post_to_story(manager, media_obj.pk, safe_video)

    except Exception as e:
        # Detectar feedback_required y marcar temporalmente
        if "feedback_required" in str(e).lower():
            print(f"[WARN] Reel {media_id} bloqueado temporalmente por Instagram.")
            marcar_publicado(config.REELS_EXCEL, media_id)
        else:
            print("[ERROR] Al publicar reel:", media_id, e)
    finally:
        remove_file(safe_video)

if __name__ == "__main__":
    main()