# LLM depth track (runs beside the security track)

**Time:** about 5 hours a week from Week 7. Security track keeps the other 35.
**Rule:** every course must produce a repo artifact. No artifact, no course.
**Check each course is still free before starting. Offers change.**

| Order | Resource | Artifact to ship |
|---|---|---|
| 1 | Anthropic Academy: Building with the Claude API, tool use, MCP | `claude-tool-agent`: an agent with 2 tools and logged calls |
| 2 | anthropics/courses (GitHub), prompt evaluation material | `eval-suite`: scores outputs before and after prompt changes |
| 3 | DeepLearning.AI short courses: RAG, agents, any LLM red teaming course | `rag-lab`: RAG app with a deliberately injectable document |
| 4 | Hugging Face LLM course; Karpathy "Neural Networks: Zero to Hero" | `notes/llm-internals.md`: tokens, attention, sampling in your own words |
| 5 | Optional: Google Cloud Skills Boost generative AI path | Only for cloud focused roles |

## Reading (one summary file per item, in your own words)
- OWASP Top 10 for LLM Applications
- MITRE ATLAS
- NIST AI Risk Management Framework
- 3 published papers or posts on prompt injection and agent attacks

## Skip
Shallow introductions (for example "AI Essentials" style courses). They add a badge, not skill.

## Test
Monthly: explain from memory how a tool calling agent works and where untrusted text enters. Logged in `tests/`.
