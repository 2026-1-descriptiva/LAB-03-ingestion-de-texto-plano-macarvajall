"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import re

    import pandas as pd

    rows = []
    current_row = None
    current_keywords = []

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()

            match = re.match(r"^\s*(\d+)\s+(\d+)\s+(\d+,\d+)\s+%\s+(.*)$", line)

            if match:
                if current_row is not None:
                    rows.append(current_row + [format_keywords(current_keywords)])

                current_row = [
                    int(match.group(1)),
                    int(match.group(2)),
                    float(match.group(3).replace(",", ".")),
                ]
                current_keywords = [match.group(4)]

            elif current_row is not None and line.strip():
                current_keywords.append(line.strip())

    if current_row is not None:
        rows.append(current_row + [format_keywords(current_keywords)])

    return pd.DataFrame(
        rows,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )


def format_keywords(keywords):
    """Normaliza espacios y separadores en la columna de palabras clave."""
    import re

    text = " ".join(keywords).strip().rstrip(".")
    text = re.sub(r"\s+", " ", text)
    return ", ".join(keyword.strip() for keyword in text.split(","))
