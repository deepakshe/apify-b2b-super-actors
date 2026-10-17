# Website Health & Broken Link Auditing Engine

[![Apify Store](https://img.shields.io/badge/Apify%20Store-Live%20Actor-blue?logo=apify)](https://apify.com/deepaksheoran172/website-health-checker)
[![Price](https://img.shields.io/badge/Apify%20Rate-$0.001%2Fpage-brightgreen)](https://apify.com/deepaksheoran172/website-health-checker)

Crawls web properties to identify 404 dead links, broken redirects, slow TTFB latency, and missing SEO metadata.

---

## 💰 ROI Price Anchoring & Cost Comparison

| Solution Tier | Cost Structure | Subscription Requirement | Scan Limit |
|---|---|---|---|
| **SaaS Crawlers (Ahrefs/Semrush)** | **$199.00 / month** | Mandatory Monthly Retainer | Strict URL limits |
| **Apify Pay-Per-Event (PPE)** | **$0.001 / page** *($1.00 / 1k pages)* | Zero Retainer | Unlimited Concurrency |
| **⚡ Net Savings** | **Save 99.5%** vs SaaS | **Pay As You Go** | **Zero Commitment** |

> 🚨 **The SaaS Killer:** Crawl 1,000 pages for $1.00 on Apify Cloud instead of locking into a $199/month recurring tool subscription.

---

## 🔍 10-Row Empirical CSV Teaser Proof

| Row | Page URL | Target Broken Anchor | HTTP Status | Root Cause |
|---|---|---|---|---|
| 1 | `/blog/marketing-guide` | `https://partner.com/signup-old` | 404 | Expired external domain |
| 2 | `/pricing` | `/features/v1-legacy` | 404 | Deleted product feature |
| 3 | `/about-us` | `/team/former-vp` | 404 | Orphaned bio page |
| 4 | `/products/item-01` | `https://cdn.example.com/img99.jpg` | 403 | S3 bucket permission error |
| 5 | `/checkout` | `/terms-and-conditions-2022` | 301 Loop | Redirect loop detected |
| 6 | `/contact` | `/support/faq-old` | 404 | Moved help center |
| 7 | `/press/releases` | `/downloads/media-kit.pdf` | 404 | Missing static asset |
| 8 | `/case-studies/corp-a` | `https://corp-a.com/case` | 502 | Target server timeout |
| 9 | `/integrations` | `/docs/v1/webhooks` | 404 | Deprecated documentation |
| **10** | *`+ 640 more scanned URLs...`* | *`[LOCKED]`* | *`404`* | *`[Run on Apify to Unlock]`* |

---

## 🚀 Quickstart via Apify API

```bash
curl -X POST "https://api.apify.com/v2/acts/deepaksheoran172~website-health-checker/run-sync-get-dataset-items" \
  -H "Content-Type: application/json" \
  -d '{"start_urls": [{"url": "https://example.com"}], "max_pages": 500}'
```
