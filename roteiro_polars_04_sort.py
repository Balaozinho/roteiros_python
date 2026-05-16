# Projeto 04 — Ordenando DataFrames com sort()
# sort() aceita múltiplas colunas com direções independentes via descending=[].

import polars as pl

df = pl.DataFrame({
    'aluno': ['Carlos', 'Ana', 'Bruno', 'Diana', 'Ana'],
    'nota': [8.5, 9.0, 7.0, 9.0, 6.5],
    'turma': ['A', 'B', 'A', 'B', 'A'],
})

# by=[...] define a ordem de prioridade das colunas de ordenação
# descending=[True, False] → nota decrescente, aluno alfabético crescente (desempate)
ordenado = df.sort(
    by=['nota', 'aluno'],
    descending=[True, False]
)

print(ordenado)
