# C01 — Install MetaMask and study Ether spent per transaction

**Syllabus:** Group C #1. **Files:** none; browser + MetaMask + blockchain explorer.

## Procedure

1. Install MetaMask from https://metamask.io; make a **new educational wallet** following `START_HERE.md`. Use a disposable test account, never a wallet containing real funds.
2. Open MetaMask → Networks → enable Show test networks → choose Sepolia (chain ID `11155111`).
3. Find your own public wallet address (`0x...`). Do not reveal private keys or seed phrases.
4. Get a small amount of Sepolia **test** ETH from a legitimate faucet if eligible; or study an existing public Sepolia transaction if none is available.
5. To generate a transaction, send a *very small* amount (e.g. 0.0001 SepoliaETH) to another test account you control. Double-check the selected testnet.
6. Approve transaction and copy its transaction hash from MetaMask Activity.
7. Open `https://sepolia.etherscan.io/tx/<YOUR_TRANSACTION_HASH>`.
8. Record **Gas Used**, **Effective Gas Price**, **Transaction Fee**, **Block**, **Status**, **From** and **To**. Transaction Fee in ETH = `Gas Used × Effective Gas Price (in gwei) / 10^9`.
9. Explain the difference between *transfer amount* (Ether being sent) and *transaction fee* (gas paid to process it).
10. Optional: repeat a contract interaction and compare gas usage; creating smart-contract state usually uses more gas than a simple transfer.

## Practical observation (fill after doing)

| Transaction type | Network | Hash | Gas Used | Effective Gas Price | Fee (ETH) |
|---|---|---|---|---|---|
| Test ETH transfer | Sepolia | | | | |
| Contract interaction (optional) | Sepolia | | | | |

**Expected understanding:** base transfer generally uses 21,000 gas, but actual fees and gas can vary. Never submit a fee value you did not measure.
