# MP01 — E-Voting dApp (Group C mini-project #7)

Two variants are included. **Set 1 main:** `BT/MP01_EVoting/Voting.sol` with `index.html` and a simpler vote-by-wallet demonstration. **Set 2 extended:** under `extended/` with admin candidate registration, voter allowlisting and winner display. Use ONE contract and ITS MATCHING frontend; do not mix files because the ABIs are different.

## Main Set 1 — Solidity contract + browser UI

### A. Deploy in Remix

1. Create a study MetaMask wallet and switch to **Sepolia**. Get a small amount of Sepolia test ETH; the browser dApp needs wallet access. A contract deployed to **Remix VM cannot be reached through a normal MetaMask browser dApp**.
2. Open https://remix.ethereum.org and create file `Voting.sol`; copy full code from `BT/MP01_EVoting/Voting.sol`.
3. Compiler: Solidity 0.8.20+; compile, ensure no errors.
4. Deploy & Run → **Browser Extension** (sometimes "Injected Provider") → approve MetaMask → verify Sepolia network.
5. Under deployment arguments provide a string array of **at least two candidate names**, for example `['Alice','Bob']` in the Remix parameter UI (the UI may require JSON double quotes: `["Alice","Bob"]`). Value 0. Deploy. Record contract address and transaction hash.
6. In deployed contract call `getCandidateCount()` (should be 2), then `getCandidate(0)` and `getCandidate(1)`; before opening election both vote counts are zero.
7. As the deployer/owner call **`openElection()`**. Only the owner account may do this.
8. Open `BT/MP01_EVoting/index.html` using a local HTTP server rather than a file URL: from `LP3` run `python -m http.server 8000` then visit `http://localhost:8000/BT/MP01_EVoting/` in the MetaMask browser. This page currently loads **ethers.js from an online CDN**, so Internet is necessary.
9. Click **Connect MetaMask** → approve; paste the exact contract address; click **Load election**; check phase `Open` and candidate list.
10. Choose candidate → **Submit vote** → review and approve MetaMask → wait for confirmation → refresh results. Using the SAME account again must revert (`Address already voted`). Use another address to demonstrate a second vote.
11. From Remix, switch back to the OWNER account and call **`closeElection()`**. Return to the dApp and click **Refresh results**. Election should show `Closed`; new votes must revert.
12. Record counts, account address prefixes, contract address, gas receipts and limitations. This demo enforces **one vote per address, not one verified person**; it is NOT an identity-proof election system.

### B. Extended Set 2 dApp (optional, registration + winner)

1. Copy/deploy `BT/MP01_EVoting/extended/Voting.sol` in Remix with Browser Extension + Sepolia. No constructor parameters.
2. Using deployer/admin account call `addCandidate("Alice")` and `addCandidate("Bob")`.
3. With the admin account call `registerVoter(<VOTER_PUBLIC_ADDRESS>)` for every test wallet that is allowed to vote. Add **before** starting the election.
4. Call `startVoting()`. After this the candidate list and voter registry are frozen.
5. Serve LP3 using `python -m http.server 8000`. Open `http://localhost:8000/BT/MP01_EVoting/extended/`. This variant includes an `ethers.umd.min.js` file for the library, but **the blockchain connection still requires an available network/RPC**.
6. Paste the extended contract address → Connect MetaMask → admin panel or candidates list. Switch MetaMask to a *registered voter account* and refresh/reconnect if necessary; click Vote and sign.
7. Try voting again from the same address: the contract must revert. Unregistered addresses must also revert.
8. Switch to admin account → `endVoting()`; refresh frontend, click `Show Winner`. The contract cannot be restarted after closure (corrected from Set 2). A tie returns the first highest-vote candidate; this is a demo decision, not a real election tie-break policy.

### Evidence checklist

| Item | Source |
|---|---|
| Contract deployment address | Remix terminal / Sepolia Etherscan |
| Candidate list before voting | Remix read-only calls |
| Start/open transaction | Remix transaction receipt |
| Successful vote | MetaMask + explorer; dApp table |
| Failed duplicate vote | Contract revert/error message |
| Closed election & results | Remix + frontend refresh |

**Security limitations:** addresses can be created freely (main variant), all votes are public and coercible, no voter anonymity, no legal identity proof, no auditing framework. Educational demonstration only.
