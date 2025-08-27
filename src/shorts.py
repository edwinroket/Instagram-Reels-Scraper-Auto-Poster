# src/shorts.py
import config
from utils_excel import guardar_reel
import requests
import json

def main():
    """
    Scrapea videos de YouTube Shorts de los canales listados en config.CHANNEL_LINKS
    y guarda en Excel evitando duplicados.
    """
    for canal in config.CHANNEL_LINKS:
        print(f"[+] Scrapeando canal: {canal}")
        
        try:
            # Construir URL de API de YouTube (simplificado)
            url = f"https://www.googleapis.com/youtube/v3/search?key={config.YOUTUBE_API_KEY}&channelId={canal}&part=snippet,id&order=date&type=video&maxResults=10"
            response = requests.get(url)
            if response.status_code != 200:
                print(f"[ERROR] Error al obtener videos: {response.status_code}")
                continue
            
            data = response.json()
            for item in data.get("items", []):
                video_id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                video_url = f"https://www.youtube.com/shorts/{video_id}"
                
                # Guardar en Excel; si ya existe, lo ignora
                guardado = guardar_reel(
                    config.REELS_EXCEL,
                    perfil=canal,
                    media_id=video_id,
                    url=video_url,
                    caption=title
                )
                
                if guardado:
                    print(f"[OK] Short guardado: {video_id} canal={canal}")
                else:
                    print(f"[SKIP] Short ya registrado: {video_id}")

        except Exception as e:
            print(f"[ERROR] Al scrapear canal {canal}: {str(e)}")