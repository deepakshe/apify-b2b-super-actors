# Apify B2B Super-Actors: 6 Enterprise Cloud Engines for Clay, n8n, Make & AI Agents

[![GitHub Stars](https://img.shields.io/github/stars/deepakshe/apify-b2b-super-actors?style=social)](https://github.com/deepakshe/apify-b2b-super-actors)
[![Apify Store](https://img.shields.io/badge/Apify%20Store-Portfolio%20Verified-blue?logo=apify)](https://apify.com/deepaksheoran172)
[![Glama MCP](https://img.shields.io/badge/Glama.ai-MCP%20Ready-black)](https://glama.ai/mcp/servers)
[![Smithery MCP](https://img.shields.io/badge/Smithery.ai-Indexed-orange)](https://smithery.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Enterprise-grade, serverless data pipelines designed for **high-converting B2B agencies**, **Clay outbound enrichment tables**, **n8n automated cron pipelines**, and **autonomous AI agents (Claude Desktop / Cursor IDE)**.

> **Stop paying $200–$500/month for rigid SaaS subscriptions.** Run pay-per-event micro-engines on Apify Cloud with **100% Fair-Billing (`charged=False` on failures)**, zero server maintenance, and sub-second synchronous API responses.

---

## 💰 The Cost-Anchoring Reality: Micro-Engines vs. Bloatware SaaS

| Capability / Workflow | Legacy SaaS Alternative | Legacy Cost | Our Apify Pay-Per-Event (PPE) Engine | PPE Cost |
|---|---|---|---|---|
| **E-Commerce Feed Normalization** | Matrixify / Salsify Enterprise | $200 – $500 / month | `catalog-feed-normalizer` | **$0.001 / run** |
| **Site Health & 404 Auditing** | Ahrefs / Screaming Frog | $199 – $499 / month | `website-health-checker` | **$0.001 / run** |
| **GovTech Tender Intelligence** | Tender247 / TendersInfo | ₹50,000 – ₹1.5L / year | `indian-public-tender-parser` | **$0.001 / run** |
| **AI Model Pricing & MCP Index** | Proprietary AI Gateways | $250 / month | `openrouter-mcp-registry` | **$0.001 / run** |
| **Store Migration & 301 Redirects** | Cart2Cart / LitExtension | $150 – $499 / migration | `store-catalog-redirect-extractor` | **$0.05 / run** |
| **Cybersecurity & DMARC Audits** | UpGuard / SecurityScorecard | $300 – $800 / month | `domain-security-super-auditor` | **$0.001 / domain** |

---

## 🛡️ The 100% Fair-Billing Guarantee (`charged=False`)

B2B technical buyers and agencies should never pay for dead runs, offline websites, or malformed inputs:
- If a target domain is unreachable or non-existent (`NXDOMAIN`), the run outputs `{"charged": false, "status": "UNREACHABLE"}`.
- If an input CSV or tender notice contains no extractable data, the job records detailed diagnostics with **`charged: false`**.
- You only pay for verified, normalized, production-grade output records.

---

## 🚀 The 6 Production Engines & 1-Click n8n Import URLs

Each workflow is pre-wired to Apify's synchronous execution endpoint (`https://api.apify.com/v2/acts/deepaksheoran172~<slug>/run-sync-get-dataset-items`).

| # | Engine | Slug | Apify Store Listing | 1-Click n8n Import Raw URL |
|---|---|---|---|---|
| **1** | **Shopify Catalog Feed Normalizer** | `catalog-feed-normalizer` | [View Store Page ➔](https://apify.com/deepaksheoran172/catalog-feed-normalizer) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool1_catalog_normalizer_n8n.json) |
| **2** | **Website Health & Broken Link Checker** | `website-health-checker` | [View Store Page ➔](https://apify.com/deepaksheoran172/website-health-checker) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool2_website_health_checker_n8n.json) |
| **3** | **India Public Tender & Procurement Parser** | `indian-public-tender-parser` | [View Store Page ➔](https://apify.com/deepaksheoran172/indian-public-tender-parser) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool3_tender_parser_n8n.json) |
| **4** | **OpenRouter Models & MCP Tool Registry** | `openrouter-mcp-registry` | [View Store Page ➔](https://apify.com/deepaksheoran172/openrouter-mcp-registry) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool4_openrouter_mcp_registry_n8n.json) |
| **5** | **Store Catalog & 301 Redirect Extractor** | `store-catalog-redirect-extractor` | [View Store Page ➔](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool5_store_redirect_extractor_n8n.json) |
| **6** | **Domain Security Super-Auditor** | `domain-security-super-auditor` | [View Store Page ➔](https://apify.com/deepaksheoran172/domain-security-super-auditor) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool6_domain_security_auditor_n8n.json) |

---

## ⚡ 1-Click Integration Ecosystem

### 1. Clay.com Outbound Enrichment Snippet
Enrich outbound sales tables in Clay with real domain security postures, SSL renewal deadlines, and DMARC deliverability metrics:
- **Method:** `POST`
- **URL:** `https://api.apify.com/v2/acts/deepaksheoran172~domain-security-super-auditor/run-sync-get-dataset-items?token={{apify_api_token}}`
- **Body:**
  ```json
  {
    "domains": ["{{company.domain}}"],
    "include_dns_deliverability": true,
    "include_rdap_age": true,
    "timeout_seconds": 10
  }
  ```
- **Clay Formula Extraction:** `{{data[0].letter_grade}}` (e.g. "A+", "D-") or `{{data[0].ssl_audit.days_until_expiry}}`.

### 2. n8n Automated Cron Pipelines
In n8n, click **Workflow > Import from URL**, paste any of the Raw URLs from the table above, set your `APIFY_API_TOKEN` environment variable, and run daily scheduled audits with zero code.

### 3. Claude Desktop & Cursor IDE (MCP Server)
Add the unified MCP bundle directly to `claude_desktop_config.json` or Cursor Settings:

```json
{
  "mcpServers": {
    "apify-b2b-suite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-fetch",
        "https://mcp.apify.com/?actors=deepaksheoran172/catalog-feed-normalizer,deepaksheoran172/website-health-checker,deepaksheoran172/indian-public-tender-parser,deepaksheoran172/openrouter-mcp-registry,deepaksheoran172/store-catalog-redirect-extractor,deepaksheoran172/domain-security-super-auditor"
      ]
    }
  }
}
```

---

## 📁 Repository Structure

```
.
├── README.md                          # SEO & Integration Master Guide
├── glama.json                         # Glama.ai MCP Crawler Manifest
├── smithery.yaml                      # Smithery.ai MCP Server Configuration
├── LICENSE                            # MIT License
├── workflows/                         # 6 Pre-wired n8n Automation Workflows
│   ├── tool1_catalog_normalizer_n8n.json
│   ├── tool2_website_health_checker_n8n.json
│   ├── tool3_tender_parser_n8n.json
│   ├── tool4_openrouter_mcp_registry_n8n.json
│   ├── tool5_store_redirect_extractor_n8n.json
│   └── tool6_domain_security_auditor_n8n.json
└── mcp/                               # Directory Submission Manifests
    └── mcp_directory_submission.json
```

---

## 📄 License

MIT © [Deepak Sheoran](https://apify.com/deepaksheoran172)
