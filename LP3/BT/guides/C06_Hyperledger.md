# C06 — Business network using Hyperledger

**Syllabus:** Group C #6. This is one of six regular assignments, so it is optional if C01–C05 are completed, but code and lab steps are included.

**Important 2026 compatibility:** Set 2's `legacy_composer/` contains Hyperledger **Composer** CTO/ACL/transaction processor. Composer was officially deprecated in **2019**; it should NOT be presented as a currently supported deployment method. Use modern **Hyperledger Fabric chaincode** here. Hyperledger Fabric is not Ethereum and does not use MetaMask.

## Prerequisites

Docker Desktop or Docker Engine with enough resources; Git, cURL, Node.js, npm; Linux (or a Linux environment such as WSL2). On macOS this may also work with Docker Desktop. Internet is needed to acquire the official Fabric binaries/images and NPM packages. Follow current prereqs: https://hyperledger-fabric.readthedocs.io/en/latest/prereqs.html

## Option A — simplest supported lab, official sample

1. Follow the official installation directions: https://hyperledger-fabric.readthedocs.io/en/latest/install.html; install `fabric-samples` with test-network components and Fabric binaries.
2. In terminal go to `fabric-samples/test-network`.
3. Run `./network.sh down` to clear a previous test network.
4. Run `./network.sh up createChannel -c mychannel -ca` (starts Org1, Org2, orderer and channel; may require Docker first run).
5. Run `./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-javascript/ -ccl javascript`.
6. Read `/asset-transfer-basic/chaincode-javascript/lib/assetTransfer.js`. The sample asset smart contract is a basic **business network**: participants/orgs maintain shared asset records with ownership transfers.
7. Follow the official interaction tutorial to create/read/transfer assets: https://hyperledger-fabric.readthedocs.io/en/latest/write_first_app.html.
8. Record network topology, channel, deployed chaincode name, asset ID, before/after owner, transaction success, Docker containers.
9. Stop network: `./network.sh down`.

## Option B — use the original *vehicle-trading* lab code, modernized

`BT/C06_Hyperledger/fabric_chaincode/` contains a JS chaincode package (BusinessNetwork.js + package.json) that supports create trader, create vehicle, transfer with balance checks, and query. Copy the **whole `fabric_chaincode` directory** into `fabric-samples/vehicle-business-network/`.

From `fabric-samples/test-network` (after bringing network up):

```bash
./network.sh deployCC -ccn vehicle -ccp ../vehicle-business-network -ccl javascript
```

Then use Fabric Gateway SDK or official `peer chaincode invoke/query` instructions to call `CreateTrader`, `CreateVehicle`, `TradeVehicle`, `ReadTrader`, and `ReadVehicle` (required arguments described in `fabric_chaincode/README.md`). No `Composer` package required. The code is locally syntax-checked, but an actual Fabric deployment still needs to be run on your own machine.

**Do not claim an actual fabric transaction, network, gas fee, or screenshot unless you performed it.** Fabric chaincode operations are not paid in Ethereum gas.

Official docs: https://hyperledger-fabric.readthedocs.io/en/latest/test_network.html. Composer deprecation notice: https://hyperledger.github.io/composer/latest/tutorials/tutorials.html.
