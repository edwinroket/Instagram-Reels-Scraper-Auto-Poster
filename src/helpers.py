# src/helpers.py
import os
import config

def load_all_config():
    """Crea las carpetas necesarias si no existen"""
    dirs = [
        config.DOWNLOAD_DIR,
        os.path.dirname(config.REELS_EXCEL),
        os.path.dirname(config.PENDIENTES_EXCEL)
    ]
    
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
            print(f"[OK] Carpeta creada: {d}")