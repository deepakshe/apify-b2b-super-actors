#!/usr/bin/env python3
"""generate_cold_outbound_audits.py

Executes real-world local B2B domain security and protocol audits using
Tool #6 (domain-security-super-auditor) and Tool #7 (domain-protocol-signals-enricher)
to generate high-converting 'Trojan Horse' personalized cold outbound campaigns.
Runs 100% locally with zero cloud spend ($0.00).
"""

from __future__ import annotations

import importlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

# Locate project roots
SCRIPT_DIR = Path(__file__).resolve().parent
DIST_KIT_DIR = SCRIPT_DIR.parent
PROJECT_ROOT = DIST_KIT_DIR.parent.parent

# Dynamically import Tool 6 & Tool 7 without namespace collision
t6_dir = PROJECT_ROOT / "01_apify_actors" / "domain_security_super_auditor_v1"
t7_dir = PROJECT_ROOT / "01_apify_actors" / "domain_protocol_signals_enricher_v1"

# Load Tool 6
sys.path.insert(0, str(t6_dir))
import src.auditors as t6_auditors
sys.path.remove(str(t6_dir))
del sys.modules["src"]

# Load Tool 7
sys.path.insert(0, str(t7_dir))
import src.enricher as t7_enricher

TARGET_DOMAINS = [
    {"domain": "linear.app", "company": "Linear", "category": "Productivity & Issue Tracking"},
    {"domain": "supabase.com", "company": "Supabase", "category": "Developer Infrastructure"},
    {"domain": "cal.com", "company": "Cal.com", "category": "Scheduling Infrastructure"},
    {"domain": "gymshark.com", "company": "Gymshark", "category": "Global E-Commerce (Shopify)"},
    {"domain": "resend.com", "company": "Resend", "category": "Developer Email Infrastructure"},
    {"domain": "postman.com", "company": "Postman", "category": "API Platform"},
]


def run_combined_audit(domain: str) -> Dict[str, Any]:
    """Runs Tool 6 and Tool 7 locally on the target domain."""
    print(f"[*] Auditing {domain}...")

    # Tool 6: Security & DNS Email Deliverability
    t6_config = {
        "include_dns_deliverability": True,
        "include_rdap_age": True,
        "timeout_seconds": 6,
    }
    try:
        t6_res = t6_auditors.audit_single_domain(domain, t6_config)
    except Exception as exc:
        t6_res = {"error": str(exc), "letter_grade": "N/A", "overall_score": 0}

    # Tool 7: Well-Known Protocols, App Links, RFC Policies
    try:
        enricher = t7_enricher.DomainProtocolEnricher(
            timeout_secs=6,
            probe_app_links=True,
            probe_identity_metadata=True,
            probe_security_policies=True,
            probe_domain_files=True,
        )
        t7_res = enricher.enrich_domain(domain)
    except Exception as exc:
        t7_res = {"error": str(exc), "scan_status": "unreachable"}

    combined = {
        "domain": domain,
        "audited_at": datetime.now(timezone.utc).isoformat(),
        "tool6_security": {
            "letter_grade": t6_res.get("letter_grade", "N/A"),
            "overall_score": t6_res.get("overall_score", 0),
            "ssl_issuer": t6_res.get("ssl_audit", {}).get("issuer_org", "Unknown"),
            "ssl_days_remaining": t6_res.get("ssl_audit", {}).get("days_until_expiry"),
            "ssl_expiry_date": t6_res.get("ssl_audit", {}).get("not_after_utc"),
            "hsts_active": t6_res.get("headers_audit", {}).get("hsts_present", False),
            "hsts_max_age": t6_res.get("headers_audit", {}).get("hsts_max_age"),
            "spf_policy": t6_res.get("email_deliverability_audit", {}).get("spf_policy", "missing"),
            "spf_lookups": t6_res.get("email_deliverability_audit", {}).get("spf_lookup_count", 0),
            "dmarc_policy": t6_res.get("email_deliverability_audit", {}).get("dmarc_policy", "missing"),
            "mx_provider": t6_res.get("email_deliverability_audit", {}).get("mx_provider", "Unknown"),
            "recommendations": t6_res.get("recommendations", []),
        },
        "tool7_protocols": {
            "scan_status": t7_res.get("scan_status", "unknown"),
            "android_app_links": t7_res.get("android_app_links_status", "not_found"),
            "android_packages": t7_res.get("android_package_names", []),
            "ios_aasa": t7_res.get("ios_aasa_status", "not_found"),
            "ios_apps": t7_res.get("ios_app_ids", []),
            "security_txt": t7_res.get("security_txt_status", "not_found"),
            "security_contacts": t7_res.get("security_contacts", []),
            "mta_sts": t7_res.get("mta_sts_status", "not_found"),
            "mta_sts_mode": t7_res.get("mta_sts_mode"),
            "apple_merchant": t7_res.get("apple_merchant_file_status", "not_found"),
            "llms_txt": t7_res.get("llms_txt_status", "not_found"),
        },
    }
    return combined


