# Clay 1-Click Integration Recipe: B2B Domain Protocol & App Link Enrichment

**Target Actor:** `deepaksheoran172/domain-protocol-signals-enricher`  
**Apify Store URL:** [https://apify.com/deepaksheoran172/domain-protocol-signals-enricher](https://apify.com/deepaksheoran172/domain-protocol-signals-enricher)  
**Cost:** $0.001 per domain probed (Tri-state evidence model: zero false negatives)

---

## The Problem in Clay Outbound & Tech Stack Enrichment
When qualifying target B2B accounts in Clay, answering fundamental engineering questions usually requires fragile HTML scraping:
- Does this prospect company build native mobile apps?
- Do they maintain an active vulnerability disclosure program (`security.txt`)?
- Do they enforce enterprise SMTP transport security (`mta-sts.txt`)?
- Do they maintain modern LLM markdown documentation (`llms.txt`)?

Scraping homepage HTML breaks constantly and costs $0.05–$0.15 in proxy compute. This Actor queries standardized `/.well-known/` protocols in milliseconds.

---

## 3-Minute Setup in Clay

### Step 1: Add Apify Connection
1. In your [Clay.com](https://clay.com) workspace, go to **Settings > Connections**.
2. Select **Apify** and paste your Apify API Token.

### Step 2: Add Enrichment Column
1. In your target Clay table (with a `Domain` or `Website` column), click **Add Enrichment**.
2. Search for **Apify** and select **Run Apify Actor** or use **HTTP API Request**.
3. Choose Actor: `deepaksheoran172/domain-protocol-signals-enricher`.

### Step 3: Input JSON Configuration
Paste this input mapping:

```json
{
  "domains": [
    "{{v.Domain}}"
  ],
  "probe_app_links": true,
  "probe_identity_metadata": true,
  "probe_security_policies": true,
  "probe_domain_files": true,
  "concurrency": 5,
  "request_timeout_secs": 10
}
```

### Step 4: Map Output Columns to Clay
Select these returned fields to stream directly into your Clay table:

| Actor Output Field | Clay Column Name | Purpose / Threshold |
| :--- | :--- | :--- |
| `data.android_app_links_status` | `Android App Links` | `"detected"` = Confirmed native Android deep-linking app. |
| `data.android_package_names` | `Android Packages` | Array of package IDs (e.g. `com.company.app`). |
| `data.ios_aasa_status` | `iOS Universal Links` | `"detected"` = Confirmed native iOS app. |
| `data.ios_app_ids` | `iOS App IDs` | Array of TeamID.BundleIDs. |
| `data.security_txt_status` | `Security.txt Status` | `"detected"` = Active RFC 9116 vulnerability reporting program. |
| `data.security_contacts` | `Security Contacts` | Direct email/HackerOne/Bugcrowd intake endpoints. |
| `data.mta_sts_mode` | `MTA-STS Mode` | `"enforce"` = High-security email infrastructure. |
| `data.llms_txt_status` | `LLMs.txt Status` | `"detected"` = AI/Agentic documentation curated. |

---

## Actionable Clay Filter Formula
Use this formula in a Clay **Formula Column** named `Tech Segment`:

```javascript
({{v.Android App Links}} === "detected" || {{v.iOS Universal Links}} === "detected") 
  ? "Mobile-First Company" 
  : ({{v.Security.txt Status}} === "detected" ? "Enterprise Compliant" : "Standard Web")
```
