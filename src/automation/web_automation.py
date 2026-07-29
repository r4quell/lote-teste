"""Orquestrador Playwright."""

from typing import Iterable, Mapping

from playwright.sync_api import sync_playwright

from src.automation.common import DataPool, EvidenceManager, Evidencia, criar_logger
from src.pages import FormPage


def executar(
    url: str,
    lotes: Iterable[Mapping[str, str]],
    datapool: DataPool,
    evidencias: EvidenceManager,
    headless: bool = True,
) -> None:
    """Processa os lotes mantendo regras de negócio fora do Page Object."""
    logger = criar_logger()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        page = browser.new_page()
        formulario = FormPage(page)
        try:
            formulario.abrir(url)
            for lote in lotes:
                numero = lote["numero_lote"]
                try:
                    formulario.preencher_lote(lote)
                    sucesso = formulario.is_sucesso()
                    screenshot = evidencias.caminho_screenshot(numero)
                    page.screenshot(path=str(screenshot), full_page=True)
                    registro = Evidencia(
                        numero, sucesso, str(screenshot), evidencias.agora()
                    )
                    evidencias.salvar_json(registro)
                    datapool.registrar(vars(registro))
                    logger.info("Lote %s processado; evidência: %s", numero, screenshot)
                except Exception:
                    logger.exception("Falha ao processar o lote %s", numero)
                    raise
        finally:
            browser.close()
