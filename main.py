# main.py
import os
import sys

# Anadir src al path para que los imports funcionen
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Importar y ejecutar la aplicacion
from app import main

if __name__ == "__main__":
    main()