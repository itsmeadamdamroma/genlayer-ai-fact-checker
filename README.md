<h1 align="center">🔍 AI Fact Checker — Intelligent Contract</h1>

<p align="center">
  <strong>Decentralized fact verification powered by AI consensus on GenLayer</strong>
</p>

<p align="center">
  <a href="https://explorer-bradbury.genlayer.com/address/0x22F8D9A5FdB4f654c72411267E62FE1fEa7CeFbf">
    <img src="https://img.shields.io/badge/Contract-Live%20on%20Bradbury-7C3AED?style=for-the-badge" />
  </a>
  <a href="https://dorahacks.io/hackathon/genlayer-bradbury/buidl">
    <img src="https://img.shields.io/badge/Hackathon-GenLayer%20Bradbury-FF6B35?style=for-the-badge" />
  </a>
  <a href="https://genlayer.com">
    <img src="https://img.shields.io/badge/Built%20on-GenLayer-000?style=for-the-badge" />
  </a>
</p>

---

## 🌟 Overview

**AI Fact Checker** is an Intelligent Contract deployed on the **GenLayer Bradbury Testnet** that enables decentralized, AI-powered fact verification. Users submit claims about real-world events along with a source URL, and the contract autonomously:

1. 🌐 **Fetches evidence** from the web in real-time
2. 🧠 **Analyzes the claim** using AI reasoning (LLM inference)
3. ⚖️ **Reaches consensus** through GenLayer's Optimistic Democracy
4. 📝 **Stores the verdict** on-chain with confidence scores

This creates a **trustless, decentralized truth layer** — no single entity decides what's true; AI validators collectively evaluate evidence and reach consensus.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                  User Submit Claim              │
│         (claim_text + source_url)               │
└──────────────────────┬──────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────┐
│          GenLayer Bradbury Testnet              │
│                                                 │
│  ┌─────────────────────────────────────────┐    │
│  │        AIFactChecker Contract           │    │
│  │                                         │    │
│  │  1. gl.get_webpage(source_url)          │    │
│  │     → Fetches web evidence              │    │
│  │                                         │    │
│  │  2. gl.exec_prompt(analysis_task)       │    │
│  │     → AI evaluates claim vs evidence    │    │
│  │                                         │    │
│  │  3. gl.eq_principle_strict_eq()         │    │
│  │     → Validators reach consensus        │    │
│  └─────────────────────────────────────────┘    │
│                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │Validator │  │Validator │  │Validator │       │
│  │  LLM A   │  │  LLM B   │  │  LLM C   │       │
│  └──────────┘  └──────────┘  └──────────┘       │
└─────────────────────────────────────────────────┘
                       │
                       ▼
            ┌──────────────────┐
            │  On-Chain Verdict│
            │  TRUE / FALSE /  │
            │  UNVERIFIABLE    │
            └──────────────────┘
```

## ✨ Key Features

| Feature | GenLayer Function | Description |
|---------|------------------|-------------|
| 🌐 **Web Access** | `gl.get_webpage()` | Fetches real-time evidence from any URL |
| 🧠 **AI Reasoning** | `gl.exec_prompt()` | LLM-powered claim analysis |
| ⚖️ **Equivalence Principle** | `gl.eq_principle_strict_eq()` | Ensures validator consensus on verdicts |
| 🗳️ **Optimistic Democracy** | Native consensus | Multiple AI validators vote on outcomes |
| 📊 **Reputation System** | `TreeMap[Address, u256]` | Tracks claim submissions per address |

## 📋 Contract Interface

### Write Methods

#### `submit_claim(claim_id, claim_text, source_url)`
Submit a real-world claim for AI verification.

```python
# Example: Verify a news headline
submit_claim(
    claim_id="btc-100k-2026",
    claim_text="Bitcoin surpassed $100,000 in March 2026",
    source_url="https://www.coindesk.com/price/bitcoin/"
)
```

### Read Methods

#### `get_claim(claim_id) → str`
Retrieve a verified claim with its verdict, confidence score, and summary.

#### `get_all_claims() → dict`
Get all verified claims stored on the contract.

#### `get_reputation(address) → int`
Check how many claims an address has submitted.

## 🚀 Deployment Info

| Field | Value |
|-------|-------|
| **Network** | GenLayer Bradbury Testnet (Chain ID 4221) |
| **Contract Address** | `0x22F8D9A5FdB4f654c72411267E62FE1fEa7CeFbf` |
| **TX Hash** | `0x93f08b484075fb697c362dcfec3e2b5ebb4557b09b51e7d649d7e826f9ac21a7` |
| **Explorer** | [View on GenExplorer](https://explorer-bradbury.genlayer.com/address/0x22F8D9A5FdB4f654c72411267E62FE1fEa7CeFbf) |
| **RPC** | `https://rpc-bradbury.genlayer.com` |

## 🛠️ How to Deploy Your Own

### Prerequisites

```bash
npm install -g genlayer
```

### Steps

```bash
# 1. Set up the Bradbury Testnet
genlayer network set testnet-bradbury

# 2. Create an account
genlayer account create --name myaccount --password mypassword

# 3. Fund your wallet from the faucet
# Visit: https://testnet-faucet.genlayer.foundation/

# 4. Deploy the contract
genlayer deploy --contract contracts/ai_fact_checker.py
```

## 🏆 Hackathon Track

**Onchain Justice** — Decentralized arbitration with AI-evaluated evidence and fair dispute resolution.

This contract demonstrates how GenLayer's unique AI consensus can be used to build **decentralized truth verification systems** — a foundational primitive for:

- 🏛️ **Dispute resolution** — AI evaluates evidence fairly
- 📰 **News verification** — Combat misinformation on-chain
- 🔮 **Prediction markets** — Resolve outcomes using real-world data
- 🤖 **AI oracles** — Bridge off-chain truth to on-chain decisions

## 📄 License

MIT License — Built for the [GenLayer Testnet Bradbury Hackathon](https://dorahacks.io/hackathon/genlayer-bradbury)

---

<p align="center">
  Built with 🧠 by <a href="https://github.com/itsmeadamdamroma">itsmeadamdamroma</a> for the GenLayer ecosystem
</p>
