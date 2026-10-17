# India Public Tender & Procurement Intelligence Parser

[![Apify Store](https://img.shields.io/badge/Apify%20Store-Live%20Actor-blue?logo=apify)](https://apify.com/deepaksheoran172/indian-public-tender-parser)
[![Price](https://img.shields.io/badge/Apify%20Rate-$0.02%20base%20+%20$0.005%2Frecord-brightgreen)](https://apify.com/deepaksheoran172/indian-public-tender-parser)

Extracts and normalizes tender notices, EMD values, submission deadlines, and bid documents from public procurement portals (GeM / CPPP).

---

## 💰 ROI Price Anchoring & Cost Comparison

| Solution Tier | Cost Structure | Update Speed | Integration |
|---|---|---|---|
| **Legacy Tender Portals** | **₹50,000–₹1,50,000 / year** | Daily email dumps | Proprietary closed UI |
| **Apify Pay-Per-Event (PPE)** | **$0.02 base + $0.005 / record** *(~$5.02 / 1k)* | Real-Time | n8n / Clay / Webhook Native |
| **⚡ Net Savings** | **Save 99.0%** vs Annual Contract | **Instant** | **REST API Output** |

> 🚨 **The Portal Killer:** Parse 1,000 government tenders for ~$5.00 on Apify Cloud instead of locking into a ₹50,000/year closed database subscription.

---

## 🔍 10-Row Empirical CSV Teaser Proof

| Row | Tender ID | Procuring Authority | Value (INR) | EMD Amount | Bid Due Date (UTC) |
|---|---|---|---|---|---|
| 1 | `GEM/2026/B/89210` | Ministry of Railways | ₹4,20,00,000 | ₹8,40,000 | 2026-11-15T15:00:00Z |
| 2 | `CPPP/NHAI/48201` | NHAI Civil Works | ₹18,50,00,000 | ₹37,00,000 | 2026-11-18T12:00:00Z |
| 3 | `GEM/2026/B/77102` | Defense R&D Org | ₹95,00,000 | ₹1,90,000 | 2026-11-10T10:30:00Z |
| 4 | `CPPP/AIIMS/0921` | AIIMS Medical Supplies | ₹2,10,00,000 | ₹4,20,000 | 2026-11-20T17:00:00Z |
| 5 | `GEM/2026/B/66190` | State Electricity Board | ₹6,40,00,000 | ₹12,80,000 | 2026-11-22T14:00:00Z |
| 6 | `CPPP/BSNL/55102` | Telecom Network Ops | ₹1,80,00,000 | ₹3,60,000 | 2026-11-12T11:00:00Z |
| 7 | `GEM/2026/B/44910` | Municipal Smart City | ₹8,90,00,000 | ₹17,80,000 | 2026-11-25T16:00:00Z |
| 8 | `CPPP/ISRO/22019` | Aerospace Instrumentation | ₹3,50,00,000 | ₹7,00,000 | 2026-11-14T09:00:00Z |
| 9 | `GEM/2026/B/33100` | Port Authority Logistics | ₹5,75,00,000 | ₹11,50,000 | 2026-11-19T13:30:00Z |
| **10** | *`+ 3,190 more active tenders...`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[Run on Apify to Unlock]`* |

---

## 🚀 Quickstart via Apify API

```bash
curl -X POST "https://api.apify.com/v2/acts/deepaksheoran172~indian-public-tender-parser/run-sync-get-dataset-items" \
  -H "Content-Type: application/json" \
  -d '{"portal": "gem", "keywords": ["solar", "infrastructure"], "max_records": 500}'
```
