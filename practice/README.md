# Practice system: scenarios and mock exams

Two kinds of practice, both scored and logged.

## 1. Scenario drills (tabletop incident exercises)
Realistic incidents of the kind AI security and blue team staff face. 45 minute time box, closed book after the first read.
**Format:** read the brief and evidence, then write a one page response covering triage, containment, investigation, fix, detection and reporting. Save it in `responses/` and commit it.
**Marking:** I mark each response against a rubric (accuracy, order of actions, evidence preserved, least privilege, clarity). I keep the marking guide out of the repo so the exercise stays a test.

| Drill | Scenario | Skills | Start |
|---|---|---|---|
| S01 | Leaked API key in a public repo | Secrets, containment, rotation | Week 6 |
| S02 | AI support assistant obeys hidden text in tickets (indirect prompt injection) | LLM01, excessive agency, detection | Week 10 |
| S03 | Stolen LLM API key runs up a large bill (denial of wallet) | Cost abuse, rate limits, alerting | Week 12 |
| S04 | Phishing leads to MFA fatigue login | Identity attacks, triage | Week 14 |
| S05 | RAG assistant leaks another customer's document | Access control on retrieval | Week 16 |
| S06 | Staff paste confidential data into a public chatbot | Shadow AI, data loss, policy | Week 18 |
| S07 | Compromised package in an AI app dependency | Supply chain | Week 20 |
| S08 | Ransomware on small business laptops | Classic incident response | Week 22 |
| S09 | Deepfake voice call requests an urgent payment | Social engineering with AI | Week 24 |
| S10 | Researcher reports a guardrail bypass | Disclosure handling | Week 26 |

Cadence: one drill every two weeks, then weekly from Week 20.

## 2. Mock exams

| Cert | When | Method | Book the real exam when |
|---|---|---|---|
| **Security+** | Quick 10 question checks every Monday from Week 8. Full length mocks in Weeks 16, 18 and 20 | My original questions, plus an official or reputable paid practice set | Two full mocks in a row at 85% or better |
| **Blue team cert** (BTL1 or CySA+) | From about Week 26 | CySA+: mock exams. BTL1: hands on lab exercises in place of a mock | Labs done without hints, and mocks at 85% |
| **BSCP** (optional) | If chosen | PortSwigger practice labs and their practice exam | Practice exam passed within the time limit |

Rules: closed book, timed, same time of day as the real exam. Every wrong answer becomes a line in `tests/weak-spots.md` and returns in the next three quizzes.

## Logs
`mocks/log.md` holds every score. A rising trend matters more than any single result.
