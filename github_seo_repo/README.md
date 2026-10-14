# B2B Automation & Data Infrastructure Suite: 6 Cloud Engines for Clay, n8n, Make & AI Agents

[![GitHub Stars](https://img.shields.io/github/stars/deepaksheoran172/apify-b2b-automation-suite?style=social)](https://github.com/deepaksheoran172)
[![Apify Store](https://img.shields.io/badge/Apify%20Store-Portfolio%20Verified-blue?logo=apify)](https://apify.com/deepaksheoran172)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MCP Ready](https://img.shields.io/badge/Model%20Context%20Protocol-Compatible-purple)](https://mcp.apify.com/?tools=deepaksheoran172/catalog-feed-normalizer,deepaksheoran172/website-health-checker,deepaksheoran172/indian-public-tender-parser,deepaksheoran172/openrouter-mcp-registry,deepaksheoran172/store-catalog-redirect-extractor,deepaksheoran172/domain-security-super-auditor)

Serverless data micro-engines designed for **B2B outbound operations**, **Clay enrichment tables**, **n8n automated cron pipelines**, and **autonomous AI agents (Claude Desktop / Cursor IDE)**.

> **Replace rigid SaaS monthly retainers with Pay-Per-Event cloud execution.** Run pay-per-event micro-engines on Apify Cloud with transparent usage-based billing, zero infrastructure maintenance, and direct REST/dataset API integration.

---

## 🚀 The 6 Production Engines

| # | Engine & Slug | High-Intent Keyword Target | Apify Store Link | n8n Workflow |
|---|---|---|---|---|
| **1** | **Shopify Catalog Feed Normalizer**<br/>`catalog-feed-normalizer` | `dropship-catalog-normalizer`, `shopify-csv-validator` | [View Actor ➔](https://apify.com/deepaksheoran172/catalog-feed-normalizer) | [`tool1_catalog_normalizer_n8n.json`](../n8n_automated_bundle/tool1_catalog_normalizer_n8n.json) |
| **2** | **Website Health & Broken Link Checker**<br/>`website-health-checker` | `broken-link-auditor`, `ssrf-protected-crawler` | [View Actor ➔](https://apify.com/deepaksheoran172/website-health-checker) | [`tool2_website_health_checker_n8n.json`](../n8n_automated_bundle/tool2_website_health_checker_n8n.json) |
| **3** | **India Public Tender & Procurement Parser**<br/>`indian-public-tender-parser` | `indian-tender-parser`, `gem-cppp-procurement` | [View Actor ➔](https://apify.com/deepaksheoran172/indian-public-tender-parser) | [`tool3_tender_parser_n8n.json`](../n8n_automated_bundle/tool3_tender_parser_n8n.json) |
| **4** | **OpenRouter Models & MCP Tool Registry**<br/>`openrouter-mcp-registry` | `openrouter-mcp`, `ai-model-pricing-index` | [View Actor ➔](https://apify.com/deepaksheoran172/openrouter-mcp-registry) | [`tool4_openrouter_mcp_registry_n8n.json`](../n8n_automated_bundle/tool4_openrouter_mcp_registry_n8n.json) |
| **5** | **Store Catalog & 301 Redirect Extractor**<br/>`store-catalog-redirect-extractor` | `woocommerce-migration`, `shopify-301-redirect-map` | [View Actor ➔](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor) | [`tool5_store_redirect_extractor_n8n.json`](../n8n_automated_bundle/tool5_store_redirect_extractor_n8n.json) |
| **6** | **Domain Security Super-Auditor**<br/>`domain-security-super-auditor` | `enterprise-ssl-audit`, `clay-enrichment`, `dmarc-scorecard` | [View Actor ➔](https://apify.com/deepaksheoran172/domain-security-super-auditor) | [`tool6_domain_security_auditor_n8n.json`](../n8n_automated_bundle/tool6_domain_security_auditor_n8n.json) |

---

## ⚡ Quickstart: 3-Click Integration Ecosystem

### 1. Clay.com Outbound Enrichment
Enrich your account lists with security audit metrics, SSL expiration signals, or e-commerce migration opportunities:
- **Action:** HTTP API Request
- **Method:** `POST`
- **URL:** `https://api.apify.com/v2/acts/deepaksheoran172~<ACTOR_SLUG>/run-sync-get-dataset-items?token={{apify_api_token}}`
- **Output:** Synchronous array of normalized records.

### 2. n8n Automated Cron Pipelines
All workflows in `n8n_automated_bundle/` include:
- Scheduled cron triggers (configurable daily/weekly intervals).
- Webhook trigger endpoints for on-demand execution.
- Direct sync calls to Apify's `run-sync-get-dataset-items` API.

**Importing an n8n workflow:**
1. Open your n8n workspace.
2. Click **Workflow > Import from File**.
3. Select any `.json` from `n8n_automated_bundle/`.
4. Add your `APIFY_API_TOKEN` environment variable and activate.

### 3. Model Context Protocol (MCP) for Claude Desktop & Cursor
Connect to Apify's official remote MCP endpoint (`mcp.apify.com`) using Streamable HTTP:

#### Native Remote HTTP Configuration (Recommended)
```json
{
  "mcpServers": {
    "apify-b2b-suite": {
      "url": "https://mcp.apify.com?tools=deepaksheoran172/catalog-feed-normalizer,deepaksheoran172/website-health-checker,deepaksheoran172/indian-public-tender-parser,deepaksheoran172/openrouter-mcp-registry,deepaksheoran172/store-catalog-redirect-extractor,deepaksheoran172/domain-security-super-auditor",
      "headers": {
        "Authorization": "Bearer YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

#### Command Bridge via `mcp-remote`
```json
{
  "mcpServers": {
    "apify-b2b-suite": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com?tools=deepaksheoran172/catalog-feed-normalizer,deepaksheoran172/website-health-checker,deepaksheoran172/indian-public-tender-parser,deepaksheoran172/openrouter-mcp-registry,deepaksheoran172/store-catalog-redirect-extractor,deepaksheoran172/domain-security-super-auditor"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

---

## 🛡️ Transparent Pay-Per-Event (PPE) Billing Model

These micro-engines operate under Apify's Pay-Per-Event (PPE) model:
- **Granular Event Billing:** Pay only for items processed and operations performed.
- **Error Isolation:** In `domain-security-super-auditor`, unresolvable domains (`NXDOMAIN`) output diagnostics and isolate errors without charging for deep enrichment stages.

---

## 📁 Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── apify_heartbeat.yml        # Weekly Cost-Free Metadata Check & Opt-In Test
├── README.md                          # SEO & Integration Master Guide
├── LICENSE                            # MIT License
├── workflows/                         # n8n Automation templates
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
