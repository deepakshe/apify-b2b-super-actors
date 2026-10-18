# Domain App-Link, Login & AI-File Detector

**In one line:** Give it a list of domains. For each one it tells you if the company has a mobile app deep link (iOS/Android), an SSO/OIDC login, `security.txt`, MTA-STS, or `llms.txt`.

## Who is this for
- **RevOps / Clay / lead-gen teams**: tag prospects, e.g. "has a mobile app", "has SSO", "is AI-ready (llms.txt)".
- **App and headless-commerce agencies**: find brands that have no app links yet.
- **Security consultants**: find companies with no `security.txt` or MTA-STS.

## What you give
```json
{ "domains": ["brand1.com", "brand2.com"] }
```

## What you get (real output, scanned on 2026-10-18)
| domain | iOS app link | Android app link | OIDC login | security.txt | llms.txt |
|---|---|---|---|---|---|
| pogodan.com | detected | not_found | detected | not_found | detected |
| comerix.com | not_found | not_found | detected | not_found | not_found |
| 424solutions.com | not_found | not_found | not_found | not_found | detected |

## Price
- $0.001 per domain. **1,000 domains = $1.**

## How to use (3 steps)
1. Open https://apify.com/deepaksheoran172/domain-protocol-signals-enricher and click **Try for free**.
2. Paste the domains.
3. Click **Start**, download the CSV, and filter on the column you need.

## What it does NOT do
- It only reads public `/.well-known/` files. It does not log in or scan ports.
- `not_found` means the file is not published. It does not prove the company has no app.
