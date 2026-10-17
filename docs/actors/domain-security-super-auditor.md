# Bulk Domain Security & SSL/TLS Audit Tool

[![Apify Store](https://img.shields.io/badge/Apify%20Store-Live%20Actor-blue?logo=apify)](https://apify.com/deepaksheoran172/domain-security-super-auditor)
[![Price](https://img.shields.io/badge/Launch%20Price-$2.40%2F1k%20domains-brightgreen)](https://apify.com/deepaksheoran172/domain-security-super-auditor)

Audits client domains in bulk for SSL/TLS certificate validity, cipher deprecation, HSTS, and SPF/DKIM/DMARC email deliverability records.

---

## 💰 ROI Price Anchoring & Cost Comparison

| Solution Tier | Cost Structure | Coverage | Verification Standard |
|---|---|---|---|
| **Manual Cybersecurity Audit** | **$180.00 / audit** | 1 Domain | Manual OpenSSL & DNS lookup |
| **Regular Store PPE Price** | $6.00 / 1k domains | Unlimited | Automated TLS 1.3 + RFC checks |
| **⚡ Active 60% Launch Discount** | **$2.40 / 1k domains** *(Save 98.7%)* | **Unlimited** | **RFC 7208 / 7489 Compliant** |

> 🚨 **Urgency Hook:** 60% Launch Discount active for MSPs and consultants. Scan 1,000 domains for just $2.40.

---

## 🔍 10-Row Empirical CSV Teaser Proof

| Row | Domain | SSL Days Remaining | Missing Headers | DMARC Policy | Grade |
|---|---|---|---|---|---|
| 1 | `client-store-alpha.com` | 14 *(CRITICAL)* | `HSTS, CSP` | `p=none` *(Vulnerable)* | `C` |
| 2 | `secure-portal-beta.io` | 180 | `X-Frame-Options` | `p=reject` | `A` |
| 3 | `agency-hub-gamma.co` | 3 | `HSTS, DMARC` | `MISSING` *(Spoofable)* | `F` |
| 4 | `fintech-checkout.net` | 365 | None | `p=reject` | `A+` |
| 5 | `legacy-corp-site.org` | -2 *(EXPIRED)* | `HSTS, CSP, X-Frame` | `p=none` | `F` |
| 6 | `global-logistics.de` | 28 | `CSP` | `p=quarantine` | `B` |
| 7 | `retail-outlet-uk.com` | 92 | `HSTS` | `p=none` | `C` |
| 8 | `health-tech-api.io` | 45 | None | `p=reject` | `A` |
| 9 | `saas-billing-portal.com` | 12 *(WARNING)* | `CSP` | `p=reject` | `B+` |
| **10** | *`+ 892 more domains detected...`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[LOCKED]`* | *`[LOCKED]`* |

---

## 🚀 Quickstart via Apify API

```bash
curl -X POST "https://api.apify.com/v2/acts/deepaksheoran172~domain-security-super-auditor/run-sync-get-dataset-items" \
  -H "Content-Type: application/json" \
  -d '{"domains": ["example.com"], "include_dns_deliverability": true}'
```