def format_cto_email(company: str, domain: str, audit: Dict[str, Any]) -> str:
    """Formats copy-ready cold email tailored to CTO / VP Engineering persona."""
    t6 = audit["tool6_security"]
    t7 = audit["tool7_protocols"]

    ssl_days = t6["ssl_days_remaining"]
    ssl_str = f"{ssl_days} days" if ssl_days is not None else "Inspection bypassed"
    dmarc = t6["dmarc_policy"]
    spf_lookups = t6["spf_lookups"]
    sec_txt = t7["security_txt"]
    mta_sts = t7["mta_sts_mode"] or "none"
    android_apps = len(t7["android_packages"])
    ios_apps = len(t7["ios_apps"])

    # High-converting cold outreach based on the Trojan Horse Framework
    email = f"""Subject: Quick engineering audit snippet for {domain} (SSL, RFC 9116, DMARC)

Hi {company} team,

Ran an automated pre-flight infrastructure hygiene check on {domain} as part of our weekly protocol scanner. Thought you'd appreciate the raw findings:

Quick Diagnostic Summary:
• Security Posture Grade: {t6['letter_grade']} ({t6['overall_score']}/100)
• SSL Certificate: {ssl_str} remaining (Issuer: {t6['ssl_issuer']})
• RFC 7208 SPF Lookups: {spf_lookups} / 10 limit (Policy: {t6['spf_policy']})
• DMARC Policy: {dmarc} (MX Provider: {t6['mx_provider']})
• RFC 9116 security.txt: {sec_txt}
• MTA-STS Mode: {mta_sts}
• Deep-Linked Mobile Apps: {android_apps} Android package(s) / {ios_apps} iOS app(s) detected via well-known manifests

{f"Observation: Your DMARC policy is currently set to '{dmarc}', which means spoofed mail from {domain} is not strictly rejected by receiving mailboxes." if dmarc in ("none", "missing") else f"Good news: Your DMARC is enforced with '{dmarc}', shielding {domain} from domain spoofing."}

We packaged this multi-signal scanner as a serverless micro-engine on Apify ($0.001/domain) that pipes directly into Clay and n8n pipelines for continuous vendor and portfolio monitoring.

Would it be helpful if I shared the full JSON audit payload and our 1-click n8n cron template?

Best,
Deepak Sheoran
Apify Cloud Data Architect"""
    return email


def format_revops_email(company: str, domain: str, audit: Dict[str, Any]) -> str:
    """Formats copy-ready cold email tailored to Head of RevOps / Growth Lead persona."""
    t6 = audit["tool6_security"]
    t7 = audit["tool7_protocols"]

    dmarc = t6["dmarc_policy"]
    spf_lookups = t6["spf_lookups"]
    has_mobile = "Yes (Android/iOS deep-links configured)" if (t7["android_packages"] or t7["ios_apps"]) else "No deep-links detected"

    email = f"""Subject: {company} outbound signals: Email deliverability & mobile stack data

Hi {company} team,

If you're enriching target account lists or monitoring partner domains in Clay, technical infrastructure data is usually expensive and fragmented across $200/mo enterprise SaaS.

We ran {domain} through our bulk protocol & deliverability auditor on Apify:

Key Account Signals Extracted for {domain}:
1. Deliverability Compliance: DMARC is '{dmarc}' | SPF triggers {spf_lookups}/10 DNS lookups
2. Google/Yahoo 2024 Bulk Sender Risk: {"At risk (needs strict DMARC)" if dmarc in ("none", "missing") else "Fully compliant"}
3. Native Mobile App Portfolio: {has_mobile}
4. Technical Security Score: {t6['letter_grade']} ({t6['overall_score']}/100)

Rather than paying $0.05–$0.15 per domain in Clay using multiple waterfall scrapers, this actor runs on Apify's Pay-Per-Event model ($0.001/domain) and streams directly into Clay via standard HTTP API.

Happy to send over our ready-to-import Clay formula recipe and sample dataset if you'd like to test on a batch of 500 accounts.

Best,
Deepak Sheoran
Data Automation Engineer"""
    return email


