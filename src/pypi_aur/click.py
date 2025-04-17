import click


# This is the version of the application.
APP_VERSION = "0.1.3"


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
