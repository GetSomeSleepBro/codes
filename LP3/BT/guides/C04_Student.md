# C04 — Student registry: struct, array and fallback, plus gas measurement

**Syllabus:** Group C #4. **Copy program:** `../C04_StudentRegistry.sol` (contract `StudentRegistry`).

1. Remix → new `StudentRegistry.sol` → paste the corresponding `BT/C04_StudentRegistry.sol` code.
2. Compile with compatible Solidity 0.8.20+.
3. Deploy with Remix VM, no Ether Value. Copy contract address and gas receipt.
4. Expand deployed `StudentRegistry` → call **`getStudentCount()`** (view). Initial count: 0.
5. Call **`addStudent("Sairaj", 21)`** (in Remix enter `"Sairaj"` for the string and `21` for uint256). Inspect receipt and gas.
6. Call **`addStudent("Sonal", 21)`**; count should become 2. Read both entries using **`getStudent(0)`** and **`getStudent(1)`** (index is **zero-based**, not roll number).
7. For **`receive()`**, use Remix deployed-contract **Low level interactions** (if displayed): set Value to 1 wei, leave CALLDATA empty (`0x`) and click Transact. Check `totalEtherReceived()` increases by 1 and `EtherReceived` event includes `viaFallback=false`.
8. For **`fallback()`**, use CALLDATA `0x1234` (unknown selector), Value `0` or `1` wei and click Transact. Check event has `viaFallback=true`. The exact low-level panel position varies with Remix UI.
9. Try **`getStudent(99)`**; the call should revert with invalid index. This confirms input validation.
10. For **testnet/gas** evaluation, repeat deployment using Browser Extension + Sepolia; inspect every state-changing transaction in https://sepolia.etherscan.io. Record **Gas Used** and **Effective Gas Price**, then compute fee.

| Operation | Transaction? | Expected | Gas used | Fee |
|---|---|---|---|---|
| Deploy | Yes | Contract created | | |
| addStudent (first) | Yes | count 1 | | |
| addStudent (second) | Yes | count 2 | | |
| getStudent(0) | No if called off-chain | Returns student | N/A | N/A |
| receive (1 wei) | Yes | received counter +1 | | |
| fallback unknown selector | Yes | event viaFallback=true | | |

**Note:** Set 2 includes an alternate student contract with roll numbers, departments and marks in `BT/alternatives/Set2_StudentData.sol`; its function signatures differ from this main Set 1 version. If demonstrating that variant, call `addStudent(rollNo, name, department, marks)` instead.
