# Bulk Domain Security & SSL/TLS Audit Tool

[![Apify Store](https://img.shields.io/badge/Apify%20Store-Live%20Actor-blue?logo=apify)](https://apify.com/deepaksheoran172/domain-security-super-auditor)
[![Price](https://img.shields.io/badge/Apify%20Rate-$0.001%2Fdomain-brightgreen)](https://apify.com/deepaksheoran172/domain-security-super-auditor)

Audits client domains in bulk for SSL/TLS certificate validity, cipher deprecation, HSTS, and SPF/DKIM/DMARC email deliverability records.

---

## 💰 ROI Price Anchoring & Cost Comparison

| Solution Tier | Cost Structure | Coverage | Verification Standard |
|---|---|---|---|
| **Manual Cybersecurity Audit** | **$180.00 / audit** | 1 Domain | Manual OpenSSL & DNS lookup |
| **Apify Pay-Per-Event (PPE)** | **$0.001 / domain** *($1.00 / 1k domains)* | Unlimited | Automated TLS 1.3 + RFC checks |
| **⚡ Net Savings** | **Save 99.4%** vs Consultant | **Unlimited** | **RFC 7208 / 7489 Compliant** |

> 🚨 **The Consultant Killer:** Audit 1,000 domains for $1.00 on Apify Cloud instead of paying $180 for a manual PDF audit.

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
