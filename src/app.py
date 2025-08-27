# src/app.py
import time
import config
import reels
import poster
import auth
from datetime import datetime, timedelta
import random
import pytz
import builtins

# Zona horaria Chile
chile_tz = pytz.timezone("America/Santiago")

def print_chile(*args, **kwargs):
    now = datetime.now(chile_tz).strftime("[%H:%M:%S]")
    builtins.print(now, *args, **kwargs, flush=True)

# Sobrescribir print globalmente
print = print_chile

# Tiempos iniciales
next_reels_scraper_run_at = datetime.now()
next_poster_run_at = datetime.now()

# Login solo si alguna funcion esta habilitada
api = auth.login() if config.IS_ENABLED_REELS_SCRAPER == 1 or config.IS_ENABLED_AUTO_POSTER == 1 else None

def segundos_a_horas_minutos(segundos):
    """Convierte segundos a formato horas:minutos"""
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    return f"{horas}h {minutos}m"

def main():
    global next_reels_scraper_run_at, next_poster_run_at, api
    
    while True:
        now = datetime.now()

        # Ejecutar scraper
        if config.IS_ENABLED_REELS_SCRAPER == 1 and next_reels_scraper_run_at <= now:
            print("Scrapeando Reels...")
            try:
                reels.main(api)
            except Exception as e:
                print("[ERROR] Scraper fallo:", str(e))
            
            # Convertir horas a segundos
            interval_hours = random.randint(config.SCRAPER_INTERVAL_MIN_HOURS, config.SCRAPER_INTERVAL_MAX_HOURS)
            interval_sec = interval_hours * 3600
            next_reels_scraper_run_at = now + timedelta(seconds=interval_sec)
            
            intervalo_legible = segundos_a_horas_minutos(interval_sec)
            print("Intervalo scraper:", intervalo_legible)
            print("Proximo Scraper:", next_reels_scraper_run_at.strftime("%Y-%m-%d %H:%M:%S"))

        # Ejecutar poster
        if config.IS_ENABLED_AUTO_POSTER == 1 and next_poster_run_at <= now:
            print("Publicando Reel...")
            try:
                poster.main()
            except Exception as e:
                print("[ERROR] Poster fallo:", str(e))
            
            # Convertir horas a segundos
            interval_hours = random.randint(config.POSTING_INTERVAL_MIN_HOURS, config.POSTING_INTERVAL_MAX_HOURS)
            interval_sec = interval_hours * 3600
            next_poster_run_at = datetime.now() + timedelta(seconds=interval_sec)
            
            # Mostrar en formato legible
            intervalo_legible = segundos_a_horas_minutos(interval_sec)
            print("Intervalo publicaciones:", intervalo_legible)
            print("Proxima publicacion:", next_poster_run_at.strftime("%Y-%m-%d %H:%M:%S"))

        time.sleep(1)

if __name__ == "__main__":
    main()