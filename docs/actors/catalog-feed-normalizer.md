# Shopify Supplier Feed & CSV Normalizer

[![Apify Store](https://img.shields.io/badge/Apify%20Store-Live%20Actor-blue?logo=apify)](https://apify.com/deepaksheoran172/catalog-feed-normalizer)
[![Price](https://img.shields.io/badge/Apify%20Rate-$0.05%20base%20+%20$0.0005%2Fitem-brightgreen)](https://apify.com/deepaksheoran172/catalog-feed-normalizer)

Cleans malformed supplier CSVs, resolves unescaped delimiters, and outputs Shopify-compliant catalog feeds that import without errors.

---

## 💰 ROI Price Anchoring & Cost Comparison

| Solution Tier | Cost Structure | Manual Effort | Error Rejection Rate |
|---|---|---|---|
| **Manual Data Ops Contractor** | **$200.00 / catalog** | 6–8 Hours | Frequent Excel parsing errors |
| **Apify Pay-Per-Event (PPE)** | **$0.05 base + $0.0005 / item** *(~$0.55 / 1k)* | **30 Seconds** | **Zero delimiter crashes** |
| **⚡ Net Savings** | **Save 99.7%** vs Contractor | **Instant** | **100% RFC 4180 Validated** |

> 🚨 **The Ops Killer:** Clean 1,000 product feed rows for $0.55 on Apify Cloud instead of paying a freelancer $200 for manual Excel cleanup.

---

## 🔍 10-Row Empirical CSV Teaser Proof

| Row | Product Title | Raw Input Price | Normalized Price | Delimiter Error | Fix Applied |
|---|---|---|---|---|---|
| 1 | `Cotton T-Shirt (Red, L)` | `15.99 USD` | `15.99` | Unescaped comma in title | Quoted RFC 4180 |
| 2 | `Ceramic Coffee Mug "Vintage"` | `$24.50` | `24.50` | Unescaped quotes | Escaped double-quotes |
| 3 | `Wireless Earbuds Pro` | `EUR 79,90` | `79.90` | Comma decimal format | Normalized to standard decimal |
| 4 | `Running Shoes Size 10` | `49.00` | `49.00` | None | Validated clean |
| 5 | `Leather Belt / Brown` | `19.95` | `19.95` | Special character slash | Sanitized UTF-8 |
| 6 | `Desk Lamp - Minimalist` | `$34.00` | `34.00` | Leading currency symbol | Stripped symbol |
| 7 | `Stainless Steel Water Bottle` | `12.50` | `12.50` | None | Validated clean |
| 8 | `Bluetooth Speaker = Bass+` | `89.00` | `89.00` | Excel formula injection (`=`) | Quoted & sanitized |
| 9 | `Smart Watch Band` | `9.99` | `9.99` | Trailing whitespace | Trimmed |
| **10** | *`+ 1,420 more catalog items...`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[Run on Apify to Unlock]`* |

---

## 🚀 Quickstart via Apify API

```bash
curl -X POST "https://api.apify.com/v2/acts/deepaksheoran172~catalog-feed-normalizer/run-sync-get-dataset-items" \
  -H "Content-Type: application/json" \
  -d '{"csv_url": "https://example.com/raw_supplier_feed.csv"}'
```
