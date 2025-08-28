# Instagram Reels & YouTube Shorts Auto Scraper y Poster

**Descripción:**  
Este proyecto automatiza el scraping de Reels de Instagram y Shorts de YouTube, y su publicación automática en Instagram. Incluye sistema anti-duplicados, gestión de archivos y programación flexible de intervalos.

---

## Características principales

- **Scraping inteligente:** Recolecta Reels de Instagram y Shorts de YouTube automáticamente.  
- **Base de datos simple:** Usa archivos Excel para evitar duplicados y trackear publicaciones.  
- **Publicación automática:** Programa publicaciones en Instagram con intervalos personalizables.  
- **Historias integradas:** Opción para compartir automáticamente en historias de Instagram.  
- **Manejo de archivos:** Limpieza automática de archivos descargados después de su uso.  
- **Zona horaria Chile:** Configurado específicamente para horario de Chile (America/Santiago).  
- **Aleatoriedad controlada:** Intervalos aleatorios para evitar detección por parte de Instagram.  

---

## Requisitos previos

- Python 3.8+  
- Cuenta de Instagram  
- API Key de YouTube (opcional, para scraping de Shorts)  
- Sistema operativo: **Linux**

---

## Instalación

1. **Clonar repositorio**
```bash
git clone https://github.com/edwinroket/Instagram-Reels-Scraper-Auto-Poster.git
cd Instagram-Reels-Scraper-Auto-Poster
```

2. **Crear entorno virtual (opcional pero recomendado)**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configuración**  
Editar `src/config.py` con tus credenciales y preferencias:
```python
USERNAME = "tu_usuario_instagram"
PASSWORD = "tu_password_instagram"
ACCOUNTS = ["perfil1", "perfil2"]
CHANNEL_LINKS = ["id_canal_youtube"]  # Opcional
YOUTUBE_API_KEY = "tu_api_key_de_youtube"  # Opcional
SCRAPER_INTERVAL_IN_MIN = 720
POSTING_INTERVAL_IN_MIN = 300
REMOVE_FILE_AFTER_MINS = 40
HASHTAGS = "#ejemplo #reels"
```

5. **Ejecución**
```bash
cd src
python3 app.py
```

El bot:  
- Scrapea Reels y Shorts según intervalos configurados.  
- Guarda datos en Excel evitando duplicados.  
- Descarga reels si es necesario.  
- Publica automáticamente en Instagram.  
- Elimina archivos antiguos según `REMOVE_FILE_AFTER_MINS`.  

---

## Estructura del proyecto

```
Instagram-Reels-Scraper-Auto-Poster/
│
├── src/                   # Código fuente principal
│   ├── app.py             # Loop principal
│   ├── auth.py            # Autenticación de Instagram
│   ├── config.py          # Configuración
│   ├── helpers.py         # Utilidades
│   ├── utils_excel.py     # Manejo de Excel
│   ├── reels.py           # Scraping de Instagram Reels
│   ├── shorts.py          # Scraping de YouTube Shorts
│   ├── poster.py          # Publicación en Instagram
│   └── remover.py         # Limpieza de archivos
│
├── downloads/             # Archivos descargados (creado automáticamente)
├── database/              # Base de datos Excel
│   └── reels.xlsx         # Registro de contenido
├── main.py                # Punto de entrada
├── requirements.txt       # Dependencias
```

---

## Configuración avanzada

En `src/config.py` puedes ajustar:

```python
# Intervalos en horas
SCRAPER_INTERVAL_MIN_HOURS = 12
SCRAPER_INTERVAL_MAX_HOURS = 20
POSTING_INTERVAL_MIN_HOURS = 4
POSTING_INTERVAL_MAX_HOURS = 6

# Comportamiento
IS_ENABLED_REELS_SCRAPER = 1   # 1=Activar scraping Reels
IS_ENABLED_AUTO_POSTER = 1     # 1=Activar auto-poster
IS_POST_TO_STORY = 1           # 1=Compartir en historias
IS_REMOVE_FILES = 1            # 1=Eliminar archivos después de publicar
```

---

## Funcionamiento

El bot opera en un ciclo continuo que:  
1. Scrapea Reels/Shorts de las cuentas configuradas en intervalos aleatorios.  
2. Guarda los datos en Excel evitando duplicados.  
3. Descarga videos en la carpeta `downloads/`.  
4. Publica automáticamente según intervalos configurados.  
5. Limpia los archivos ya publicados.  
6. Repite el ciclo indefinidamente.  

---

## Troubleshooting

**Problemas comunes:**

- **Error de login de Instagram:**  
  1. Verifica que las credenciales sean correctas.  
  2. Instagram puede requerir verificación en el primer login, elimina `session.json` en `src/`.

- **Problemas con YouTube API:**  
  1. Asegúrate de tener una API key válida.  
  2. Verifica que los IDs de canal sean correctos.

- **Archivos no se eliminan:**  
  1. Revisa los permisos de la carpeta `downloads/`.  

---

## Notas importantes

- Optimizado para zona horaria de Chile.  
- Usa intervalos aleatorios para evitar detección.  
- Respeta siempre los términos de servicio de Instagram y YouTube.  
- Se recomienda usar una cuenta dedicada para automatizaciones.  

---

## Licencia y Disclaimer

Este proyecto es **educativo**.  
El usuario es responsable de cumplir con los términos de servicio de Instagram y YouTube.
