# src/reels.py
import os
import time
import random
import requests
import config
from utils_excel import guardar_reel

def descargar_video(video_url, filename):
    os.makedirs(config.DOWNLOAD_DIR, exist_ok=True)
    filepath = os.path.join(config.DOWNLOAD_DIR, filename)
    try:
        r = requests.get(video_url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filepath, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return filepath
    except Exception as e:
        print(f"[ERROR] No se pudo descargar {video_url}: {str(e)}")
        return None

def main(api):
    num_cuentas = random.randint(2, min(6, len(config.ACCOUNTS)))
    cuentas_seleccionadas = random.sample(config.ACCOUNTS, num_cuentas)
    print("cuentas seleccionadas:", cuentas_seleccionadas)

    print("="*60)
    print(f"Scrapeando {num_cuentas} cuentas")
    print("="*60)

    for i, cuenta in enumerate(cuentas_seleccionadas, start=1):
        if i > 1:
            time.sleep(random.uniform(160, 180))
        print(f"[{i}/{num_cuentas}] Scrapeando: {cuenta}")
        try:
            user_id = api.user_id_from_username(cuenta)
            time.sleep(random.uniform(30, 60))
            medias = api.user_medias_v1(user_id, amount=config.FETCH_LIMIT)

            for media in medias:
                time.sleep(random.uniform(2, 5))
                if media.media_type not in [2, 8]:
                    continue
                url = f"https://www.instagram.com/reel/{media.code}/"
                caption = media.caption_text if media.caption_text else ""
                
                media_id = str(media.pk)  # siempre string
                guardado = guardar_reel(
                    config.REELS_EXCEL,
                    perfil=cuenta,
                    media_id=media_id,
                    url=url,
                    caption=caption
                )

                video_url = getattr(media, "video_url", None)
                if video_url:
                    filename = f"{media_id}.mp4"  # consistente
                    path = descargar_video(video_url, filename)
                    if path:
                        print(f"[OK] Reel descargado en {path}")

                if guardado:
                    print(f"[OK] Reel guardado en Excel {media_id}")
                else:
                    print(f"[SKIP] Reel ya registrado {media_id}")
        except Exception as e:
            print(f"[ERROR] Al scrapear {cuenta}: {str(e)}")