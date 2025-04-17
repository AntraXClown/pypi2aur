from typing import Any
from rich.console import Console
import requests


cl = Console()


def fetchPkgInfo(pkg: str) -> dict[str, Any] | None:
    """
    Consulta a API do PyPI e retorna todas as informações possíveis sobre a última versão do pacote.
    """
    url: str = f"https://pypi.org/pypi/{pkg}/json"
    try:
        resp: requests.Response = requests.get(url=url)
        resp.raise_for_status()
        data = resp.json()
        latest_version = data["info"]["version"]
        version_info = data["releases"].get(latest_version, [])
        return {
            "info": data["info"],
            "latest_version": latest_version,
            "release_files": version_info,
            "urls": data.get("urls", []),
        }
    except Exception as e:
        return None
