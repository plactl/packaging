#!/usr/bin/env node

const pkg = require("../package.json");

console.log(`plactl v${pkg.version}`);
console.log("");
console.log("plactl is an internal developer platform: GitHub-integrated,");
console.log("Terraform-driven AWS provisioning in your own AWS Organization.");
console.log("");
console.log("The plactl CLI has not shipped to npm yet — this package reserves");
console.log("the name and will become the official distribution when it does.");
console.log("");
console.log(`Project: ${pkg.homepage}`);

process.exit(1);
