"""Serviços compartilhados pelos orquestradores."""

import json
import logging
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Protocol


class DataPool(Protocol):
    """Contrato mínimo para registrar o resultado de um item."""

    def registrar(self, registro: Mapping[str, object]) -> None:
        """Persiste um registro processado."""


class JsonDataPool:
    """DataPool local e fictício, substituível pelo gateway do Maestro."""

    def __init__(self, caminho: Path) -> None:
        self._caminho = caminho

    def registrar(self, registro: Mapping[str, object]) -> None:
        existentes: list[dict[str, object]] = []
        if self._caminho.exists():
            existentes = json.loads(self._caminho.read_text(encoding="utf-8"))
        existentes.append(dict(registro))
        self._caminho.write_text(
            json.dumps(existentes, ensure_ascii=False, indent=2), encoding="utf-8"
        )


@dataclass(frozen=True)
class Evidencia:
    """Rastreabilidade de um lote processado."""

    numero_lote: str
    sucesso: bool
    screenshot: str
    processado_em: str


class EvidenceManager:
    """Cria nomes e arquivos JSON de evidência."""

    def __init__(self, diretorio: Path) -> None:
        self.diretorio = diretorio
        self.diretorio.mkdir(parents=True, exist_ok=True)

    def caminho_screenshot(self, numero_lote: str) -> Path:
        seguro = "".join(c for c in numero_lote if c.isalnum() or c in "-_")
        return self.diretorio / f"{seguro}.png"

    def salvar_json(self, evidencia: Evidencia) -> Path:
        caminho = self.diretorio / f"{evidencia.numero_lote}.json"
        caminho.write_text(
            json.dumps(asdict(evidencia), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return caminho

    @staticmethod
    def agora() -> str:
        return datetime.now(timezone.utc).isoformat()


def criar_logger() -> logging.Logger:
    """Configura logging sem duplicar handlers."""
    logger = logging.getLogger("lote_automation")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
