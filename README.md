# plactl packaging

Source for the `plactl` packages published to public registries. These are
currently **name reservations**: each package ships a stub binary that prints
project information and exits. When the plactl CLI ships, real releases will
be published through these same names.

| Registry | Package | Source |
|----------|---------|--------|
| npm | [`plactl`](https://www.npmjs.com/package/plactl) | [`npm/`](./npm) |
| PyPI | [`plactl`](https://pypi.org/project/plactl/) | [`pypi/`](./pypi) |
| crates.io | [`plactl`](https://crates.io/crates/plactl) | [`crates/`](./crates) |

**plactl** is an internal developer platform: GitHub-integrated,
Terraform-driven AWS provisioning that runs entirely in your own AWS
Organization.
