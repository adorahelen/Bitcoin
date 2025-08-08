const { ethers } = require("hardhat");

async function main() {
  const MyToken = await ethers.getContractFactory("MyToken");
  const myToken = await MyToken.deploy(1000);

  await myToken.waitForDeployment(); // 🔄 .deployed() 대신

  console.log("MyToken deployed to:", await myToken.getAddress()); // 🔄 address 접근 방식 변경
}

main().catch((error) => {
  console.error("❌ 배포 오류:", error);
  process.exitCode = 1;
});
