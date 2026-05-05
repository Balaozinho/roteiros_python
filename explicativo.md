# Automação Web com Python e Selenium

## Objetivo

Este vídeo ensina como automatizar ações em um navegador usando Python com a biblioteca Selenium. Com menos de 15 linhas de código, é possível abrir o Chrome programaticamente, navegar até um site, localizar elementos na página e interagir com eles — abrindo as portas para scraping, testes automatizados e bots de preenchimento de formulários.

## Conceitos Abordados

- Instalação e importação do Selenium (`webdriver`, `By`)
- Inicialização do Chrome via `webdriver.Chrome()`
- Navegação para URLs com `driver.get()`
- Localização de elementos HTML com `find_element(By.NAME, ...)`
- Interação com campos de texto via `send_keys()`
- Encerramento controlado do navegador com `driver.quit()`
- Uso de `input()` para pausar a execução e inspecionar o navegador antes de fechar

## Pré-requisitos Sugeridos

- Python 3.8 ou superior instalado
- Biblioteca Selenium instalada: `pip install selenium`
- Google Chrome instalado na máquina
- ChromeDriver compatível com a versão do Chrome (ou usar `selenium-manager`, incluído no Selenium 4.6+)
- Conhecimento básico de HTML (o que são atributos `name`, `id`, `class`)

## Estrutura do Código — Passo a Passo

### Passo 1: Importar as dependências

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
```

`webdriver` fornece a interface para controlar o navegador. `By` é uma classe de constantes que define as estratégias de localização de elementos: `By.NAME`, `By.ID`, `By.XPATH`, `By.CSS_SELECTOR`, entre outras.

### Passo 2: Inicializar o Chrome e navegar para o site

```python
driver = webdriver.Chrome()
driver.get("https://www.google.com")
```

`webdriver.Chrome()` abre uma janela real do Chrome sob controle do Selenium. A partir do Selenium 4.6, o ChromeDriver é baixado automaticamente pelo `selenium-manager` — não é necessário configurá-lo manualmente. `driver.get()` carrega a URL e aguarda o carregamento completo da página.

### Passo 3: Localizar o campo de pesquisa

```python
campo_pesquisa = driver.find_element(By.NAME, "q")
```

`find_element` retorna o primeiro elemento HTML que corresponde ao seletor informado. `By.NAME` busca pelo atributo `name` da tag — no Google, o campo de busca tem `name="q"`. O resultado é um objeto `WebElement`, que representa o elemento no DOM.

### Passo 4: Digitar texto no campo

```python
campo_pesquisa.send_keys("Python Selenium")
```

`send_keys()` simula a digitação caractere por caractere, exatamente como um usuário faria no teclado. Pode receber qualquer string, incluindo teclas especiais como `Keys.ENTER` ou `Keys.TAB` (importadas de `selenium.webdriver.common.keys`).

### Passo 5: Pausar e fechar o navegador

```python
input("Pressione ENTER para fechar o navegador...")
driver.quit()
```

`input()` congela a execução do script e permite inspecionar visualmente o navegador antes de encerrar. `driver.quit()` fecha o Chrome e encerra o processo do ChromeDriver — sempre prefira `quit()` a `close()` para liberar todos os recursos corretamente.
