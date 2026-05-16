# Projeto 03 — Tratando Números Nulos
# with_columns + fill_null substitui None por valores padrão por tipo de coluna.

import polars as pl

df = pl.DataFrame({
    'nome': ['Ana', 'Bruno', None, 'Carla'],
    'idade': [25, None, 30, None],
    'cidade': ['SP', 'RJ', 'MG', None],
})

# with_columns aplica transformações coluna a coluna sem criar cópia do DataFrame
# fill_null recebe o valor de substituição adequado ao tipo: str para texto, int para número
df_limpo = df.with_columns([
    pl.col('nome').fill_null('Desconhecido'),
    pl.col('idade').fill_null(0),
    pl.col('cidade').fill_null('Nao informado')
])

print(df_limpo)
