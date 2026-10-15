#!/usr/bin/env python3
"""autonomous_marketing_daemon.py

24/7 Autonomous B2B Marketing & Cold Outbound Distribution Engine.
Audits target accounts every 3-4 hours in rotating batches using Tool 6 + Tool 7,
generating evidence-backed Trojan Horse cold outreach and technical community posts.
Runs 100% locally with zero cloud spend ($0.00).
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

# Setup paths
SCRIPT_DIR = Path(__file__).resolve().parent
DIST_KIT_DIR = SCRIPT_DIR.parent
GROWTH_AUDIT_DIR = DIST_KIT_DIR / "growth_audit"
DISPATCH_DIR = GROWTH_AUDIT_DIR / "scheduled_dispatches"
PROJECT_ROOT = DIST_KIT_DIR.parent.parent

# Clean dynamic imports for Tool 6 & Tool 7
t6_dir = PROJECT_ROOT / "01_apify_actors" / "domain_security_super_auditor_v1"
t7_dir = PROJECT_ROOT / "01_apify_actors" / "domain_protocol_signals_enricher_v1"

sys.path.insert(0, str(t6_dir))
import src.auditors as t6_auditors
sys.path.remove(str(t6_dir))
if "src" in sys.modules:
    del sys.modules["src"]

sys.path.insert(0, str(t7_dir))
import src.enricher as t7_enricher

TARGETS_CSV = GROWTH_AUDIT_DIR / "master_target_companies.csv"
STATE_FILE = GROWTH_AUDIT_DIR / "daemon_state.json"
QUEUE_CSV = GROWTH_AUDIT_DIR / "marketing_queue.csv"


def load_target_catalog() -> List[Dict[str, str]]:
    """Loads all target accounts dynamically from master_target_companies.csv."""
    if not TARGETS_CSV.exists():
        return [
            {"domain": "linear.app", "company": "Linear", "category": "Productivity & Issue Tracking"},
            {"domain": "supabase.com", "company": "Supabase", "category": "Developer Infrastructure"},
        ]
    records = []
    with open(TARGETS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append({
                "domain": row.get("domain", "").strip(),
                "company": row.get("company", "").strip(),
                "category": row.get("category", "B2B Enterprise").strip(),
                "priority": row.get("priority", "P1").strip(),
                "tier": row.get("tier", "Tier-1").strip(),
            })
    return [r for r in records if r["domain"]]


def load_state() -> Dict[str, Any]:
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"current_index": 0, "total_runs": 0, "last_run_utc": None, "history": []}


def save_state(state: Dict[str, Any]) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def audit_account(target: Dict[str, str]) -> Dict[str, Any]:
    domain = target["domain"]
    company = target["company"]
    category = target["category"]

    # Tool 6
    try:
        t6_res = t6_auditors.audit_single_domain(domain, {
            "include_dns_deliverability": True,
            "include_rdap_age": False,  # fast, lean execution
            "timeout_seconds": 5,
        })
    except Exception as exc:
        t6_res = {"letter_grade": "N/A", "overall_score": 0, "error": str(exc)}

    # Tool 7
    try:
        enricher = t7_enricher.DomainProtocolEnricher(
            timeout_secs=5,
            probe_app_links=True,
            probe_identity_metadata=True,
            probe_security_policies=True,
            probe_domain_files=True,
        )
        t7_res = enricher.enrich_domain(domain)
    except Exception as exc:
        t7_res = {"scan_status": "unreachable", "error": str(exc)}

    return {
        "domain": domain,
        "company": company,
        "category": category,
        "audited_at": datetime.now(timezone.utc).isoformat(),
        "tool6": {
            "letter_grade": t6_res.get("letter_grade", "N/A"),
            "score": t6_res.get("overall_score", 0),
            "ssl_issuer": t6_res.get("ssl_audit", {}).get("issuer_org", "Unknown"),
            "ssl_days": t6_res.get("ssl_audit", {}).get("days_until_expiry"),
            "dmarc": t6_res.get("email_deliverability_audit", {}).get("dmarc_policy", "missing"),
            "spf_lookups": t6_res.get("email_deliverability_audit", {}).get("spf_lookup_count", 0),
            "spf_policy": t6_res.get("email_deliverability_audit", {}).get("spf_policy", "missing"),
            "mx_provider": t6_res.get("email_deliverability_audit", {}).get("mx_provider", "Unknown"),
        },
        "tool7": {
            "android_apps": len(t7_res.get("android_package_names", [])),
            "ios_apps": len(t7_res.get("ios_app_ids", [])),
            "security_txt": t7_res.get("security_txt_status", "not_found"),
            "mta_sts": t7_res.get("mta_sts_mode") or "none",
            "llms_txt": t7_res.get("llms_txt_status", "not_found"),
        },
    }


def generate_outbound_emails(rec: Dict[str, Any]) -> Dict[str, str]:
    domain = rec["domain"]
    company = rec["company"]
    t6 = rec["tool6"]
    t7 = rec["tool7"]

    ssl_str = f"{t6['ssl_days']} days remaining" if t6['ssl_days'] is not None else "Inspection bypassed"
    dmarc = t6["dmarc"]
    spf_lookups = t6["spf_lookups"]
    sec_txt = t7["security_txt"]
    mta_sts = t7["mta_sts"]
    apps_count = t7["android_apps"] + t7["ios_apps"]

    cto_email = f"""Subject: Quick engineering hygiene snippet for {domain} (SSL, RFC 9116, DMARC)

