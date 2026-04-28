from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


ventas = pd.read_csv(DATA_DIR / "ventas.csv")

print("Ventas originales")
print(ventas)

print("\nMuestra del 25% con random_state para reproducibilidad")
muestra_porcentaje = ventas.sample(frac=0.25, random_state=42)
print(muestra_porcentaje)

print("\nMuestra de 3 filas")
muestra_filas = ventas.sample(n=3, random_state=42)
print(muestra_filas)

print("\nEjemplo con numeros aleatorios usando numpy, sin pd.np")
numeros = pd.DataFrame({"valor": np.random.default_rng(seed=42).random(10)})
print(numeros)
