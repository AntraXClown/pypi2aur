from nturl2path import url2pathname
from .kernel import *
from .click import cli, showNameAndVersion
from slugify import slugify


def main() -> None:
    showNameAndVersion()
    cli()
