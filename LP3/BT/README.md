# Group C: Blockchain Technology — practical execution manual

For each university experiment read the matching **copy-and-follow guide** in `guides/`. The first five plus the e-voting mini-project cover the compulsory minimum. C06 is also supplied but requires extra Hyperledger Fabric software.

| Practical | File to open/copy | Step-by-step guide |
|---|---|---|
| C01 MetaMask installation + gas study | No Solidity file | [`guides/C01_Metamask_Gas.md`](guides/C01_Metamask_Gas.md) |
| C02 Create crypto wallet | No Solidity file | [`guides/C02_Create_Wallet.md`](guides/C02_Create_Wallet.md) |
| C03 Bank account contract | `C03_Bank.sol` | [`guides/C03_Bank.md`](guides/C03_Bank.md) |
| C04 Student struct, array + fallback | `C04_StudentRegistry.sol` | [`guides/C04_Student.md`](guides/C04_Student.md) |
| C05 Survey types of blockchain | `C05_Survey_Report.md` | [`guides/C05_Survey.md`](guides/C05_Survey.md) |
| C06 Hyperledger business network | `C06_Hyperledger/fabric_chaincode/` | [`guides/C06_Hyperledger.md`](guides/C06_Hyperledger.md) |
| MP01 E-Voting | `MP01_EVoting/Voting.sol` + `index.html` | [`guides/MP01_EVoting.md`](guides/MP01_EVoting.md) |

**Order:** install MetaMask → create a throwaway study wallet → use Remix VM for contracts → optionally try Sepolia with test ETH → run the mini-project frontend on the same network used to deploy its smart contract. Do not switch networks between contract deployment and frontend connection.

**Tools:** https://remix.ethereum.org (or https://app.remix.live) | https://metamask.io | https://sepolia.etherscan.io | https://hyperledger-fabric.readthedocs.io/

**Gas note:** Reading via `view` using Remix's call UI is typically an off-chain call and does not submit a transaction or incur a network fee. Deploying or writing storage does. Gas usage varies, so record observed values; do not copy made-up results.

**Reality check:** Python and C++ programs can be tested locally. Solidity compiler/MetaMask/Sepolia and a full Fabric deployment require external tools and cannot be asserted verified until run there. `docs/VERIFICATION.md` records the actual extent of local testing.
