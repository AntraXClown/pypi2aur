from rich.console import Console


cl = Console()


def fetchPkgInfo(pkg: str) -> dict:
    """
    Fetch package Pypi information
    """
    cl.print(f"[bold yellow]Fetching package info for {pkg}...[/bold yellow]")
    return {
        "name": pkg,
        "version": "1.0.0",
        "description": "A sample package",
        "author": "John Doe",
        "license": "MIT",
        "url": "https://example.com",
    }
