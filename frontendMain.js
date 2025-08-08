// frontend/main.js

let provider;
let signer;
let contract;

const contractAddress = "example"; // 배포된 주소
const abi = [
  "function transfer(address to, uint amount) public returns (bool)",
  "function balanceOf(address account) public view returns (uint256)"
];

document.getElementById("connectButton").onclick = async () => {
  if (window.ethereum) {
    await window.ethereum.request({ method: "eth_requestAccounts" });

    provider = new ethers.providers.Web3Provider(window.ethereum);
    signer = provider.getSigner();
    contract = new ethers.Contract(contractAddress, abi, signer);

    const userAddress = await signer.getAddress();
    const balance = await contract.balanceOf(userAddress);
    alert(`Connected: ${userAddress}\nToken Balance: ${balance}`);
  } else {
    alert("MetaMask not detected!");
  }
};

document.getElementById("sendButton").onclick = async () => {
  const to = document.getElementById("recipient").value;
  const amount = document.getElementById("amount").value;

  try {
    const tx = await contract.transfer(to, amount);
    await tx.wait();
    alert(`Sent ${amount} tokens to ${to}`);
  } catch (error) {
    alert("Transfer failed: " + error.message);
  }
};
