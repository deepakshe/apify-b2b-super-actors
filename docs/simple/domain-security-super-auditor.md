# Domain Security & Email Health Checker (SPF, DMARC, SSL)

**In one line:** Paste a list of domains. Get a simple A–F grade for each one, and a clear list of what is broken: SPF, DMARC, SSL expiry, security headers.

## Who is this for
- **Email marketing / deliverability agencies**: check every client domain before you send a campaign.
- **MSPs and IT consultants**: one report for all your clients' domains.
- **Cold email teams**: find domains with weak email setup before you warm them up.

## What you give
```json
{ "domains": ["yourclient.com", "anotherclient.co.uk"] }
```

## What you get (real output, scanned on 2026-10-18)
| domain | grade | SPF | DMARC | SSL days left |
|---|---|---|---|---|
| andzen.com.au | D (57) | softfail, 10 DNS lookups (at the limit) | p=none | 35 |
| orcaad.com | C (74) | softfail | **missing** | 39 |
| webmefy.com | A (92) | softfail | p=none | 87 |

Every row also has the raw SPF and DMARC record, the MX provider, HSTS/CSP status, and domain age, so you can check each result yourself.

## Price
- $0.0025 per domain for the SSL and security check
- $0.0025 per domain for the DNS, SPF, DMARC and domain-age check
- **100 domains ≈ $0.50.** If a domain does not resolve (NXDOMAIN), you are not charged for it.

## How to use (3 steps)
1. Open https://apify.com/deepaksheoran172/domain-security-super-auditor and click **Try for free**.
2. Paste your domains into `domains`.
3. Click **Start**. Download the results as CSV, Excel or JSON.

## What it does NOT do
- It does not fix records for you. It tells you exactly what to fix.
- It does not check DNSSEC or CAA records.
- It does not send test emails or check spam placement.
