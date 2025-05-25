def main() -> None:
    from pypi2aur.click import cli, showNameAndVersion

    showNameAndVersion()
    cli()
