from .kernel import *


def main() -> None:
    pkg = fetchPkgInfo(pkg="py-nvfan")
    # cl.print(pkg["info"])
    # cl.print(pkg["latest_version"])
    # cl.print(pkg["release_files"])
    if pkg is not None:
        cl.print(pkg["info"])
        cl.print(pkg["latest_version"])
        cl.print(pkg["release_files"])
