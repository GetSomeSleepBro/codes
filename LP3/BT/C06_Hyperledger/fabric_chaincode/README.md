# Modern Fabric chaincode (JavaScript): Vehicle Business Network

This is a supportable successor to Set 2's archived Composer model/ACL/logic. Deploy using `fabric-samples/test-network` (Docker, Node, Git and Fabric images required).

Business operations (all values supplied as strings from peer CLI/Gateway):

- `CreateTrader("T1","Alice","Smith","10000")` — create seller with 10,000 cents.
- `CreateTrader("T2","Bob","Jones","20000")` — create buyer with 20,000 cents.
- `CreateVehicle("VIN1","Honda","City","5000","T1")` — create vehicle owned by T1, 5,000 cents.
- `ReadVehicle("VIN1")` — query current owner.
- `TradeVehicle("VIN1","T2")` — deduct buyer's 5,000 cents, credit seller and transfer owner.
- `ReadTrader("T1")`, `ReadTrader("T2")` — verify balances.

All IDs and values are educational, not real money. **Role-based ACL is NOT implemented here**. Unlike Set 2 Composer ACL, any authorized Fabric submitting participant that can invoke this chaincode can submit a transfer; secure production chaincode requires client identity checks and endorsements. Use the `guides/C06_Hyperledger.md` full setup.
