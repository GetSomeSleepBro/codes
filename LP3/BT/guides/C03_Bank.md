# C03 — Bank account smart contract (deposit, withdraw, show balance)

**Syllabus:** Group C #3. **Copy program:** `../C03_Bank.sol` (contract `Bank`). **Network:** Remix VM first, Sepolia optional.

## Click-by-click lab

1. Open https://remix.ethereum.org → File Explorer → new `Bank.sol` → paste entire `BT/C03_Bank.sol` source.
2. Solidity Compiler → version 0.8.20+ → Compile `Bank.sol`. Check there are **no errors**.
3. Deploy & Run → Remix VM → Account 1 → Value `0` → Contract `Bank` → **Deploy**.
4. In Deployed Contracts expand `Bank`. Note its address and deploy gas in the terminal.
5. Click **`createAccount()`** using Account 1. This must be done before depositing. Record transaction receipt.
6. Set Remix **Value** to `0.01 ether` (or `10000000000000000 wei`); click **`deposit()`**. Value is the ETH sent with the payable transaction, *not* a function parameter. Record successful receipt.
7. Set Value back to `0` before the next transaction. Click **`getBalance()`**. Expected **logical ledger balance**: `10000000000000000` wei. This is a view call and normally does not require a mined transaction.
8. Call **`withdraw(5000000000000000)`**, which withdraws **0.005 ETH**. Check `getBalance()` again; the ledger now should show **0.005 ETH** in wei.
9. Attempt **`withdraw(9000000000000000)`**; it must revert with insufficient balance. Record the revert (do not consider it a successful withdrawal).
10. Switch Remix VM account to Account 2. Check `getBalance()` starts at 0; create an account for Account 2 and repeat the deposit/withdraw if requested.
11. Optional: first create Account 2 and test `transferInternal(Account2Address, 1000000000000000)` from Account 1; this updates the *internal bank ledger*, not the recipient wallet balance.
12. For actual testnet deployment, switch to Browser Extension/MetaMask on Sepolia, obtain test ETH, deploy again, repeat with smaller deposit and record explorer gas.

## Observation table

| Step | Function + arguments | Expected property | Observed result | Gas |
|---|---|---|---|---|
| 1 | deploy `Bank` | Contract address created | | |
| 2 | `createAccount()` | Account registered | | |
| 3 | `deposit()` + 0.01 ETH Value | Stored balance increases | | |
| 4 | `getBalance()` | Returns deposited wei | | view/no fee |
| 5 | `withdraw(5000000000000000)` | Stored balance decreases | | |
| 6 | `withdraw(9000000000000000)` | Reverts | | |

**Concepts:** `payable`, `msg.sender`, `msg.value`, `mapping`, `require`, events, wei, checks-effects-interactions, non-reentrancy. **Never use real funds.**
