// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// @notice Lab demo for account balances backed 1:1 by deposited test Ether.
/// @dev Educational contract; do not deploy with valuable real funds.
contract Bank {
    mapping(address => bool) public accountExists;
    mapping(address => uint256) private balances;
    bool private locked;

    event AccountCreated(address indexed account);
    event Deposited(address indexed account, uint256 amount);
    event Withdrawn(address indexed account, uint256 amount);
    event InternalTransfer(address indexed from, address indexed to, uint256 amount);

    modifier nonReentrant() {
        require(!locked, "Reentrancy blocked");
        locked = true;
        _;
        locked = false;
    }

    function createAccount() external {
        require(!accountExists[msg.sender], "Account already exists");
        accountExists[msg.sender] = true;
        emit AccountCreated(msg.sender);
    }

    /// @notice Set Remix VALUE, then call deposit(). Never supply an unbacked amount.
    function deposit() external payable {
        require(accountExists[msg.sender], "Create account first");
        require(msg.value > 0, "Zero deposit");
        balances[msg.sender] += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    function withdraw(uint256 amountWei) external nonReentrant {
        require(amountWei > 0 && balances[msg.sender] >= amountWei, "Insufficient balance");
        balances[msg.sender] -= amountWei; // checks-effects-interactions
        (bool success,) = payable(msg.sender).call{value: amountWei}("");
        require(success, "Ether transfer failed");
        emit Withdrawn(msg.sender, amountWei);
    }

    /// @notice Transfers INTERNAL ledger balance; does not send Ether to the recipient wallet.
    function transferInternal(address recipient, uint256 amountWei) external {
        require(accountExists[msg.sender] && accountExists[recipient], "Both accounts must exist");
        require(recipient != address(0) && amountWei > 0, "Invalid recipient or amount");
        require(balances[msg.sender] >= amountWei, "Insufficient balance");
        balances[msg.sender] -= amountWei;
        balances[recipient] += amountWei;
        emit InternalTransfer(msg.sender, recipient, amountWei);
    }

    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
