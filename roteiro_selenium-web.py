"""
Automação Web com Python e Selenium
=====================================
Demonstra como abrir o Chrome automaticamente, navegar até o Google
e interagir com o campo de pesquisa usando Selenium WebDriver.
Baseado no tutorial do vídeo 130.mov (arquivo 123Selenium2.py).

Dependências:
    pip install selenium

Nota: A partir do Selenium 4.6+, o ChromeDriver é gerenciado automaticamente
pelo selenium-manager — não é necessário baixar ou configurar o chromedriver.exe.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def criar_driver() -> webdriver.Chrome:
    """Inicializa e retorna uma instância do Chrome controlada pelo Selenium.

    Returns:
        Instância do WebDriver apontando para o Chrome aberto.

    Raises:
        WebDriverException: se o Chrome não estiver instalado ou o ChromeDriver
            não for compatível com a versão do navegador.
    """
    # Abre o Chrome em modo normal (com interface gráfica)
    # Para modo headless (sem janela): use options.add_argument("--headless")
    return webdriver.Chrome()


def pesquisar_no_google(driver: webdriver.Chrome, termo: str) -> None:
    """Navega até o Google e realiza uma pesquisa pelo termo informado.

    Args:
        driver: Instância ativa do WebDriver.
        termo: Texto a ser digitado no campo de pesquisa.
    """
    # Carrega a URL e aguarda o DOM estar pronto
    driver.get("https://www.google.com")

    # Localiza o campo de pesquisa pelo atributo name="q"
    # Alternativas equivalentes:
    #   driver.find_element(By.CSS_SELECTOR, "input[name='q']")
    #   driver.find_element(By.XPATH, "//input[@name='q']")
    campo_pesquisa = driver.find_element(By.NAME, "q")

    # Digita o termo — send_keys simula digitação real no teclado
    campo_pesquisa.send_keys(termo)

    # Pressiona ENTER para executar a pesquisa (alternativa a clicar no botão)
    campo_pesquisa.send_keys(Keys.ENTER)


def encerrar(driver: webdriver.Chrome, pausar: bool = True) -> None:
    """Encerra a sessão do navegador, com pausa opcional para inspeção visual.

    Args:
        driver: Instância ativa do WebDriver.
        pausar: Se True, aguarda o usuário pressionar ENTER antes de fechar.
    """
    if pausar:
        # Congela o script para permitir inspeção visual do navegador
        input("Pressione ENTER para fechar o navegador...")

    # quit() fecha o browser E encerra o processo ChromeDriver
    # Prefira quit() a close() para liberar todos os recursos do sistema
    driver.quit()


# --- Exemplo de uso ---

if __name__ == "__main__":
    driver = criar_driver()

    try:
        pesquisar_no_google(driver, termo="Python Selenium")
        encerrar(driver, pausar=True)
    except Exception as e:
        # Garante que o driver seja encerrado mesmo em caso de erro
        print(f"Erro durante a automação: {e}")
        driver.quit()

    # Exemplos de outras estratégias de localização de elementos:
    # elemento = driver.find_element(By.ID, "meu-id")
    # elemento = driver.find_element(By.CLASS_NAME, "minha-classe")
    # elemento = driver.find_element(By.XPATH, "//button[text()='Entrar']")
    # elemento = driver.find_element(By.CSS_SELECTOR, "div.container > input")
