# src/remover.py
import os
import config
from utils_excel import leer_excel

def main():
    # Leer Excel y obtener media_ids publicados
    df = leer_excel(config.REELS_EXCEL)
    publicados = df[df["publicado"] == 1]["media_id"].astype(str).tolist()

    if not publicados:
        print("[INFO] No hay reels publicados para limpiar")
        return

    # Listar archivos en downloads/
    for file in os.listdir(config.DOWNLOAD_DIR):
        file_path = os.path.join(config.DOWNLOAD_DIR, file)
        if not os.path.isfile(file_path):
            continue

        base_name, ext = os.path.splitext(file.lower())
        if ext not in [".mp4", ".jpg"]:
            continue

        if base_name in publicados:
            try:
                os.remove(file_path)
                print(f"[OK] Archivo publicado eliminado: {file_path}")
            except Exception as e:
                print(f"[ERROR] No se pudo eliminar {file_path}: {e}")