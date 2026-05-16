# Projeto 02 — Agrupando e Somando como um Profissional
# group_by + agg permite calcular múltiplas métricas por categoria em uma única chamada.

import polars as pl

df = pl.DataFrame({
    'categoria': ['Eletronico', 'Roupa', 'Eletronico', 'Roupa', 'Livro', 'Livro'],
    'valor': [1200.0, 89.90, 450.0, 199.90, 45.0, 60.0],
})

# group_by agrupa as linhas pela coluna indicada
# .agg() aplica funções de agregação em cada grupo
# .alias() renomeia a coluna resultante para um nome legível
resumo = df.group_by('categoria').agg(
    pl.sum('valor').alias('Total de Vendas'),
    pl.mean('valor').alias('Ticket Medio')
)

print(resumo)
