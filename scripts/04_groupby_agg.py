from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


ventas = pd.read_csv(DATA_DIR / "ventas.csv")
ventas["importe"] = ventas["cantidad"] * ventas["precio_unitario"]

print("Ventas")
print(ventas)

print("\nConteo por categoria")
conteo_categoria = ventas.groupby("categoria").count()
print(conteo_categoria)

print("\nResumen por categoria")
resumen_categoria = ventas.groupby("categoria").agg(
    total_vendido=("importe", "sum"),
    ticket_promedio=("importe", "mean"),
    cantidad_operaciones=("venta_id", "count"),
    productos=("producto", lambda valores: ", ".join(sorted(valores.unique()))),
)
print(resumen_categoria)

print("\nResumen por pais y categoria")
resumen_pais_categoria = ventas.groupby(["pais", "categoria"]).agg(
    total_vendido=("importe", "sum"),
    unidades=("cantidad", "sum"),
)
print(resumen_pais_categoria)