Hi {company} team,

Ran an automated pre-flight infrastructure hygiene check on {domain} as part of our weekly protocol scanner. Thought your engineering team would find the diagnostic findings useful:

Diagnostic Summary:
• Security Posture Grade: {t6['letter_grade']} ({t6['score']}/100)
• SSL Certificate: {ssl_str} (Issuer: {t6['ssl_issuer']})
• RFC 7208 SPF Lookups: {spf_lookups} / 10 limit (Policy: {t6['spf_policy']})
• DMARC Policy: {dmarc} (MX Provider: {t6['mx_provider']})
• RFC 9116 security.txt: {sec_txt}
• MTA-STS Mode: {mta_sts}
• Deep-Linked Mobile Apps: {apps_count} detected via well-known manifests

{"Observation: DMARC is currently set to '" + dmarc + "', meaning unauthenticated spoofed mail is not strictly rejected." if dmarc in ("none", "missing") else "Good news: DMARC is enforced with '" + dmarc + "', preventing domain spoofing."}

We packaged this multi-signal scanner as a serverless micro-engine on Apify ($0.001/domain) that pipes directly into Clay and n8n pipelines for continuous monitoring.

Would it be helpful if I shared the full JSON payload and our 1-click n8n cron template?

Best,
Deepak Sheoran
Apify Cloud Data Architect"""

    revops_email = f"""Subject: {company} outbound signals: Email deliverability & mobile stack data

Hi {company} team,

If you're enriching target account lists or monitoring partner domains in Clay, technical infrastructure data is usually expensive and fragmented across $200/mo enterprise SaaS.

We ran {domain} through our bulk protocol & deliverability auditor on Apify:

Key Account Signals Extracted for {domain}:
1. Deliverability Compliance: DMARC is '{dmarc}' | SPF triggers {spf_lookups}/10 DNS lookups
2. Google/Yahoo 2024 Bulk Sender Risk: {"At risk (needs strict DMARC)" if dmarc in ("none", "missing") else "Fully compliant"}
3. Native Mobile App Portfolio: {"Yes (Active deep-links)" if apps_count > 0 else "No deep-links detected"}
4. Technical Security Score: {t6['letter_grade']} ({t6['score']}/100)

Rather than paying $0.05–$0.15 per domain in Clay using multiple waterfall scrapers, this actor runs on Apify's Pay-Per-Event model ($0.001/domain) and streams directly into Clay via standard HTTP API.

Happy to send over our ready-to-import Clay formula recipe and sample dataset if you'd like to test on a batch of 500 accounts.

Best,
Deepak Sheoran
Data Automation Engineer"""

    x_thread = f"""Quick infrastructure teardown on {company} ({domain}):
- Security Posture: {t6['letter_grade']} ({t6['score']}/100)
- SSL Expiration: {ssl_str}
- DMARC Policy: {dmarc} (RFC 7208 lookups: {spf_lookups}/10)
- RFC 9116 security.txt: {sec_txt}
- Deep-linked apps: {apps_count} detected

Built this passive prober as an Apify Actor ($0.001/run) for Clay & n8n tables. Full guide & template: https://apify.com/deepaksheoran172/domain-protocol-signals-enricher"""

    return {"cto_email": cto_email, "revops_email": revops_email, "x_thread": x_thread}


