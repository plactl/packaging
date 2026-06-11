fn main() {
    println!("plactl v{}", env!("CARGO_PKG_VERSION"));
    println!();
    println!("plactl is an internal developer platform: GitHub-integrated,");
    println!("Terraform-driven AWS provisioning in your own AWS Organization.");
    println!();
    println!("The plactl CLI has not shipped to crates.io yet — this crate reserves");
    println!("the name and will become the official distribution when it does.");
    println!();
    println!("Project: {}", env!("CARGO_PKG_HOMEPAGE"));
    std::process::exit(1);
}
