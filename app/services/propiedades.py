from app.db.fake_db import PROPIEDADES

def buscar_propiedades(tipo=None, ubicacion=None):
    resultados = PROPIEDADES

    if tipo:
        resultados = [p for p in resultados if p["tipo"] == tipo]

    if ubicacion:
        resultados = [p for p in resultados if ubicacion.lower() in p["ubicacion"].lower()]

    return resultados
