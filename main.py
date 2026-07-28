import sys
from pathlib import Path
from threading import Thread
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from pages.login_page import LoginPage
from pages.form_page import FormPage


URL_BASE = "http://127.0.0.1:8000/index.html"


def start_http_server(port=8000):
    handler = lambda *args, **kwargs: SimpleHTTPRequestHandler(*args, directory=str(ROOT), **kwargs)
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def stop_http_server(server):
    server.shutdown()
    server.server_close()


def criar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def main():
    server = start_http_server()
    driver = criar_driver()
    try:
        driver.get(URL_BASE)

        login_page = LoginPage(driver)
        login_page.fazer_login("standard_user", "secret_sauce")

        form_page = FormPage(driver)
        dados_lote = {
            "numero_lote": "LOTE-2025-0001",
            "produto": "Notebook",
            "status": "Concluído",
        }
        form_page.preencher_formulario(dados_lote)

        if form_page.is_sucesso():
            print("Cadastro realizado com sucesso.")
        else:
            print("Mensagem de sucesso não foi exibida.")
    finally:
        driver.quit()
        stop_http_server(server)


if __name__ == "__main__":
    main()
