#!/usr/bin/env python3
"""target_catalog_manager.py

Scalable Target B2B Companies Database Manager.
Manages ingestion, deduplication, categorization, and expansion to thousands of domains.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path
from typing import Dict, List, Set

SCRIPT_DIR = Path(__file__).resolve().parent
DIST_KIT_DIR = SCRIPT_DIR.parent
CSV_PATH = DIST_KIT_DIR / "growth_audit" / "master_target_companies.csv"

DOMAIN_REGEX = re.compile(r"^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$")


def load_catalog() -> List[Dict[str, str]]:
    if not CSV_PATH.exists():
        return []
    records = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records


def print_stats() -> None:
    catalog = load_catalog()
    total = len(catalog)
    print("=" * 65)
    print(f"  MASTER B2B TARGET COMPANIES CATALOG: {total} ENTERPRISE DOMAINS")
    print("=" * 65)

    categories: Dict[str, int] = {}
    tiers: Dict[str, int] = {}

    for r in catalog:
        cat = r.get("category", "Uncategorized")
        categories[cat] = categories.get(cat, 0) + 1
        tier = r.get("tier", "Unknown")
        tiers[tier] = tiers.get(tier, 0) + 1

    print("\n[-] Category Breakdown:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        bar = "#" * (count // 3)
        print(f"  * {cat:<32} : {count:>3} accounts {bar}")

    print("\n[*] Tier Allocation:")
    for tier, count in sorted(tiers.items()):
        print(f"  * {tier:<15} : {count} accounts")

    print(f"\n[+] Database File: {CSV_PATH.resolve()}")
    print("=" * 65)


def add_domains_from_file(file_path: Path, default_category: str = "B2B SaaS & Enterprise", default_tier: str = "Tier-2") -> int:
    if not file_path.exists():
        print(f"[!] File not found: {file_path}")
        return 0

    catalog = load_catalog()
    existing_domains: Set[str] = {r["domain"].lower() for r in catalog}

    new_records = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            raw = line.strip().lower()
            if not raw or raw.startswith("#"):
                continue
            # Extract domain from URLs if provided
            raw = re.sub(r"^https?://", "", raw).split("/")[0].split(":")[0]
            if raw in existing_domains or not DOMAIN_REGEX.match(raw):
                continue

            company_name = raw.split(".")[0].capitalize()
            new_records.append({
                "domain": raw,
                "company": company_name,
                "category": default_category,
                "priority": "P2",
                "tier": default_tier,
            })
            existing_domains.add(raw)

    if new_records:
        file_exists = CSV_PATH.exists()
        with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["domain", "company", "category", "priority", "tier"])
            if not file_exists:
                writer.writeheader()
            for rec in new_records:
                writer.writerow(rec)

    print(f"[+] Successfully added {len(new_records)} new unique domains! Total now: {len(catalog) + len(new_records)}")
    return len(new_records)


def main() -> None:
    parser = argparse.ArgumentParser(description="Target Catalog Manager")
    parser.add_argument("--stats", action="store_true", help="Display catalog stats")
    parser.add_argument("--add-file", type=Path, help="Path to text or CSV file containing domains to import")
    parser.add_argument("--category", type=str, default="B2B SaaS & Enterprise", help="Category for imported domains")
    parser.add_argument("--tier", type=str, default="Tier-2", help="Tier for imported domains")
    args = parser.parse_args()

    if args.add_file:
        add_domains_from_file(args.add_file, default_category=args.category, default_tier=args.tier)
    else:
        print_stats()


if __name__ == "__main__":
    main()
