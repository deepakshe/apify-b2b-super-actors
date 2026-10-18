# Messy Supplier CSV → Clean Shopify Product CSV

**In one line:** Upload any supplier or vendor product sheet. Get a clean Shopify import file, plus a report of exactly which rows were bad and why.

## Who is this for
- **Shopify agencies and store managers** who get product sheets from suppliers in random formats.
- **Catalog / data-entry freelancers** who fix prices, variants and duplicate SKUs by hand.

## What you give
Either paste the CSV text into `rawCsv`, or give a link:
```json
{ "csvUrl": "https://example.com/supplier_feed.csv", "defaultVendor": "Your Brand", "defaultStatus": "active" }
```

## What you get (real test on a sample messy file)
- 9 rows read → **6 clean Shopify rows**, 3 rejected, with the reason for each one:
  - Row 6: Missing required 'Title'
  - Row 7: Malformed price value: 'N/A'
  - Row 8: Price cannot be negative: '-25.00'
- 1 duplicate SKU flagged. Prices like `"$ 1,299.00"` are cleaned to `1299.00`. Size and colour become Shopify Option1/Option2.

## Price
- $0.05 per file + $0.0005 per product
- 1,000 products ≈ **$0.55**.

## How to use (3 steps)
1. Open https://apify.com/deepaksheoran172/catalog-feed-normalizer and click **Try for free**.
2. Paste your CSV into `rawCsv`, or a public link into `csvUrl`.
3. Click **Start**, download the Shopify CSV, and fix only the rows listed in the report.

## What it does NOT do
- It does not upload to Shopify for you. You import the CSV yourself.
- It does not write product descriptions or translate them.
