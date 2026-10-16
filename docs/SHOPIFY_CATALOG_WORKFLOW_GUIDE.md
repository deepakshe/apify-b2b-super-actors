# Shopify Supplier-Feed Preparation & Validation Workflow Guide

A practical, technical reference for e-commerce operations teams, Shopify merchants, and catalog migration developers who need to normalize raw vendor CSV exports and validate product data before bulk import.

---

## 1. The Core Operational Problem

When receiving dropshipping feeds, wholesaler CSVs, or legacy catalog exports, differences in formatting routinely break Shopify's native CSV import:

- **Missing Variant Handles:** Multiple variant rows (e.g., Size, Color) missing a common parent `Handle` are created as separate standalone products rather than grouped variants.
- **European Decimals & Currency Notation:** Raw strings such as `"1.499,00 €"` or `"$19.95 USD"` fail Shopify's numeric float validation or cause silent zeroing (`0.00`).
- **Unescaped HTML & Formula Injections:** Commas inside unquoted product descriptions corrupt column alignment under RFC 4180. Cells beginning with `=`, `+`, `-`, or `@` trigger spreadsheet formula warnings.
- **Silent Import Failures:** Importing dirty data without pre-validation results in partial imports, duplicate SKUs, or time-consuming manual rollbacks in Shopify Admin.

---

## 2. Verified Actor Capabilities

The [`deepaksheoran172/catalog-feed-normalizer`](https://apify.com/deepaksheoran172/catalog-feed-normalizer) Actor provides two deterministic processing jobs:

1. **Feed Normalization:** Groups variant rows under slugified parent handles, standardizes Option1/Option2/Option3 hierarchies, converts currency strings into clean two-decimal floats, and safely quotes all text columns to RFC 4180 standards.
2. **Pre-Import Diagnostic Validation:** Scans the feed before Shopify import, checking for duplicate SKUs, missing titles, empty variant prices, and malformed rows. Ambiguous or corrupted rows are quarantined with descriptive audit codes rather than guessed.

---

## 3. Published 1-Click Task Pages

Both workflows can be executed directly on the Apify platform via dedicated public Task Pages without manual configuration:

- **Task 1 — Normalization:**  
  [Normalize Supplier CSV for Shopify Import](https://apify.com/deepaksheoran172/catalog-feed-normalizer/examples/normalize-supplier-csv-shopify)  
  *Directly transforms messy vendor CSV rows into standardized Shopify import CSV format.*

- **Task 2 — Validation & QA:**  
  [Validate Product CSV Before Shopify Import](https://apify.com/deepaksheoran172/catalog-feed-normalizer/examples/validate-product-csv-shopify)  
  *Runs diagnostic audits to identify corrupted fields, duplicate identifiers, and formatting issues prior to import.*

---

## 4. Input Specification (Live Schema)

The Actor accepts the following verified input properties:

| Property | Type | Required | Description | Default / Example |
|---|---|:---:|---|---|
| `rawCsv` | String | No* | Raw CSV content pasted directly into the input. | Synthetic vendor CSV string |
| `csvUrl` | String | No* | Public HTTP/HTTPS URL pointing to a remote CSV feed. | *(Provide either `rawCsv` or `csvUrl`)* |
| `mapping` | Object | No | Custom column mapping dictionary to bridge vendor headers. | `{ "Vendor SKU": "Variant SKU" }` |
| `defaultVendor` | String | No | Fallback vendor string applied when row vendor is missing. | `"Acme Supplies"` |
| `defaultStatus` | String | No | Default Shopify product status: `draft` or `active`. | `"draft"` |

---

## 5. Synthetic Sample Walkthrough

### Raw Input Example (Dirty Synthetic Data)
```csv
SKU,Product Name,Raw Price,Color,Size,Supplier
RUN-01,Trail Runner Sneaker =SUM(1+1),"1.299,50 €",Navy,10,Wholesale Direct
RUN-02,Trail Runner Sneaker,"1.299,50 €",Navy,11,Wholesale Direct
RUN-03,Trail Runner Sneaker,"1.299,50 €",Black,10,Wholesale Direct
```

### Normalized Shopify Output Example (Clean RFC 4180)
```csv
Handle,Title,Option1 Name,Option1 Value,Option2 Name,Option2 Value,Variant SKU,Variant Price,Vendor,Status
trail-runner-sneaker,"Trail Runner Sneaker ' =SUM(1+1)",Color,Navy,Size,10,RUN-01,1299.50,Wholesale Direct,draft
trail-runner-sneaker,"Trail Runner Sneaker ' =SUM(1+1)",Color,Navy,Size,11,RUN-02,1299.50,Wholesale Direct,draft
trail-runner-sneaker,"Trail Runner Sneaker ' =SUM(1+1)",Color,Black,Size,10,RUN-03,1299.50,Wholesale Direct,draft
```

---

## 6. Known Scope & Operational Limitations

- **Source Ingestion:** The Actor processes provided raw CSV text or accessible HTTP(S) CSV URLs. It does not authenticate into private vendor intranets, solve CAPTCHAs, or navigate multi-factor auth supplier portals.
- **Data Governance:** The normalizer operates as a deterministic syntax and schema engine; it does not verify inventory levels with external ERPs or fabricate missing product descriptions.
- **Search Engine & Platform Outcomes:** Formatting your feed to official Shopify RFC 4180 specifications ensures syntactic import validity; it does not guarantee search rankings, marketplace acceptance, or sales conversions.
- **Recommended Workflow:** Always test a representative sample (10–50 rows) before running large-scale batch transformations.
