"""CLI da automação fictícia de lotes."""

import argparse
from pathlib import Path
from typing import Sequence

from src.automation.common import EvidenceManager, JsonDataPool


LOTE_DEMONSTRACAO = {
    "numero_lote": "LOTE-DEMO-0001",
    "produto": "Notebook",
    "status": "Pendente",
}


def main(argv: Sequence[str] | None = None) -> int:
    """Executa a automação pelo motor selecionado."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--engine", choices=("selenium", "playwright"), default="selenium")
    parser.add_argument("--headed", action="store_true")
    args = parser.parse_args(argv)

    raiz = Path(__file__).resolve().parent.parent
    url = (raiz / "lote-teste.html").as_uri()
    datapool = JsonDataPool(raiz / "datapool.json")
    evidencias = EvidenceManager(raiz / "evidencias")

    if args.engine == "playwright":
        from src.automation.web_automation import executar
    else:
        from src.automation.selenium_automation import executar
    executar(url, [LOTE_DEMONSTRACAO], datapool, evidencias, not args.headed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
