const hre = require("hardhat");

async function main() {
  const AuditRegistry = await hre.ethers.getContractFactory("AuditRegistry");
  const audit = await AuditRegistry.deploy();

  await audit.deployed();

  console.log("AuditRegistry deployed to:", audit.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});