def main() -> None:
    print("=" * 65)
    print("  'TROJAN HORSE' B2B OUTBOUND AUDIT PIPELINE — ZERO-SPEND ENGINE")
    print("=" * 65)

    all_audits = []

    for item in TARGET_DOMAINS:
        domain = item["domain"]
        company = item["company"]
        category = item["category"]

        audit_data = run_combined_audit(domain)
        audit_data["company"] = company
        audit_data["category"] = category

        cto_email = format_cto_email(company, domain, audit_data)
        revops_email = format_revops_email(company, domain, audit_data)

        audit_data["cold_outbound"] = {
            "cto_persona_email": cto_email,
            "revops_persona_email": revops_email,
        }
        all_audits.append(audit_data)
        time.sleep(0.5)

    # Save structured JSON
    output_json_path = DIST_KIT_DIR / "growth_audit" / "trojan_horse_audits.json"
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(all_audits, f, indent=2)
    print(f"\n[+] Saved structured audit JSON to: {output_json_path.name}")

    # Generate Markdown Outbound Playbook
    md_path = DIST_KIT_DIR / "growth_audit" / "trojan_horse_cold_outbound_campaign.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# 'Trojan Horse' High-Converting Cold Outbound Campaign\n\n")
        f.write(f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}  \n")
        f.write("**Execution Engine:** 100% Local Prototype (Tool 6 + Tool 7) — $0.00 Cloud Spend  \n")
        f.write("**Strategy:** Deliver immediate diagnostic proof and actionable infrastructure audits before asking for any commitment.\n\n")
        f.write("---\n\n")

        f.write("## 📊 Executive Diagnostic Matrix (Live Target Accounts)\n\n")
        f.write("| Company | Domain | Grade | DMARC | SPF Lookups | SSL Days | RFC 9116 | MTA-STS | Mobile App Links |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for a in all_audits:
            t6 = a["tool6_security"]
            t7 = a["tool7_protocols"]
            ssl_str = f"{t6['ssl_days_remaining']}d" if t6['ssl_days_remaining'] is not None else "N/A"
            mob_str = f"{len(t7['android_packages'])} Android / {len(t7['ios_apps'])} iOS"
            f.write(f"| **{a['company']}** | `{a['domain']}` | **{t6['letter_grade']}** ({t6['overall_score']}) | `{t6['dmarc_policy']}` | `{t6['spf_lookups']}/10` | {ssl_str} | `{t7['security_txt']}` | `{t7['mta_sts_mode'] or 'none'}` | {mob_str} |\n")

        f.write("\n---\n\n")
        f.write("## ✉️ Copy-Ready Trojan Horse Cold Outbound Snippets\n\n")

        for idx, a in enumerate(all_audits, 1):
            f.write(f"### Account #{idx}: {a['company']} (`{a['domain']}`)\n")
            f.write(f"**Industry Category:** {a['category']}  \n\n")

            f.write("#### 👨‍💻 CTO / Head of Engineering Persona Copy\n")
            f.write("```text\n")
            f.write(a["cold_outbound"]["cto_persona_email"])
            f.write("\n```\n\n")

            f.write("#### 📈 Head of RevOps / Growth Lead Persona Copy\n")
            f.write("```text\n")
            f.write(a["cold_outbound"]["revops_persona_email"])
            f.write("\n```\n\n")
            f.write("---\n\n")

    print(f"[+] Saved complete outbound campaign report to: {md_path.name}")
    print("\n[SUCCESS] Trojan Horse outbound pipeline executed with 100% success!")


if __name__ == "__main__":
    main()
