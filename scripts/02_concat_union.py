from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


jugadores_peru = pd.read_csv(DATA_DIR / "jugadores_a.csv")
jugadores_brasil = pd.read_csv(DATA_DIR / "jugadores_b.csv")

print("Jugadores Peru")
print(jugadores_peru)

print("\nJugadores Brasil")
print(jugadores_brasil)

print("\nConcat conserva los indices originales")
union_all = pd.concat([jugadores_peru, jugadores_brasil])
print(union_all)

print("\nConcat con ignore_index=True reinicia el indice")
union_all_reindexado = pd.concat([jugadores_peru, jugadores_brasil], ignore_index=True)
print(union_all_reindexado)

print("\nUnion sin duplicados usando drop_duplicates")
union_sin_duplicados = union_all_reindexado.drop_duplicates()
print(union_sin_duplicados)
