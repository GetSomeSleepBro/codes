// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    // Mapping to store each customer's account balance securely by address
    mapping(address => uint256) private balances;

    // Events to log deposits and withdrawals on the blockchain
    event Deposited(address indexed accountHolder, uint256 amount);
    event Withdrawn(address indexed accountHolder, uint256 amount);

    // 1. Deposit Money
    // Allows users to send Ether into their bank account balance
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    // 2. Withdraw Money
    // Allows users to withdraw a specified amount from their balance
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct balance first to prevent re-entrancy vulnerabilities
        balances[msg.sender] -= amount;

        // Transfer funds back to the user's wallet
        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "ETH transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // 3. Show Balance
    // Returns the current Ether balance of the caller's account
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    // Receive function to automatically handle direct ETH transfers as deposits
    receive() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }
}
