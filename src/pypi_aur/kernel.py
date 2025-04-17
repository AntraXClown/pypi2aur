from typing import Any
from rich.console import Console
import requests


cl = Console()


def fetchPkgInfo(pkg: str) -> dict[str, Any] | None:
    """
    Query the PyPI API and return all possible information about the latest version of the package.
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


def aurPackageExists(package_name: str) -> bool:
    """
    Check if a package exists in the AUR (Arch User Repository).

    Args:
        package_name (str): The name of the AUR package.

    Returns:
        bool: True if the package exists, False otherwise.
    """
    url = f"https://aur.archlinux.org/rpc/v5/info/{package_name}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("resultcount", 0) > 0
    except requests.RequestException as e:
        cl.print(f"[red]Error connecting to AUR API: {e}[/red]")
        return False
