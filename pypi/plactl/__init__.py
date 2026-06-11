"""plactl — official name reservation for the plactl CLI."""

__version__ = "0.0.1"

HOMEPAGE = "https://github.com/plactl"


def main() -> int:
    print(f"plactl v{__version__}")
    print()
    print("plactl is an internal developer platform: GitHub-integrated,")
    print("Terraform-driven AWS provisioning in your own AWS Organization.")
    print()
    print("The plactl CLI has not shipped to PyPI yet — this package reserves")
    print("the name and will become the official distribution when it does.")
    print()
    print(f"Project: {HOMEPAGE}")
    return 1
