# Instagram Reels & YouTube Shorts Auto Scraper y Poster

Este proyecto permite:

Este proyecto permite automatizar el scraping de Reels de Instagram y Shorts de YouTube, y su posterior publicación automática en Instagram. Incluye sistema anti-duplicados, gestión de archivos y programación flexible de intervalos.

---

## **Características principales**

Scraping inteligente: Recolecta Reels de Instagram y Shorts de YouTube automáticamente

Base de datos simple: Usa archivos Excel para evitar duplicados y trackear publicaciones

Publicación automática: Programa publicaciones en Instagram con intervalos personalizables

Historias integradas: Opción para compartir automáticamente en historias de Instagram

Manejo de archivos: Limpieza automática de archivos descargados después de su uso

Zona horaria Chile: Configurado específicamente para horario de Chile (America/Santiago)

Aleatoriedad controlada: Intervalos aleatorios para evitar detección

---

## **Instalación**

Prerrequisitos
Python 3.8+

Cuenta de Instagram

API Key de YouTube (opcional, para scraping de Shorts)


1. Clonar repositorio:
```bash
git clone https://github.com/edwinroket/Instagram-Reels-Scraper-Auto-Poster.git
cd Instagram-Reels-Scraper-Auto-Poster
2. Crear entorno virtual (opcional pero recomendado):
python3 -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

3. Instalar dependencias:
pip install -r requirements.txt

4. Configuración
Editar src/config.py con tus credenciales y preferencias:
Editar config.py:
USERNAME = "tu_usuario_instagram"
PASSWORD = "tu_password_instagram"
ACCOUNTS = ["perfil1", "perfil2"]
CHANNEL_LINKS = ["id_canal_youtube"]
# Configuración de YouTube (opcional)
YOUTUBE_API_KEY = "tu_api_key_de_youtube"
CHANNEL_LINKS = ["UCcanal1", "UCcanal2"]  # IDs de canales de YouTube
SCRAPER_INTERVAL_IN_MIN = 720
POSTING_INTERVAL_IN_MIN = 300
REMOVE_FILE_AFTER_MINS = 40
HASHTAGS = "#ejemplo #reels"

5. Ejecución
python main.py

El bot:
Scrapea reels y shorts según intervalos configurados.
Guarda datos en Excel evitando duplicados.
Descarga reels si es necesario.
Publica automáticamente en Instagram.
Elimina archivos antiguos según REMOVE_FILE_AFTER_MINS.

Estructura del proyecto

Instagram-Reels-Scraper-Auto-Poster/
│
├── src/                    # Código fuente principal
│   ├── __init__.py
│   ├── app.py             # Loop principal
│   ├── auth.py            # Autenticación de Instagram
│   ├── config.py          # Configuración
│   ├── helpers.py         # Utilidades
│   ├── utils_excel.py     # Manejo de Excel
│   ├── reels.py          # Scraping de Instagram Reels
│   ├── shorts.py         # Scraping de YouTube Shorts
│   ├── poster.py         # Publicación en Instagram
│   └── remover.py        # Limpieza de archivos
│
├── downloads/             # Archivos descargados (se crea automáticamente)
├── database/             # Base de datos Excel (se crea automáticamente)
│   └── reels.xlsx        # Registro de contenido
│
├── main.py               # Punto de entrada
├── requirements.txt      # Dependencias

⚙️ Configuración avanzada
En src/config.py puedes ajustar:
# Intervalos en horas
SCRAPER_INTERVAL_MIN_HOURS = 12   # Mínimo 12 horas entre scraping
SCRAPER_INTERVAL_MAX_HOURS = 20   # Máximo 20 horas entre scraping
POSTING_INTERVAL_MIN_HOURS = 4    # Mínimo 4 horas entre publicaciones
POSTING_INTERVAL_MAX_HOURS = 6    # Máximo 6 horas entre publicaciones

# Comportamiento
IS_ENABLED_REELS_SCRAPER = 1      # 1=Activar scraping Reels, 0=Desactivar
IS_ENABLED_AUTO_POSTER = 1        # 1=Activar auto-poster, 0=Desactivar
IS_POST_TO_STORY = 1              # 1=Compartir en historias, 0=No compartir
IS_REMOVE_FILES = 1               # 1=Eliminar archivos después de publicar

🔄 Funcionamiento

El bot opera en un ciclo continuo que:
Scrapea Reels: De las cuentas configuradas en intervalos aleatorios
Guarda en Excel: Registra el contenido evitando duplicados
Descarga videos: Almacena temporalmente en la carpeta downloads
Publica automáticamente: Según los intervalos configurados
Limpia archivos: Elimina los videos ya publicados
Repite el ciclo: De forma indefinida

🛠️ Troubleshooting

Problemas comunes:
Error de login de Instagram:
Verifica que las credenciales sean correctas
Instagram puede requerir verificación en el primer login, elimina el session.json que se genera en el src
Problemas con YouTube API:
Asegúrate de tener una API key válida
Verifica que los IDs de canal sean correctos

Archivos no se eliminan:
Revisa los permisos de la carpeta downloads/

📝 Notas importantes
El proyecto está optimizado para la zona horaria de Chile Usa intervalos aleatorios para evitar detección por parte de Instagram Siempre respeta los términos de servicio de Instagram y YouTube Se recomienda usar una cuenta dedicada para este tipo de automatizaciones

📄 Licencia
Este proyecto es para fines educativos. Asegúrate de cumplir con los términos de servicio de Instagram y YouTube al utilizarlo.

------------------------------------------------------------------------

Disclaimer: Este software está destinado para fines educativos. El usuario es responsable de cumplir con los términos de servicio de las plataformas utilizadas.


