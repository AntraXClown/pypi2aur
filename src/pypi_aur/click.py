import click

# This is the version of the application.
APP_VERSION = "0.1.3"
APP_NAME = "pypi-aur"


def showNameAndVersion() -> None:
    """
    Show the name and version of the application.

    Returns:
        None
    """
    click.echo(f"{APP_NAME} version {APP_VERSION}")


@click.group()
@click.version_option(APP_VERSION, "-v", "--version", message="%(version)s")
def cli() -> None:
    """pypi-aur - PyPi to AUR PKGBUILD generator and helper."""
    # Show program name and version on every invocation
    pass


@cli.command()
@click.argument("pkg", required=True)
def create(pkg: str) -> None:
    """
    Create a new PKGBUILD file for a pypi package.

    Args:
        pkg (str): Name of the pypi  package for which to create a PKGBUILD

    """
    click.echo(f"Creating package {pkg}...")


@cli.command()
def start() -> None:
    """Start the application."""
    click.echo("Executing start command...")
