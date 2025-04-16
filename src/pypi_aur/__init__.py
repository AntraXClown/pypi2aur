from .kernel import *


def main() -> None:
    pkg = fetchPkgInfo(pkg="py-nvfan")
    if pkg:
        # cl.print(pkg["info"])
        # cl.print(pkg["latest_version"])
        cl.print(pkg["release_files"])
    else:
        print("No package found.")
