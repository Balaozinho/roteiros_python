# Projeto 01 — Benchmark: Pandas vs Polars
# Mede e compara o tempo de leitura de CSV entre as duas bibliotecas.

import pandas as pd
import polars as pl
import time


def benchmark_leitura_csv(caminho_csv: str) -> None:
    """Compara o tempo de leitura de um arquivo CSV entre Pandas e Polars.

    Args:
        caminho_csv: Caminho para o arquivo .csv a ser lido.
    """
    # --- Leitura com Pandas ---
    inicio = time.time()
    df_pandas = pd.read_csv(caminho_csv)
    tempo_exec_pandas = time.time() - inicio

    # --- Leitura com Polars ---
    inicio2 = time.time()
    df_polars = pl.read_csv(caminho_csv)
    tempo_exec_polars = time.time() - inicio2

    print(f'Tempo de execução do PANDAS foi de {tempo_exec_pandas:.6f}s')
    print(f'Tempo de execução do POLARS foi de {tempo_exec_polars:.6f}s')

    # Razão correta: pandas/polars indica quantas vezes Polars é mais rápido
    if tempo_exec_polars > 0:
        razao = tempo_exec_pandas / tempo_exec_polars
        print(f'O POLARS é {razao:.2f}x mais rápido do que o Pandas')


# --- Exemplo de uso ---
if __name__ == '__main__':
    # Crie um arquivo dados.csv antes de rodar, ou ajuste o caminho
    benchmark_leitura_csv('dados.csv')
