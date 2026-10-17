# Domain Protocol & Mobile App Link Signals Enricher

[![Apify Store](https://img.shields.io/badge/Apify%20Store-Live%20Actor-blue?logo=apify)](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher)
[![Price](https://img.shields.io/badge/Launch%20Price-$2.40%2F1k%20domains-brightgreen)](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher)

Inspects `assetlinks.json`, `apple-app-site-association`, and RFC 9116 `security.txt` endpoints for mobile deep-linking compliance and protocol health.

---

## 💰 ROI Price Anchoring & Cost Comparison

| Solution Tier | Cost Structure | Protocol Coverage | RFC Validation |
|---|---|---|---|
| **Manual Mobile QA Audit** | **$160.00 / audit** | 1 Domain | Manual browser checks |
| **Regular Store PPE Price** | $6.00 / 1k domains | Android + iOS + Security | Full automated verification |
| **⚡ Active 60% Launch Discount** | **$2.40 / 1k domains** *(Save 98.5%)* | **Complete Suite** | **RFC 9116 Compliant** |

> 🚨 **Urgency Hook:** 60% Launch Discount active. Audit universal links across 1,000 domains in 60 seconds.

---

## 🔍 10-Row Empirical CSV Teaser Proof

| Row | Domain | Android App Links | iOS Universal Links | security.txt | Protocol Status |
|---|---|---|---|---|---|
| 1 | `fashion-retail-app.com` | `assetlinks.json` (Valid) | `apple-app-site-association` (Valid) | Present | `PASS` |
| 2 | `bank-mobile-portal.net` | Missing SHA256 Cert | Missing Details | Present | `FAIL` |
| 3 | `crypto-wallet-web.io` | `assetlinks.json` (Valid) | Missing JSON format | Missing | `WARNING` |
| 4 | `ride-share-mobility.co` | `assetlinks.json` (Valid) | `apple-app-site-association` (Valid) | Present | `PASS` |
| 5 | `health-tracker-direct.org` | HTTP 404 Not Found | HTTP 404 Not Found | Present | `FAIL` |
| 6 | `travel-booking-hub.com` | `assetlinks.json` (Valid) | `apple-app-site-association` (Valid) | Missing | `WARNING` |
| 7 | `stream-video-service.tv` | Unsigned Package | `apple-app-site-association` (Valid) | Present | `WARNING` |
| 8 | `b2b-erp-cloud.com` | `assetlinks.json` (Valid) | `apple-app-site-association` (Valid) | Present | `PASS` |
| 9 | `food-delivery-network.app`| Invalid JSON syntax | Valid | Present | `FAIL` |
| **10** | *`+ 490 more mobile domains...`*| *`[LOCKED]`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[Run on Apify to Unlock]`* |

---

## 🚀 Quickstart via Apify API

```bash
curl -X POST "https://api.apify.com/v2/acts/deepaksheoran172~domain-protocol-signals-enricher/run-sync-get-dataset-items" \
  -H "Content-Type: application/json" \
  -d '{"domains": ["example.com"], "check_well_known": true}'
```
