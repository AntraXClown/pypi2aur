import click
from pypi2aur.constants import APP_VERSION, APP_NAME
from pypi2aur.kernel import createPKGBUILD, readPyPiDeps, updatePKGBUILD
from rich.console import Console


cl = Console()


@click.group()
@click.version_option(
    version=APP_VERSION, prog_name=APP_NAME, message=f"{APP_NAME} v{APP_VERSION}"
)
def cli() -> None:
    """pypi2aur - PyPi to AUR PKGBUILD generator and helper."""
    # Show program name and version on every invocation

    cl.print(
        f"[bold blue]{APP_NAME}[/bold blue] [bold green]{APP_VERSION}[/bold green]"
    )


@cli.command()
@click.argument("pkg", required=True)
def create(pkg: str) -> None:
    """
    Create a new PKGBUILD file for a pypi package.

    Args:
        pkg (str): Name of the pypi package for which to create a PKGBUILD

    """
    createPKGBUILD(pypiPackage=pkg)


@cli.command()
def update() -> None:
    """
    Update PKGBUILD file based on a pypi package.

    This command updates an existing PKGBUILD file in the current directory
    by reading the package information and updating the relevant fields.
    """
    updatePKGBUILD()


@cli.command()
@click.argument("pkg", required=True)
def showdeps(pkg: str) -> None:
    """
    Read and show pypi package dependencies.

    Args:
        pkg (str): Name of the pypi package to analyze dependencies for

    """
    readPyPiDeps(pypipackage=pkg)
