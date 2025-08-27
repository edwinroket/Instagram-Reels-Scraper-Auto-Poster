# src/utils_excel.py
import os
import pandas as pd

def guardar_reel(excel_file, perfil, media_id, url, caption):
    """
    Guarda un reel en el archivo Excel, si no esta registrado aun.
    """
    media_id = str(media_id)  # siempre string

    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file, dtype={"media_id": str, "publicado": int})
    else:
        df = pd.DataFrame(columns=["perfil", "media_id", "url", "caption", "publicado"])

    if media_id in df["media_id"].values:
        return False

    nuevo = pd.DataFrame([{
        "perfil": perfil,
        "media_id": media_id,
        "url": url,
        "caption": caption,
        "publicado": 0
    }])
    df = pd.concat([df, nuevo], ignore_index=True)

    df.to_excel(excel_file, index=False)
    return True


def leer_excel(excel_file):
    """
    Lee el Excel asegurando que media_id se lea como string.
    """
    if os.path.exists(excel_file):
        return pd.read_excel(excel_file, dtype={"media_id": str, "publicado": int})
    else:
        return pd.DataFrame(columns=["perfil", "media_id", "url", "caption", "publicado"])


def marcar_publicado(excel_file, media_id, bloqueado=False):
    """
    Marca un reel como publicado en el Excel.
    Si bloqueado=True, marca como publicado pero podria usarse para tracking especial.
    """
    media_id = str(media_id)  # siempre string

    if not os.path.exists(excel_file):
        return

    df = pd.read_excel(excel_file, dtype={"media_id": str, "publicado": int})

    # Marcar como publicado (1) incluso si esta bloqueado
    df.loc[df["media_id"] == media_id, "publicado"] = 1

    df.to_excel(excel_file, index=False)