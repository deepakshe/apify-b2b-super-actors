# Apify B2B Super-Actors: 7 Enterprise Cloud Engines for Clay, n8n, Make & AI Agents

[![GitHub Stars](https://img.shields.io/github/stars/deepakshe/apify-b2b-super-actors?style=social)](https://github.com/deepakshe/apify-b2b-super-actors)
[![Live Benchmark](https://img.shields.io/badge/Live%20Benchmark-7%2F7%20Online-brightgreen)](LIVE_BENCHMARK_STATUS.md)
[![Apify Store](https://img.shields.io/badge/Apify%20Store-Portfolio%20Verified-blue?logo=apify)](https://apify.com/deepaksheoran172)
[![RapidAPI Specs](https://img.shields.io/badge/RapidAPI-OpenAPI%203.0%20Ready-purple)](marketplace_syndication/)
[![Glama MCP](https://img.shields.io/badge/Glama.ai-Manifest%20Configured-black)](https://glama.ai/mcp)
[![Smithery MCP](https://img.shields.io/badge/Smithery.ai-Compatible-orange)](https://smithery.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Serverless data micro-engines designed for **B2B outbound operations**, **Clay enrichment tables**, **n8n automated cron pipelines**, and **autonomous AI agents (Claude Desktop / Cursor IDE)**.

> **Replace rigid SaaS monthly retainers with Pay-Per-Event cloud execution.** Run pay-per-event micro-engines on Apify Cloud with transparent usage-based billing, zero infrastructure maintenance, and direct REST/dataset API integration.

---

## 💰 High-Converting ROI Price Anchoring & Cost Model

| Capability / Workflow | Manual Agency / Legacy SaaS Cost | Verified Live Apify PPE Rate | Effective Value & Savings | 10-Row Empirical Teaser Proof |
|---|---|---|---|---|
| **Store Migration & 301 Redirects** | $250.00 / migration | **$0.05 base + $0.001 / item** | **Save 99.6%** vs Manual Agency | [`store-catalog-redirect-extractor`](docs/actors/store-catalog-redirect-extractor.md) |
| **Cybersecurity & DMARC Audits** | $180.00 / audit | **$0.001 / domain** ($1.00 / 1k) | **Save 99.4%** vs Consultant | [`domain-security-super-auditor`](docs/actors/domain-security-super-auditor.md) |
| **E-Commerce Feed Normalization** | $200.00 / cleanup | **$0.05 base + $0.0005 / item** | **Save 99.7%** vs Contractor | [`catalog-feed-normalizer`](docs/actors/catalog-feed-normalizer.md) |
| **Site Health & 404 Auditing** | $199.00 / mo SaaS | **$0.001 / page** ($1.00 / 1k) | **Save 99.5%** vs Monthly Retainer | [`website-health-checker`](docs/actors/website-health-checker.md) |
| **GovTech Tender Intelligence** | ₹50,000 / yr portal | **$0.02 base + $0.005 / record** | **Save 99.0%** vs Annual Contract | [`indian-public-tender-parser`](docs/actors/indian-public-tender-parser.md) |
| **AI Model Pricing & MCP Index** | $150.00 / gateway setup | **$0.01 base + $0.001 / model** | **Save 99.8%** vs Gateway Ops | [`openrouter-mcp-registry`](docs/actors/openrouter-mcp-registry.md) |
| **Domain Protocol & App Links** | $160.00 / audit | **$0.001 / domain** ($1.00 / 1k) | **Save 99.4%** vs Manual QA | [`domain-protocol-signals-enricher`](docs/actors/domain-protocol-signals-enricher.md) |

> ⚡ **The 99% SaaS-Replacement Law:** Run production datasets on demand with transparent micro-cent Pay-Per-Event billing. Download a free 10-row teaser CSV before running production batches.

---

## 🛡️ Transparent Pay-Per-Event (PPE) Billing Model

These micro-engines operate under Apify's Pay-Per-Event (PPE) model:
- **Custom Event Charges vs. Platform Usage Costs:**
  - **Custom Event Charges:** Billed per successful audit event defined and charged by the Actor (`ssl-tls-base-audit` at **$0.001 / audit**; optional `security-headers-dns-enrichment` at **$0.001 / enrichment** when `include_dns_deliverability: true` is enabled).
  - **Platform Usage Costs:** Platform compute and memory consumption are distinct from Actor event fees. Depending on the current Apify Actor monetization configuration, platform usage costs may either be covered by the Actor publisher or transferred to the user; buyers should not assume platform usage is always charged separately.
- **Error Isolation (Verified Failure Paths):** In `domain-security-super-auditor`, custom event charges (`Actor.charge`) are bypassed (`charged: false`, `events_charged: []`) specifically for input validation errors (`INVALID_DOMAIN_FORMAT`), unresolvable hostnames (`DNS_NXDOMAIN` or missing A/AAAA records), anti-SSRF private IP blocks, or overall audit execution timeouts. If a domain successfully resolves to a public IP but encounters web server or port 443 connection failures, the Actor completes the evaluation with a failing grade and assesses the base audit event charge.
- **Technical DNS Auditing (No Inbox Guarantees):** Email authentication checks inspect technical DNS records against RFC specifications (RFC 7208 / RFC 7489) and provider thresholds (Google/Yahoo 2024+ sender guidelines). Because inbox placement depends on IP reputation, domain history, sending volume, and content, this engine evaluates DNS configuration alignment rather than guaranteeing deliverability outcomes.
- **Predictable Scaling:** Workflows in Clay or n8n can process thousands of records with predictable micro-cent event charges.

---

## 🚀 The 7 Production Engines & 1-Click n8n Import URLs

Each workflow is pre-wired to Apify's synchronous execution endpoint (`https://api.apify.com/v2/acts/deepaksheoran172~<slug>/run-sync-get-dataset-items`).

| # | Engine | Slug | Apify Store & 1-Click Browser Tasks | 1-Click n8n Import Raw URL |
|---|---|---|---|---|
| **1** | **Shopify Catalog Feed Normalizer** | `catalog-feed-normalizer` | [View Store Page ➔](https://apify.com/deepaksheoran172/catalog-feed-normalizer)<br>• [Task: Normalize Supplier CSV](https://apify.com/deepaksheoran172/catalog-feed-normalizer/examples/normalize-supplier-csv-shopify)<br>• [Task: Validate Product CSV](https://apify.com/deepaksheoran172/catalog-feed-normalizer/examples/validate-product-csv-shopify) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool1_catalog_normalizer_n8n.json) |
| **2** | **Website Health & Broken Link Checker** | `website-health-checker` | [View Store Page ➔](https://apify.com/deepaksheoran172/website-health-checker)<br>• [Task: Check Website & Links](https://apify.com/deepaksheoran172/website-health-checker/examples/check-website-status-and-broken-links)<br>• [Task: Technical SEO Signals](https://apify.com/deepaksheoran172/website-health-checker/examples/review-technical-seo-page-signals) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool2_website_health_checker_n8n.json) |
| **3** | **India Public Tender & Procurement Parser** | `indian-public-tender-parser` | [View Store Page ➔](https://apify.com/deepaksheoran172/indian-public-tender-parser)<br>• [Task: Structure Public Notice](https://apify.com/deepaksheoran172/indian-public-tender-parser/examples/structure-indian-public-tender-notice)<br>• [Task: Review Deadlines & EMD](https://apify.com/deepaksheoran172/indian-public-tender-parser/examples/review-tender-deadlines-and-emd) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool3_tender_parser_n8n.json) |
| **4** | **OpenRouter Models & MCP Tool Registry** | `openrouter-mcp-registry` | [View Store Page ➔](https://apify.com/deepaksheoran172/openrouter-mcp-registry)<br>• [Task: Compare Model Pricing](https://apify.com/deepaksheoran172/openrouter-mcp-registry/examples/compare-openrouter-model-pricing)<br>• [Task: Discover MCP Servers](https://apify.com/deepaksheoran172/openrouter-mcp-registry/examples/discover-mcp-server-registry-records) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool4_openrouter_mcp_registry_n8n.json) |
| **5** | **Store Catalog & 301 Redirect Extractor** | `store-catalog-redirect-extractor` | [View Store Page ➔](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor)<br>• [Task: Catalog Migration QA](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor/examples/extract-store-catalog-for-migration-qa)<br>• [Task: 301 Redirect Records](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor/examples/prepare-redirect-records-for-migration-review) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool5_store_redirect_extractor_n8n.json) |
| **6** | **Domain Security Super-Auditor** | `domain-security-super-auditor` | [View Store Page ➔](https://apify.com/deepaksheoran172/domain-security-super-auditor)<br>• [Task: Audit TLS & DNS Signals](https://apify.com/deepaksheoran172/domain-security-super-auditor/examples/audit-domain-tls-and-dns-signals)<br>• [Task: Email Auth & DMARC](https://apify.com/deepaksheoran172/domain-security-super-auditor/examples/review-domain-email-authentication) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool6_domain_security_auditor_n8n.json) |
| **7** | **Domain Protocol & App Link Signals Enricher** | `domain-protocol-signals-enricher` | [View Store Page ➔](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher)<br>• [Task: Domain Protocol Signals](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher/examples/collect-public-domain-protocol-signals)<br>• [Task: Well-Known Domain Files](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher/examples/inspect-well-known-domain-files) | [Raw n8n JSON](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool7_domain_protocol_enricher_n8n.json) |

> 📘 **Detailed Buyer Workflows:** For full outcome-based integration guides across all 14 task pages, see the [Enterprise B2B Workflow Catalog](docs/WORKFLOW_CATALOG.md).


---

## ⚡ Integration Ecosystem

### 1. Clay.com Outbound Enrichment Snippet
Enrich outbound sales tables in Clay with domain security posture, SSL renewal deadlines, and technical DNS authentication records:
- **Action:** HTTP API Request
- **Method:** `POST`
- **URL:** `https://api.apify.com/v2/acts/deepaksheoran172~domain-security-super-auditor/run-sync-get-dataset-items`
- **Security & Authentication:** Recommend configuring the `Authorization` header securely via Clay's workspace-level HTTP API (Headers) account (`Bearer YOUR_APIFY_TOKEN`). Keep tokens strictly out of query strings and request bodies.
- **Headers:**
  - `Content-Type: application/json`
  - `Authorization: Bearer {{apify_api_token}}`
- **Body:**
  ```json
  {
    "domains": ["{{company.domain}}"],
    "include_dns_deliverability": true,
    "include_rdap_age": true,
    "timeout_seconds": 10
  }
  ```
- **Clay Formula Extractions (Verified Schema):**
  - Composite Letter Grade: `{{data[0].letter_grade}}` (e.g. `"A+"`, `"B"`, `"F"`)
  - Overall Numeric Score: `{{data[0].overall_score}}` (0–100 integer)
  - Days Until SSL Expiry: `{{data[0].ssl_audit.days_until_expiry}}`
  - DMARC Policy Status: `{{data[0].email_deliverability_audit.dmarc_policy}}` (e.g. `"reject"`, `"quarantine"`, `"none"`, `"missing"`)
  - SPF Policy Status: `{{data[0].email_deliverability_audit.spf_policy}}` (e.g. `"hardfail (-all)"`, `"softfail (~all)"`, `"dangerous (+all)"`, `"neutral (?all)"`, `"missing"`)
  - Mail Provider: `{{data[0].email_deliverability_audit.mx_provider}}` (e.g. `"Google Workspace"`, `"Microsoft 365"`)

### 2. n8n Automated Cron Pipelines
In n8n, click **Workflow > Import from URL**, paste any of the Raw URLs from the table above, set your `APIFY_API_TOKEN` environment variable, and run daily scheduled audits with zero code.

### 3. Claude Desktop & Cursor IDE (MCP Integration)
Connect to Apify's official remote MCP endpoint (`mcp.apify.com`) using Streamable HTTP:

#### Native Remote HTTP Configuration (Recommended for Cursor & Claude Desktop)
Add to your client configuration:
```json
{
  "mcpServers": {
    "apify-b2b-suite": {
      "url": "https://mcp.apify.com?tools=deepaksheoran172/catalog-feed-normalizer,deepaksheoran172/website-health-checker,deepaksheoran172/indian-public-tender-parser,deepaksheoran172/openrouter-mcp-registry,deepaksheoran172/store-catalog-redirect-extractor,deepaksheoran172/domain-security-super-auditor,deepaksheoran172/domain-protocol-signals-enricher",
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
        "https://mcp.apify.com?tools=deepaksheoran172/catalog-feed-normalizer,deepaksheoran172/website-health-checker,deepaksheoran172/indian-public-tender-parser,deepaksheoran172/openrouter-mcp-registry,deepaksheoran172/store-catalog-redirect-extractor,deepaksheoran172/domain-security-super-auditor,deepaksheoran172/domain-protocol-signals-enricher"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

---

## 📁 Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── apify_heartbeat.yml        # Weekly Cost-Free Metadata Check & Opt-In Test
├── README.md                          # Integration & Architecture Guide
├── glama.json                         # Glama.ai MCP Server Verification Manifest
├── smithery.yaml                      # Smithery.ai Remote HTTP MCP Configuration
├── LICENSE                            # MIT License
├── workflows/                         # 7 Pre-wired n8n Automation Workflows
│   ├── tool1_catalog_normalizer_n8n.json
│   ├── tool2_website_health_checker_n8n.json
│   ├── tool3_tender_parser_n8n.json
│   ├── tool4_openrouter_mcp_registry_n8n.json
│   ├── tool5_store_redirect_extractor_n8n.json
│   ├── tool6_domain_security_auditor_n8n.json
│   └── tool7_domain_protocol_enricher_n8n.json
└── mcp/                               # Directory Submission Manifests
    └── mcp_directory_submission.json
```

---

## 📄 License

MIT © [Deepak Sheoran](https://apify.com/deepaksheoran172)
