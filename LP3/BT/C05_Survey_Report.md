# Survey Report: Types of Blockchains and their Real-Time Use Cases

## 1. Introduction
A blockchain is a decentralized, distributed and immutable ledger that records transactions in blocks. Each block is linked to the previous block through a cryptographic hash. Every node keeps a copy of the ledger, and new blocks are added using a consensus mechanism (Proof of Work, Proof of Stake, PBFT, Raft, etc.). Different applications need different levels of openness, privacy and speed, so blockchains are classified into four main types.

## 2. Types of Blockchain

### 2.1 Public Blockchain (Permissionless)
- Anyone can join, read, write and take part in consensus. Fully decentralized.
- Consensus: Proof of Work (Bitcoin), Proof of Stake (Ethereum).
- **Advantages:** transparency, high security, censorship-resistant, no central authority.
- **Disadvantages:** slow (Bitcoin ≈ 7 TPS), high energy use (PoW), transaction fees, limited privacy.
- **Examples:** Bitcoin, Ethereum, Solana, Litecoin.
- **Use cases:** cryptocurrency payments, DeFi (Uniswap, Aave), NFTs, DAOs, crowdfunding (ICOs).

### 2.2 Private Blockchain (Permissioned)
- Controlled by one organization, which decides who can join and what each node can do.
- Consensus: Raft, PBFT, Proof of Authority.
- **Advantages:** fast, scalable, private, low cost, the organization has control.
- **Disadvantages:** centralized, less trustless, a single point of control can be compromised.
- **Examples:** Hyperledger Fabric (single-org), R3 Corda, Multichain.
- **Use cases:** internal auditing, supply-chain management within a company, asset tracking, database management.

### 2.3 Consortium (Federated) Blockchain
- Semi-decentralized: governed by a **group of organizations** rather than one.
- Pre-selected nodes validate blocks.
- **Advantages:** more decentralized than private, efficient, privacy between members, shared cost.
- **Disadvantages:** less transparent than public, needs trust and agreement among members.
- **Examples:** R3 (banks), Energy Web Foundation, IBM Food Trust, Marco Polo (trade finance).
- **Use cases:** inter-bank payments and settlements, trade finance, insurance claims sharing, research collaboration.

### 2.4 Hybrid Blockchain
- Combines a private permissioned network with a public blockchain. Some data is private, and some is published publicly for verification.
- **Advantages:** controlled privacy with public verifiability, flexible, cheaper.
- **Disadvantages:** complex to design, not fully transparent.
- **Examples:** XinFin (XDC), Dragonchain, IBM Food Trust (partially).
- **Use cases:** real estate, government records, healthcare, regulated finance.

## 3. Comparison
| Feature | Public | Private | Consortium | Hybrid |
|---|---|---|---|---|
| Access | Anyone | Single organization | Group of organizations | Mixed |
| Decentralization | Full | Low | Partial | Partial |
| Speed (TPS) | Low | High | High | Medium–High |
| Privacy | Low | High | High | Configurable |
| Consensus | PoW / PoS | Raft / PoA | PBFT / Raft | Varies |
| Immutability | Very high | Can be altered by owner | High | High |
| Examples | Bitcoin, Ethereum | Hyperledger Fabric | R3 Corda, IBM Food Trust | XinFin, Dragonchain |

## 4. Real-Time Use Cases
| Domain | Use case | Example |
|---|---|---|
| Finance | Cross-border payments, settlements | RippleNet, JP Morgan Onyx (JPM Coin) |
| Supply chain | Food traceability from farm to store | Walmart + IBM Food Trust (trace mango origin in 2.2 s instead of 7 days) |
| Healthcare | Secure sharing of patient records | MedRec, Estonia e-Health |
| Government | Land records, e-voting, digital identity | Andhra Pradesh land registry, Estonia e-Residency |
| Education | Tamper-proof certificates | MIT Blockcerts (digital diplomas) |
| Energy | Peer-to-peer energy trading | Power Ledger, Energy Web |
| Insurance | Automatic claims via smart contracts | AXA Fizzy (flight-delay insurance) |
| Real estate | Tokenized property ownership | Propy |
| Digital art | NFTs, royalties | OpenSea, CryptoPunks |
| India specific | Digital Rupee (e₹) pilot, trade-finance network | RBI CBDC pilot, Indian banks' blockchain consortium |

## 5. Challenges
Scalability, energy consumption (PoW), regulatory uncertainty, interoperability between chains, smart-contract bugs, key-management by users.

## 6. Conclusion
Public blockchains suit trustless, transparent systems such as cryptocurrency. Private and consortium blockchains suit enterprises that need speed and privacy. Hybrid blockchains combine both. The choice depends on the application's needs for **trust, privacy, speed and control**.

## References
1. Imran Bashir, *Mastering Blockchain*, Packt.
2. Melanie Swan, *Blockchain: Blueprint for a New Economy*, O'Reilly.
3. Hyperledger Foundation documentation – https://www.hyperledger.org
4. Ethereum documentation – https://ethereum.org/developers