def run_batch(batch_size: int = 5) -> Dict[str, Any]:
    catalog = load_target_catalog()
    total_targets = len(catalog)
    if total_targets == 0:
        print("[!] No target accounts found in catalog!")
        return {"status": "ERROR", "message": "Catalog empty"}

    state = load_state()
    start_idx = state.get("current_index", 0)

    batch_targets = []
    for i in range(batch_size):
        idx = (start_idx + i) % total_targets
        batch_targets.append(catalog[idx])

    timestamp_str = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    print(f"\n[>>>] EXECUTING MARKETING BATCH at {timestamp_str} (Batch Size: {len(batch_targets)} / Total in Catalog: {total_targets})")

    batch_results = []
    for target in batch_targets:
        print(f"  [-] Probing {target['company']} ({target['domain']})...")
        rec = audit_account(target)
        copy = generate_outbound_emails(rec)
        rec["copy"] = copy
        batch_results.append(rec)
        time.sleep(0.3)

    # Save Dispatch Markdown
    dispatch_file = DISPATCH_DIR / f"dispatch_{timestamp_str}.md"
    with open(dispatch_file, "w", encoding="utf-8") as f:
        f.write(f"# Automated B2B Marketing Dispatch: {timestamp_str}\n\n")
        f.write(f"**Batch Size:** {len(batch_results)} Accounts | **Total Catalog Size:** {total_targets} Accounts | **Execution Cost:** $0.00\n\n")
        f.write("## Diagnostic Results Table\n\n")
        f.write("| Company | Domain | Grade | DMARC | SPF Lookups | SSL Days | RFC 9116 | Mobile Apps |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for r in batch_results:
            t6 = r["tool6"]
            t7 = r["tool7"]
            ssl_str = f"{t6['ssl_days']}d" if t6['ssl_days'] is not None else "N/A"
            apps_str = f"{t7['android_apps'] + t7['ios_apps']} apps"
            f.write(f"| **{r['company']}** | `{r['domain']}` | **{t6['letter_grade']}** ({t6['score']}) | `{t6['dmarc']}` | `{t6['spf_lookups']}/10` | {ssl_str} | `{t7['security_txt']}` | {apps_str} |\n")

        f.write("\n---\n\n## ✉️ Ready-to-Send Outbound & Community Copy\n\n")
        for idx, r in enumerate(batch_results, 1):
            f.write(f"### {idx}. {r['company']} ({r['domain']})\n\n")
            f.write("**CTO Persona Email:**\n```text\n" + r["copy"]["cto_email"] + "\n```\n\n")
            f.write("**RevOps Persona Email:**\n```text\n" + r["copy"]["revops_email"] + "\n```\n\n")
            f.write("**X / Social Post:**\n```text\n" + r["copy"]["x_thread"] + "\n```\n\n---\n\n")

    # Update Queue CSV
    file_exists = QUEUE_CSV.exists()
    with open(QUEUE_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for r in batch_results:
            queue_id = f"MQ-{timestamp_str[:8]}-{r['domain'].replace('.', '_')}"
            writer.writerow([
                queue_id,
                datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "domain-protocol-signals-enricher",
                "B2B_COLD_DIAGNOSTIC",
                r["company"],
                f"https://{r['domain']}",
                f"Grade {r['tool6']['letter_grade']} | DMARC: {r['tool6']['dmarc']} | SSL: {r['tool6']['ssl_days']}d",
                "READY_TO_DISPATCH",
                f"Generated in dispatch_{timestamp_str}.md",
            ])

    # Update State
    state["current_index"] = (start_idx + batch_size) % total_targets
    state["total_runs"] += 1
    state["last_run_utc"] = datetime.now(timezone.utc).isoformat()
    state["history"].append({
        "timestamp": timestamp_str,
        "dispatch_file": dispatch_file.name,
        "accounts_audited": [t["domain"] for t in batch_targets],
    })
    save_state(state)

    print(f"[+] Batch completed! Dispatch saved: {dispatch_file.name}")
    print(f"[+] Next batch starts at index {state['current_index']} / {total_targets}")
    return {"status": "SUCCESS", "dispatch_file": str(dispatch_file), "count": len(batch_results)}


def main() -> None:
    parser = argparse.ArgumentParser(description="24/7 Autonomous B2B Marketing & Outbound Daemon")
    parser.add_argument("--run-once", action="store_true", help="Execute single batch immediately and exit")
    parser.add_argument("--batch-size", type=int, default=5, help="Number of accounts per batch")
    parser.add_argument("--interval-hours", type=float, default=3.0, help="Interval between runs in daemon mode")
    parser.add_argument("--daemon", action="store_true", help="Run continuously in background")
    args = parser.parse_args()

    catalog = load_target_catalog()
    print("=" * 65)
    print("  AUTONOMOUS 24/7 B2B MARKETING & COLD OUTBOUND DAEMON")
    print(f"  Target Catalog: {len(catalog)} Top B2B Companies (Database: master_target_companies.csv)")
    print("=" * 65)

    if args.run_once or not args.daemon:
        run_batch(batch_size=args.batch_size)
        return

    interval_secs = int(args.interval_hours * 3600)
    print(f"[*] Running in 24/7 daemon mode. Interval: {args.interval_hours} hours ({interval_secs}s).")
    while True:
        try:
            run_batch(batch_size=args.batch_size)
            print(f"[*] Sleeping for {args.interval_hours} hours until next automated dispatch cycle...")
            time.sleep(interval_secs)
        except KeyboardInterrupt:
            print("\n[!] Daemon stopped by operator.")
            break
        except Exception as exc:
            print(f"\n[!] Error during dispatch cycle: {exc}. Retrying in 60 seconds...")
            time.sleep(60)


if __name__ == "__main__":
    main()
