// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 BT Assignment 3
 Write a smart contract on a test network, for Bank account of a customer for
 following operations:
   - Deposit money
   - Withdraw Money
   - Show balance

 How to run: open https://remix.ethereum.org -> new file Bank.sol -> paste -> Compile (0.8.x)
 -> Deploy & Run -> Environment "Remix VM" (offline) or "Injected Provider - MetaMask" (Sepolia).
 Deposit: put amount in the VALUE box (e.g. 1 ether), click deposit.
*/

contract Bank {
    address public owner;
    mapping(address => uint256) private balances;
    mapping(address => bool) public hasAccount;

    event AccountCreated(address indexed customer);
    event Deposited(address indexed customer, uint256 amount);
    event Withdrawn(address indexed customer, uint256 amount);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyCustomer() {
        require(hasAccount[msg.sender], "Account does not exist. Create account first.");
        _;
    }

    function createAccount() public {
        require(!hasAccount[msg.sender], "Account already exists");
        hasAccount[msg.sender] = true;
        emit AccountCreated(msg.sender);
    }

    // Deposit Ether sent with the transaction (msg.value)
    function deposit() public payable onlyCustomer {
        require(msg.value > 0, "Deposit amount must be greater than 0");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    // Withdraw amount (in wei) back to the customer's wallet
    function withdraw(uint256 amount) public onlyCustomer {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;          // update state before transfer (re-entrancy safe)
        payable(msg.sender).transfer(amount);
        emit Withdrawn(msg.sender, amount);
    }

    function showBalance() public view onlyCustomer returns (uint256) {
        return balances[msg.sender];
    }

    // Total Ether held by the bank contract
    function bankBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
