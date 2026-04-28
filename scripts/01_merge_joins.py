from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


clientes = pd.read_csv(DATA_DIR / "clientes.csv")
pedidos = pd.read_csv(DATA_DIR / "pedidos.csv")

print("Clientes")
print(clientes)

print("\nPedidos")
print(pedidos)

print("\nInner join: solo clientes con pedidos existentes")
inner_join = pd.merge(clientes, pedidos, how="inner", on="cliente_id", indicator=True)
print(inner_join)

print("\nLeft join: todos los clientes, aunque no tengan pedidos")
left_join = pd.merge(clientes, pedidos, how="left", on="cliente_id", indicator=True)
print(left_join)

print("\nRight join: todos los pedidos, aunque no exista el cliente en clientes.csv")
right_join = pd.merge(clientes, pedidos, how="right", on="cliente_id", indicator=True)
print(right_join)

print("\nOuter join: todos los clientes y todos los pedidos")
outer_join = pd.merge(clientes, pedidos, how="outer", on="cliente_id", indicator=True)
print(outer_join)

clientes_con_codigo = clientes.rename(columns={"cliente_id": "codigo_cliente"})
print("\nMerge con columnas de distinto nombre")
merge_distinto_nombre = pd.merge(
    clientes_con_codigo,
    pedidos,
    how="left",
    left_on="codigo_cliente",
    right_on="cliente_id",
    indicator=True,
)
print(merge_distinto_nombre)
