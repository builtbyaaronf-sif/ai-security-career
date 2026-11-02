# Crypto bug bounty track (optional, decision at Week 22)

**Status:** exploration. Skill evidence first, income second. No plan depends on bounty money.

## Why it fits, and where it does not
- Web and API parts of crypto programs (exchanges, wallets, dashboards) use Stage A skills directly.
- Smart contract bounties need Solidity, EVM knowledge and DeFi patterns. Estimate: 150 to 250 hours before a realistic first submission.
- Competition is high. Many beginners earn nothing for a long time.

## Platforms (verify current status before using)
| Platform | Notes |
|---|---|
| HackenProof | Smart contracts, web and API. Beginner friendly start |
| Immunefi | Largest. KYC may be required after a valid report. Scope set per program |
| Hats Finance | On-chain vaults |
| Sherlock, Cantina | Audit contests and curated bounties |
| Code4rena | Reported as winding down. Check |
| HackerOne, Bugcrowd | Some exchange and wallet programs. Check |

## Schedule
| When | Step |
|---|---|
| Weeks 13 to 22 | Optional: Chainlink "Smart Contract Security and Auditing 101" (about 1 hour) |
| Week 22 | Checkpoint: are web and API skills solid? Try one web or API program on HackenProof. Read Immunefi's rules |
| Stage B | Solidity basics, Cyfrin Updraft security course, Ethernaut, Damn Vulnerable DeFi. Tools: Slither, Foundry |
| After | Audit contests, then real bounties |

## Rust (decision after Solidity, not before)
- Used for Solana programs (often with Anchor) and some other chains. Ethereum contracts use Solidity.
- Estimate: 80 to 120 hours for basics. Bug classes differ by chain (for example Solana signer and account ownership checks).
- Do not learn Solidity and Rust at the same time.
- Order: Python, then Solidity, then Rust only if the programs I want to target use it.
- Free resources when the time comes: The Rust Programming Language (official book) and Rustlings.

## Rules
1. Test only what a program lists as in scope. Follow its rules.
2. Never test on mainnet. Use local forks or testnets.
3. Never share a seed phrase or private key. Separate browser profile and a wallet with tiny funds.
4. Ignore "recruiters" and bounty offers by DM. Do not run unknown scripts.
5. Keep records for UK tax. KYC and USDC payouts are common.
6. Every submission gets a sanitised case study in `case-studies/` after disclosure is complete.
