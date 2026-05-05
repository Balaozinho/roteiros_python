"""
Text-to-Speech com Python e OpenAI API
=======================================
Converte texto em áudio MP3 narrado usando o endpoint audio.speech da OpenAI.
Baseado no tutorial do notebook 3Whisper.ipynb (série PYTHON IA).

Dependências:
    pip install openai python-dotenv

Configuração:
    Crie um arquivo .env na raiz do projeto com:
    OPENAI_API_KEY=sk-...
"""

import openai
from dotenv import load_dotenv, find_dotenv


# Carrega as variáveis do arquivo .env para o ambiente do processo.
# find_dotenv() sobe os diretórios até achar o .env, sem precisar de caminho fixo.
_ = load_dotenv(find_dotenv())


def criar_cliente() -> openai.OpenAI:
    """Instancia o cliente OpenAI usando a chave do ambiente.

    Returns:
        Cliente OpenAI autenticado, pronto para chamadas à API.

    Raises:
        openai.AuthenticationError: se OPENAI_API_KEY estiver ausente ou inválida.
    """
    # A SDK lê OPENAI_API_KEY automaticamente — não passe a chave diretamente aqui
    return openai.OpenAI()


def gerar_audio(
    texto: str,
    caminho_saida: str,
    modelo: str = "tts-1",
    voz: str = "echo",
) -> None:
    """Converte texto em áudio MP3 e salva no caminho especificado.

    Args:
        texto: Conteúdo a ser narrado. Pode ser qualquer comprimento.
        caminho_saida: Caminho local onde o MP3 será gravado (ex: 'audio.mp3').
        modelo: Modelo TTS a usar. 'tts-1' é rápido; 'tts-1-hd' tem maior qualidade.
        voz: Voz da narração. Opções: 'alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer'.

    Returns:
        None. O arquivo é salvo diretamente no disco.

    Raises:
        openai.APIError: em caso de falha na chamada à API.
        IOError: se o caminho de saída não for gravável.
    """
    client = criar_cliente()

    # Chama o endpoint de síntese de voz — chamada síncrona (aguarda resposta completa)
    resposta = client.audio.speech.create(
        model=modelo,
        voice=voz,
        input=texto,
    )

    # Grava o binário MP3 retornado pela API diretamente no arquivo
    resposta.write_to_file(caminho_saida)
    print(f"Áudio salvo em: {caminho_saida}")


# --- Exemplo de uso ---

if __name__ == "__main__":
    # Texto de exemplo — substitua pelo conteúdo desejado
    texto_exemplo = "Python é mais legal"

    # Nome do arquivo de saída
    arquivo_saida = "gali_audio.mp3"

    # Gera o áudio com a voz 'echo' (grave, clara, neutra)
    gerar_audio(
        texto=texto_exemplo,
        caminho_saida=arquivo_saida,
        modelo="tts-1",
        voz="echo",
    )

    # Para usar voz feminina calorosa:
    # gerar_audio(texto=texto_exemplo, caminho_saida="audio_nova.mp3", voz="nova")

    # Para maior qualidade de áudio (mais lento e mais caro):
    # gerar_audio(texto=texto_exemplo, caminho_saida="audio_hd.mp3", modelo="tts-1-hd")
