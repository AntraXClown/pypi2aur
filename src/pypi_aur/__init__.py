from .kernel import *
from .click import cli


def main() -> None:
    pkg = fetchPkgInfo(pkg="py-nvfan")
    # cl.print(pkg["info"])
    if pkg is not None:
        cl.print(pkg["latest_version"])

    # cli()
    # print(aurPackageExists(package_name="confz"))
