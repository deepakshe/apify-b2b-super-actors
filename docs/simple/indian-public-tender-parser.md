# Indian Tender Notice Parser (CPPP, GeM, State Portals)

**In one line:** Paste the HTML of a tender notice. Get clean data back: tender ID, department, work name, value in ₹, EMD, and closing date in standard format, with corrigendum and duplicate flags.

## Who is this for
- **Tender consultants and bid teams** who copy tender details into Excel by hand.
- **Developers building tender alert or tender search apps** who need one clean format from many portals.

## What you give
```json
{ "raw_html": "<table><tr><td>Tender Reference No:</td><td>NIT-2026-PWD-8841</td></tr>...</table>",
  "source_url": "https://eprocure.gov.in/eprocure/app",
  "portal_name": "Indian eProcurement Portal" }
```

## What you get (real output from the example above)
| field | value |
|---|---|
| tender_id | NIT-2026-PWD-8841 |
| organization | Public Works Department |
| title | Construction of 4-Lane Bypass Road |
| estimated_cost_inr | 15500000 (from "₹ 1.55 Crore") |
| emd_inr | 310000 (from "₹ 3,10,000") |
| closing_date_iso | 2026-11-05T11:30:00Z (from "05-Nov-2026 05:00 PM IST") |
| is_corrigendum / is_duplicate | false / false |

"Crore" and "Lakh" amounts and IST dates are converted for you.

## Price
- $0.02 per run + $0.005 per tender parsed
- One tender notice per run ≈ **$0.025** (about ₹2).

## How to use (3 steps)
1. Open https://apify.com/deepaksheoran172/indian-public-tender-parser and click **Try for free**.
2. Paste the tender page HTML into `raw_html` (in your browser: right-click → View source → copy).
3. Click **Start** and download the result as JSON or CSV.

## What it does NOT do
- **It does not log in to or crawl tender portals.** You give it the HTML. (Portals use captchas and logins.)
- It does not submit bids or download tender documents.
