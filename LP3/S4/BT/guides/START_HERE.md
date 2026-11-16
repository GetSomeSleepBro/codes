# Before any BT practical

## Option A — fastest, no account/testnet funding (recommended for the bank and student contracts)

1. Open https://remix.ethereum.org.
2. File Explorer → Create New File → name it as the required `.sol` file.
3. Open corresponding `.sol` file inside `LP3/BT/`, copy **all source**, paste into Remix, and save.
4. Solidity Compiler → select a compatible `0.8.20` or newer `0.8.x` compiler → **Compile**.
5. Deploy & Run → Environment **Remix VM** → choose Account 1 → Deploy.
6. Open deployed contract and follow individual guide; record transaction receipt gas shown in Remix terminal.

## Option B — real testnet (for wallet setup and contract deployment)

1. Install MetaMask ONLY from https://metamask.io and keep the recovery phrase OFFLINE, privately.
2. MetaMask → Networks → enable **Show test networks** → choose **Sepolia**. Its chain ID is `11155111`.
3. Acquire small amounts of **test Sepolia ETH** from a reputable faucet for eligible accounts; test tokens have no cash value.
4. Open Remix in the SAME browser. Set Deploy & Run → Environment to **Browser Extension** (older Remix calls it **Injected Provider**) and approve MetaMask.
5. Confirm network/account in both apps. On deployment or transactions, review the wallet popup and approve. Save the transaction hash.
6. For browser dApps, deploy the Solidity contract on a network the frontend can access through MetaMask, NOT on Remix VM; Remix VM is isolated from the wallet provider.

**Safety:** Do not use mainnet, purchase tokens, share keys, or import a recovery phrase from an unknown source. Never accept a request to transfer real ETH to a lab address. If Remix changes labels, follow the official Deploy & Run docs: https://remix-ide.readthedocs.io/en/latest/run.html

## Standard evidence for a practical journal

Aim, requirements, short explanation, algorithm/steps, contract/program listing, input values, own observed output, transaction hash where applicable, Gas Used/Gas Price/Transaction Fee, conclusion, examiner signature. Leave observations blank until actually executed.
