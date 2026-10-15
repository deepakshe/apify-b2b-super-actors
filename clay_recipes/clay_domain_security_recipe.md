# Clay 1-Click Integration Recipe: Bulk Domain Security & DMARC Auditing

**Target Actor:** `deepaksheoran172/domain-security-super-auditor`  
**Apify Store URL:** [https://apify.com/deepaksheoran172/domain-security-super-auditor](https://apify.com/deepaksheoran172/domain-security-super-auditor)  
**Cost:** $0.002 per domain audited (Fair-billing guarantee: unresolvable domains charged $0.00)

---

## The Problem in Clay Outbound Stacks
When scaling cold email campaigns using secondary domains in Clay + Smartlead/Instantly, an unenforced DMARC record, an SPF recursive lookup count exceeding 10, or an SSL cert with <14 days remaining will cause Google and Yahoo to dump outbound messages into the spam folder.

---

## 3-Minute Setup in Clay

### Step 1: Add Apify Connection
1. In your [Clay.com](https://clay.com) workspace, go to **Settings > Connections**.
2. Select **Apify** and paste your Apify API Token.

### Step 2: Add Enrichment Column
1. In your target Clay table (with a `Domain` or `Website` column), click **Add Enrichment**.
2. Search for **Apify** and select **Run Apify Actor**.
3. Choose Actor: `deepaksheoran172/domain-security-super-auditor`.

### Step 3: Input JSON Configuration
Paste this input mapping:

```json
{
  "domains": [
    "{{v.Domain}}"
  ],
  "include_dns_deliverability": true,
  "include_rdap_age": true,
  "min_composite_score_warning": 70
}
```

### Step 4: Map Output Columns to Clay
Select these returned fields to stream directly into your Clay table:

| Actor Output Field | Clay Column Name | Purpose / Threshold |
| :--- | :--- | :--- |
| `data.composite_risk_score` | `Domain Risk Score` | 0–100 integer. Filter for `>= 80` before launching. |
| `data.dmarc.policy` | `DMARC Policy` | Must be `quarantine` or `reject` for high-volume outbound. |
| `data.spf.lookup_count` | `SPF Lookups` | Must be `<= 10` (RFC 7208 strict limit). |
| `data.ssl.days_remaining` | `SSL Days Remaining` | Flag if `< 30` days. |
| `data.rdap.age_days` | `Domain Age (Days)` | Flag if `< 30` (burner/fresh domain warning). |

---

## Actionable Clay Filter Formula
Use this formula in a Clay **Formula Column** named `Outbound Ready`:

```javascript
({{v.DMARC Policy}} === "reject" || {{v.DMARC Policy}} === "quarantine") && 
{{v.SPF Lookups}} <= 10 && 
{{v.SSL Days Remaining}} > 30 && 
{{v.Domain Age (Days)}} > 30 ? "READY" : "AT RISK"
```

Only push domains with `"READY"` status to Smartlead or Instantly.
