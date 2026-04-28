# Curso Practico de Pandas

Proyecto educativo para aprender operaciones frecuentes de `pandas` con ejemplos reproducibles. El contenido esta organizado por tema para que puedas estudiar, ejecutar y modificar cada caso de forma independiente.

## Objetivo

Aprender a manipular datos tabulares con `DataFrame` usando operaciones esenciales:

- unir tablas con `merge`
- concatenar datos con `concat`
- limpiar valores nulos y duplicados
- agrupar datos con `groupby` y `agg`
- tomar muestras reproducibles con `sample`

## Estructura

```text
pandas-mejorado/
  data/
    clientes.csv
    pedidos.csv
    jugadores_a.csv
    jugadores_b.csv
    ventas.csv
  notebooks/
    01_merge_joins.ipynb
    02_concat_union.ipynb
    03_limpieza_dropna_duplicados.ipynb
    04_groupby_agg.ipynb
    05_sample.ipynb
  scripts/
    01_merge_joins.py
    02_concat_union.py
    03_limpieza_dropna_duplicados.py
    04_groupby_agg.py
    05_sample.py
  requirements.txt
```

## Instalacion

Se recomienda Python 3.9 o superior.

```bash
pip install -r requirements.txt
```

Para abrir los notebooks:

```bash
jupyter notebook notebooks
```

Para ejecutar un script:

```bash
python scripts/01_merge_joins.py
```

## Temas

### 1. Merge y joins

Explica como combinar tablas relacionadas con `pd.merge()` usando `inner`, `left`, `right` y `outer`. Tambien muestra como unir columnas con nombres distintos mediante `left_on` y `right_on`.

### 2. Concat y union

Muestra como apilar filas con `pd.concat()`, reiniciar indices con `ignore_index=True` y simular una union sin duplicados con `drop_duplicates()`.

### 3. Limpieza de datos

Incluye diagnostico de valores nulos con `isna().sum()`, eliminacion de filas vacias con `dropna(how="all")`, limpieza estricta con `dropna()`, eliminacion de duplicados y eliminacion de columnas.

### 4. GroupBy y agregaciones

Agrupa ventas por categoria y pais. Usa agregaciones simples y personalizadas con `agg()`, incluyendo suma, promedio, conteo y union de textos.

### 5. Sample

Enseña como tomar muestras por porcentaje o cantidad fija usando `sample()`. Todos los ejemplos usan `random_state` para obtener resultados reproducibles.

## Ejercicios sugeridos

1. Cambia el tipo de join en el notebook `01_merge_joins.ipynb` y explica que filas aparecen o desaparecen.
2. Agrega un nuevo cliente sin pedidos y revisa como cambia el `left join`.
3. Inserta una fila duplicada en `ventas.csv` y limpiala con `drop_duplicates()`.
4. Agrupa ventas por vendedor y calcula el total vendido.
5. Toma una muestra del 40% de las ventas y cambia el `random_state`.

## Buenas practicas aplicadas

- Datos separados en archivos CSV.
- Ejemplos reproducibles.
- Nombres de variables descriptivos.
- Separacion por tema.
- Scripts equivalentes para ejecutar sin Jupyter.
- Sin uso de `pd.np`, que esta obsoleto.
