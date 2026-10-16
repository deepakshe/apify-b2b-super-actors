# 🚀 Enterprise B2B Workflow Catalog & Task Directory
> **Verified Apify Super-Actors & 1-Click Browser Blueprints**  
> *Zero External Heavy Dependencies · Pure Standard Library Execution · RFC-4180 Standards · 100% Deterministic*

This directory indexes all 7 production Apify Actors and their 14 pre-configured public Task Pages. Each task allows instant evaluation directly in your web browser with synthetic data before integrating into automated production pipelines.

---

## 📑 Quick Navigation by Business Outcome

1. [Shopify & E-Commerce Catalog Ingestion](#1-shopify--e-commerce-catalog-ingestion)
2. [Replatforming, Migrations & 301 Redirect QA](#2-replatforming-migrations--301-redirect-qa)
3. [Technical SEO, Crawlability & Health Auditing](#3-technical-seo-crawlability--health-auditing)
4. [Domain Security, Deliverability & Protocol Telemetry](#4-domain-security-deliverability--protocol-telemetry)
5. [Public Procurement Intelligence & Indian Tender Normalization](#5-public-procurement-intelligence--indian-tender-normalization)
6. [AI Infrastructure, MCP Server Registry & Token Pricing](#6-ai-infrastructure-mcp-server-registry--token-pricing)

---

## 1. Shopify & E-Commerce Catalog Ingestion

### [Catalog Feed Normalizer](https://apify.com/deepaksheoran172/catalog-feed-normalizer)
*Sanitizes multi-vendor CSV/JSON product feeds into 32-column Shopify-compliant CSV format with formula injection protection.*

* **Task 1: [Normalize Supplier CSV for Shopify Import](https://apify.com/deepaksheoran172/catalog-feed-normalizer/examples/normalize-supplier-csv-shopify)**
  * **Use Case:** Converts raw supplier feeds with German/European number formats (`1.499,00 €`), messy option variants, and unescaped quotes into ready-to-import Shopify files.
* **Task 2: [Validate Product CSV Before Shopify Import](https://apify.com/deepaksheoran172/catalog-feed-normalizer/examples/validate-product-csv-shopify)**
  * **Use Case:** Scans dirty product feeds, catches missing titles/prices, and quarantines invalid rows into an audit report without breaking the bulk upload.
* **Integration Assets:**
  * [n8n Automation Template](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool1_catalog_normalizer_n8n.json)
  * [Full Workflow Guide](https://github.com/deepakshe/apify-b2b-super-actors/blob/main/docs/SHOPIFY_CATALOG_WORKFLOW_GUIDE.md)

---

## 2. Replatforming, Migrations & 301 Redirect QA

### [Store Catalog Redirect Extractor](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor)
*Extracts complete product catalogs and generates deduplicated 301 URL redirect maps for platform migrations (Magento/WooCommerce to Shopify).*

* **Task 1: [Extract Store Catalog for Migration QA](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor/examples/extract-store-catalog-for-migration-qa)**
  * **Use Case:** Extracts collections, product handles, and variant pricing into standard CSV format for staging comparison.
* **Task 2: [Prepare Redirect Records for Migration Review](https://apify.com/deepaksheoran172/store-catalog-redirect-extractor/examples/prepare-redirect-records-for-migration-review)**
  * **Use Case:** Maps legacy catalog paths to new canonical target routes, eliminating broken backlinks and crawl 404s.
* **Integration Assets:**
  * [n8n Migration Workflow](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool5_store_redirect_extractor_n8n.json)

---

## 3. Technical SEO, Crawlability & Health Auditing

### [Website Health Checker](https://apify.com/deepaksheoran172/website-health-checker)
*High-concurrency URL health and broken link auditor operating with zero browser overhead ($0.001/URL).*

* **Task 1: [Check Website Status and Broken Links](https://apify.com/deepaksheoran172/website-health-checker/examples/check-website-status-and-broken-links)**
  * **Use Case:** Recursively checks internal links, detects 404/500 errors, broken anchor targets, and redirect chains.
* **Task 2: [Review Technical SEO Page Signals](https://apify.com/deepaksheoran172/website-health-checker/examples/review-technical-seo-page-signals)**
  * **Use Case:** Extracts canonical tags, meta robots, OpenGraph titles, and page response latencies.
* **Integration Assets:**
  * [n8n Health Audit Workflow](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool2_website_health_checker_n8n.json)

---

## 4. Domain Security, Deliverability & Protocol Telemetry

### [Domain Security Super-Auditor](https://apify.com/deepaksheoran172/domain-security-super-auditor)
*5-in-1 B2B technical security auditor checking TLS/SSL certificates, HTTP security headers, SPF 10-lookup limits, DMARC, and RDAP age.*

* **Task 1: [Audit Domain TLS and DNS Signals](https://apify.com/deepaksheoran172/domain-security-super-auditor/examples/audit-domain-tls-and-dns-signals)**
  * **Use Case:** Inspects SAN coverage, cipher strength, expiration thresholds, and DNS authoritative nameservers.
* **Task 2: [Review Domain Email Authentication](https://apify.com/deepaksheoran172/domain-security-super-auditor/examples/review-domain-email-authentication)**
  * **Use Case:** Validates SPF record syntax, calculates DNS query depth (staying under the 10-lookup RFC limit), and verifies DMARC enforcement policies.
* **Integration Assets:**
  * [n8n Security Workflow](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool6_domain_security_auditor_n8n.json)
  * [Clay Table Recipe](https://github.com/deepakshe/apify-b2b-super-actors/blob/main/clay_recipes/clay_domain_security_recipe.md)

### [Domain Protocol Signals Enricher](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher)
*Extracts verifiable evidence from well-known domain endpoints (`security.txt`, `assetlinks.json`, `apple-app-site-association`, `mta-sts.txt`, `llms.txt`).*

* **Task 1: [Collect Public Domain Protocol Signals](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher/examples/collect-public-domain-protocol-signals)**
  * **Use Case:** B2B prospect qualification by identifying native mobile apps, security policies, and AI crawler permissions.
* **Task 2: [Inspect Supported Well-Known Domain Files](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher/examples/inspect-well-known-domain-files)**
  * **Use Case:** Audits OAuth discovery endpoints and structured LLM permission files.
* **Integration Assets:**
  * [n8n Protocol Workflow](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool7_domain_protocol_enricher_n8n.json)
  * [Clay Table Recipe](https://github.com/deepakshe/apify-b2b-super-actors/blob/main/clay_recipes/clay_domain_protocol_recipe.md)

---

## 5. Public Procurement Intelligence & Indian Tender Normalization

### [Indian Public Tender Parser](https://apify.com/deepaksheoran172/indian-public-tender-parser)
*Parses complex nested public procurement HTML tables (CPPP, GeM, State eProcurement) into clean datasets.*

* **Task 1: [Structure an Indian Public Tender Notice](https://apify.com/deepaksheoran172/indian-public-tender-parser/examples/structure-indian-public-tender-notice)**
  * **Use Case:** Converts raw tender tables into structured JSON with tender IDs, issuing authority, and categories.
* **Task 2: [Review Tender Deadlines and EMD Fields](https://apify.com/deepaksheoran172/indian-public-tender-parser/examples/review-tender-deadlines-and-emd)**
  * **Use Case:** Normalizes Lakhs/Crores into exact numeric INR and converts closing times to ISO-8601 UTC.
* **Integration Assets:**
  * [n8n Tender Pipeline Workflow](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool3_tender_parser_n8n.json)

---

## 6. AI Infrastructure, MCP Server Registry & Token Pricing

### [OpenRouter MCP Registry](https://apify.com/deepaksheoran172/openrouter-mcp-registry)
*Real-time pricing, context length, and Model Context Protocol (MCP) tool schema registry for AI engineering pipelines.*

* **Task 1: [Compare OpenRouter Model Pricing Data](https://apify.com/deepaksheoran172/openrouter-mcp-registry/examples/compare-openrouter-model-pricing)**
  * **Use Case:** Syncs live token costs ($/1M prompt, $/1M completion) and context window limits across 200+ models.
* **Task 2: [Discover MCP Server Registry Records](https://apify.com/deepaksheoran172/openrouter-mcp-registry/examples/discover-mcp-server-registry-records)**
  * **Use Case:** Indexes available MCP tool endpoints for dynamic routing in multi-agent frameworks (LangChain, CrewAI, AutoGen).
* **Integration Assets:**
  * [n8n Registry Workflow](https://raw.githubusercontent.com/deepakshe/apify-b2b-super-actors/main/workflows/tool4_openrouter_mcp_registry_n8n.json)
  * [Runnable Python Blueprints](https://github.com/deepakshe/apify-b2b-super-actors/tree/main/mcp)

---

## 🛡️ Reliability & Zero False-Completion Standard

- **Deterministic Standard Library:** All scrapers and normalizers are built with zero bloated third-party dependencies (`pandas`, `playwright`), guaranteeing minimal compute spend and lightning-fast execution.
- **Pay-Per-Event (PPE) Pricing:** Transparent pay-as-you-go pricing without mandatory subscriptions.
- **Fail-Closed Security:** Strict anti-SSRF protections, formula injection sanitization, and verified schema compliance.
