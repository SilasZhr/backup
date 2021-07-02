const { BN } = require('web3-utils');
const merkleRoot = require('../test/generatedReal.js');
const now = Math.floor(new Date().getTime() / 1000);
const start_time = now + 86400;
const end_time = now + 86400 * 6;
var rice_address = "0x19dFDdE99b38Fcf024a0465bFE7424223A85fBA8";
const amount = "1000000000000000000000000";

async function main() {

  const [deployer] = await ethers.getSigners();

  console.log(
    "Deploying contracts with the account:",
    deployer.address
  );

  console.log("Account balance:", (await deployer.getBalance()).toString());

  /**
   * should remove in develop environment
   */
  const test_token = await ethers.getContractFactory("TestTokenA");
  const token = await test_token.deploy(amount);
  rice_address = token.address;
  console.log("testToken created", token.address, ", amount:", (await token.balanceOf(deployer.address)).toString());


  const Airdrop = await ethers.getContractFactory("Airdrop");
  const airdrop = await Airdrop.deploy(rice_address, merkleRoot['merkleRoot'], start_time, end_time);
  console.log("airdrop address:", airdrop.address);


}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });