import pandas as pd


jugadores = pd.DataFrame(
    {
        "jugador": ["Trauco", "Advincula", None, "Lapadula", "Trauco", None],
        "posicion": ["Defensa", "Defensa", None, "Delantero", "Defensa", None],
        "pais": ["Peru", "Peru", None, "Peru", "Peru", None],
    }
)

print("Datos originales")
print(jugadores)

print("\nCantidad de nulos por columna")
print(jugadores.isna().sum())

print("\nEliminar filas donde todos los campos son nulos")
sin_filas_vacias = jugadores.dropna(how="all")
print(sin_filas_vacias)

print("\nEliminar filas donde al menos un campo es nulo")
sin_nulos = jugadores.dropna()
print(sin_nulos)

print("\nEliminar duplicados")
sin_duplicados = sin_filas_vacias.drop_duplicates()
print(sin_duplicados)

print("\nEliminar columnas posicion y pais")
solo_jugadores = sin_duplicados.drop(["posicion", "pais"], axis=1)
print(solo_jugadores)
