# OpenRouter AI Models & MCP Schema Registry

[![Apify Store](https://img.shields.io/badge/Apify%20Store-Live%20Actor-blue?logo=apify)](https://apify.com/deepaksheoran172/openrouter-mcp-registry)
[![Price](https://img.shields.io/badge/Apify%20Rate-$0.01%20base%20+%20$0.001%2Fmodel-brightgreen)](https://apify.com/deepaksheoran172/openrouter-mcp-registry)

Synchronizes 200+ frontier AI models, live context window limits, prompt pricing, and verified Model Context Protocol (MCP) tool declarations for Cursor, Claude Desktop, and autonomous agents.

---

## 💰 ROI Price Anchoring & Cost Comparison

| Solution Tier | Cost Structure | Model Coverage | MCP Tool Support |
|---|---|---|---|
| **Proprietary AI Gateway** | **$150.00–$250.00 / month** | Limited to single vendor | No native MCP sync |
| **Apify Pay-Per-Event (PPE)** | **$0.01 base + $0.001 / model** *(~$0.21 / run)* | 200+ frontier models | Full JSON schema export |
| **⚡ Net Savings** | **Save 99.8%** vs Gateway | **200+ Frontier Models** | **Claude & Cursor Native** |

> 🚨 **The Gateway Killer:** Sync 200+ AI models and verified MCP declarations for ~$0.21 on Apify Cloud instead of maintaining proprietary gateway pipelines.

---

## 🔍 10-Row Empirical CSV Teaser Proof

| Row | Model ID | Context Window | Prompt Price / 1M | Completion Price / 1M | MCP Schema Status |
|---|---|---|---|---|---|
| 1 | `anthropic/claude-3.5-sonnet` | 200,000 | $3.00 | $15.00 | `VERIFIED` |
| 2 | `openai/gpt-4o-2024-08-06` | 128,000 | $2.50 | $10.00 | `VERIFIED` |
| 3 | `google/gemini-pro-1.5` | 2,000,000 | $1.25 | $5.00 | `VERIFIED` |
| 4 | `deepseek/deepseek-coder` | 128,000 | $0.14 | $0.28 | `VERIFIED` |
| 5 | `meta-llama/llama-3.1-405b` | 128,000 | $2.00 | $2.00 | `VERIFIED` |
| 6 | `mistralai/mistral-large` | 128,000 | $2.00 | $6.00 | `VERIFIED` |
| 7 | `qwen/qwen-2.5-72b-instruct` | 32,768 | $0.35 | $0.40 | `VERIFIED` |
| 8 | `cohere/command-r-plus` | 128,000 | $2.50 | $10.00 | `VERIFIED` |
| 9 | `google/gemini-flash-1.5` | 1,000,000 | $0.075 | $0.30 | `VERIFIED` |
| **10** | *`+ 190 more frontier models...`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[Run on Apify to Unlock]`* |

---

## 🚀 Quickstart via Apify API

```bash
curl -X POST "https://api.apify.com/v2/acts/deepaksheoran172~openrouter-mcp-registry/run-sync-get-dataset-items" \
  -H "Content-Type: application/json" \
  -d '{"include_mcp_declarations": true}'
```
