# Text-to-Speech com Python e OpenAI API

## Objetivo

Este vídeo ensina como transformar texto em áudio narrado usando a API da OpenAI com Python. Em menos de 10 linhas de código, é possível gerar um arquivo MP3 de alta qualidade a partir de qualquer string de texto, escolhendo entre diferentes vozes disponíveis na plataforma. O resultado é um arquivo de áudio pronto para uso em projetos de IA, automações e conteúdo.

## Conceitos Abordados

- Autenticação com a OpenAI API usando variáveis de ambiente (`.env` + `python-dotenv`)
- Instanciação do cliente OpenAI (`openai.Client`)
- Uso do endpoint `audio.speech.create` para síntese de voz
- Parâmetros de configuração: modelo TTS, voz e texto de entrada
- Salvamento do áudio gerado em arquivo MP3 com `write_to_file`

## Pré-requisitos Sugeridos

- Python 3.8 ou superior instalado
- Conta na OpenAI com chave de API (`OPENAI_API_KEY`)
- Familiaridade com Jupyter Notebooks
- Conhecimento básico de variáveis e funções em Python
- Pacotes instalados: `openai`, `python-dotenv`

## Estrutura do Código — Passo a Passo

### Passo 1: Importar bibliotecas e carregar variáveis de ambiente

```python
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
```

A biblioteca `python-dotenv` localiza automaticamente o arquivo `.env` no diretório do projeto e carrega as variáveis definidas nele como variáveis de ambiente do sistema. Assim, a `OPENAI_API_KEY` fica disponível sem precisar ser exposta diretamente no código.

### Passo 2: Instanciar o cliente OpenAI

```python
client = openai.Client()
```

O cliente lê automaticamente a variável de ambiente `OPENAI_API_KEY` carregada no passo anterior. Toda comunicação com a API da OpenAI é feita através deste objeto.

> **Nota:** A versão atual da SDK usa `openai.OpenAI()` (com letra maiúscula). Ambas funcionam, mas `openai.OpenAI()` é a forma recomendada nas versões mais recentes.

### Passo 3: Definir o arquivo de saída e o texto a narrar

```python
arquivo = 'gali_audio.mp3'
texto = 'Python é mais legal'
```

Define o nome do arquivo MP3 que será salvo localmente e o texto que será convertido em fala. O texto pode ter qualquer tamanho — a API fragmenta internamente textos longos.

### Passo 4: Configurar e executar a síntese de voz

```python
resposta = client.audio.speech.create(
    model='tts-1',
    voice='echo',
    input=texto,
)
```

- `model='tts-1'`: modelo padrão de TTS da OpenAI (rápido e econômico). Use `tts-1-hd` para maior qualidade de áudio.
- `voice='echo'`: uma das 6 vozes disponíveis. Outras opções: `alloy`, `fable`, `onyx`, `nova`, `shimmer`.
- `input=texto`: o texto a ser narrado.

A chamada à API é síncrona — o código aguarda a resposta completa antes de continuar.

### Passo 5: Salvar o arquivo de áudio

```python
resposta.write_to_file(arquivo)
```

Escreve o conteúdo binário do MP3 no caminho especificado. O arquivo é salvo no diretório de trabalho atual. Após a execução, o áudio está pronto para reprodução.
