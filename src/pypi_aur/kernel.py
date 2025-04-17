from typing import Any
from rich.console import Console
import requests
import click


# This is the version of the application.
APP_VERSION = "1.0.0"
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


@click.group()
@click.version_option(APP_VERSION, "-v", "--version", message="%(version)s")
def cli() -> None:
    pass


@cli.command()
def clone() -> None:
    """Clone the repository."""
    click.echo("Executing clone command...")


@cli.command()
def start() -> None:
    """Faz um L gostoso."""
    click.echo("Executing start command...")
