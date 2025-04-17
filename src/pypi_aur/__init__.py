from .kernel import *
from .click import cli, showNameAndVersion


def main() -> None:
    # pkg = fetchPkgInfo(pkg="py-nvfan")
    # cl.print(pkg["info"])
    # if pkg is not None:
    #     cl.print(pkg["latest_version"])

    showNameAndVersion()
    cli()
    # print(aurPackageExists(package_name="confz"))
