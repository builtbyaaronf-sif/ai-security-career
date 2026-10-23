# Roadmap: 48 weeks, 6 phases

Each phase ends with a **gate** (written test + practical). Pass at 80% or repeat the weak areas for a week.

## Phase 1: Foundations (Weeks 1 to 6)
**Goal:** write Python and use Linux, Git and HTTP without help.

| Skill | Free resource |
|---|---|
| Python | *Automate the Boring Stuff* (free online), CS50P (Harvard, free) |
| Linux + terminal | OverTheWire **Bandit** (levels 0 to 20) |
| Git + GitHub | GitHub Skills (free interactive courses) |
| Networking + HTTP | Professor Messer Network+ videos, MDN HTTP docs |
| Security baseline cert | Decide later. ISC2 CC is no longer free (programme closed 20 May 2026). See the cert plan below |

**Ship:** `python-security-scripts` repo (port scanner, log parser, HTTP header checker).
**Gate 1:** Bandit level 20, CS50P problem sets done, quiz 80%+.

## Phase 2: Web and API security (Weeks 7 to 14)
**Goal:** find and fix real web vulnerabilities. This is what AI apps are built on.

| Skill | Free resource |
|---|---|
| Web vulns (SQLi, XSS, SSRF, auth, access control) | **PortSwigger Web Security Academy** (free, best in class) |
| API security | OWASP API Security Top 10, APIsec University (free) |
| Threat modelling | OWASP Threat Dragon, STRIDE |
| Cloud basics | AWS Skill Builder free tier, AWS Cloud Practitioner Essentials |

**Ship:** 15+ PortSwigger labs written up. A STRIDE threat model of FORGE's payment and intake flow (see `EVIDENCE.md`). Burp Suite Certified Practitioner (BSCP) exam booked.
**Gate 2:** 3 unseen PortSwigger labs solved unaided in 3 hours.

## Phase 3: How LLM systems work (Weeks 15 to 20)
**Goal:** build what you will later attack.

| Skill | Free resource |
|---|---|
| LLM APIs, tool use, agents | Anthropic courses (github.com/anthropics/courses), DeepLearning.AI short courses |
| RAG + embeddings | DeepLearning.AI RAG courses, ChromaDB docs |
| Evals | Anthropic eval docs, promptfoo docs |

**Ship:** a small RAG app *with an eval suite* that scores accuracy before and after prompt changes.
**Gate 3:** explain end to end how a tool calling agent decides to call a tool, and where untrusted text enters.

## Phase 4: AI security core (Weeks 21 to 30)
**Goal:** attack and defend LLM systems with industry frameworks.

| Skill | Free resource |
|---|---|
| Frameworks | OWASP Top 10 for LLM Apps (2025), OWASP Agentic AI threats, MITRE ATLAS, NIST AI RMF |
| Prompt injection (direct + indirect) | Lakera **Gandalf** (all levels), PortSwigger **Web LLM attacks** labs |
| Red teaming tools | **garak** (NVIDIA), **PyRIT** (Microsoft), **promptfoo** red team |
| Red teaming method | Microsoft AI Red Team 101 (free), Anthropic and OpenAI published red team writeups |
| Guardrails | Llama Guard, NeMo Guardrails |

**Ship:** Project #1 **LLM Input Sanitiser Gateway** with a garak/promptfoo eval showing attack success rate before and after. Project #2 **indirect prompt injection research on agents that read web pages** (FORGE's SCOUT is the real world case). 2 min demo video.
**Gate 4:** red team an unseen toy agent in 4 hours, deliver a findings report mapped to OWASP LLM IDs.

## Phase 5: Public proof (Weeks 31 to 40)
**Goal:** third party validated evidence.

- Bug bounty: **huntr.com** (AI/ML open source bounties), vendor AI bug bounty programs. Target: 1 valid report.
- Competitions: HackAPrompt, AI Village CTF (DEF CON), Kaggle security comps when live.
- Open source: 3 merged PRs into garak, PyRIT, promptfoo or an OWASP GenAI project.
- Writing: 1 technical blog post every 2 weeks.
- Optional paid cert once evidence exists: HTB AI Red Teamer path, or OffSec / SANS later via employer.

**Gate 5:** 1 external validation (bounty, CVE, merged PR, or CTF placing).

## Phase 6: Job hunt (Weeks 41 to 48, overlap from Week 30)
- CV and LinkedIn rewritten from `EVIDENCE.md`.
- 10 tailored applications a week. Targets: AI labs, AI security startups (Lakera, Protect AI, HiddenLayer, Prompt Security type companies), and AppSec roles at AI-heavy companies (the realistic first door).
- Monthly mock interviews from week 30: system design for a secure agent, live threat model, code review.

**Gate 6:** an offer.

## Certification plan (revised 23 Oct 2026)
| When | Cert | Notes |
|---|---|---|
| Weeks 7 to 14 | PortSwigger lab progress (free) | Public profile, hard to fake |
| About week 14 | Burp Suite Certified Practitioner | Practical exam, about $99. Check price |
| About week 24 | CompTIA Security+ | Common HR filter. Roughly $400. Check price and vouchers |
| Optional | ISC2 CC | Free programme ended 20 May 2026. Only if discounted or you hold an unexpired voucher |
| Phase 5 | Hands on AI red teaming credential | Verify current options first |

## Honest expectations
- 12 months at 40 hrs/week is realistic for a **junior to mid AI security / AppSec role**. "High paying" senior roles typically come 1 to 2 years after that, on top of this evidence.
- The adjacent door (AppSec engineer, security analyst at an AI company) is the most likely first hire. Plan for it.
