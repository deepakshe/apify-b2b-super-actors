# Shopify / WooCommerce Product Export + 301 Redirect Map

**In one line:** Give it a store URL. Get every product as a Shopify-ready import CSV, plus a 301 redirect map from the old URLs to the new ones.

## Who is this for
- **Agencies migrating a store** from WooCommerce to Shopify (or Shopify to Shopify).
- **Freelancers** who are tired of copy-pasting products and building redirect sheets by hand.

## What you give
```json
{ "platform": "woocommerce", "storeUrl": "https://old-store.com", "maxPages": 5 }
```
`platform` can be `woocommerce` or `shopify`. `storeUrl` is the public store address. You do not need admin access.

## What you get (real test, 2026-10-18)
We ran it on allbirds.com with a 25-product limit and got **25 products → 302 Shopify CSV rows** (one row per variant), in Shopify's exact import format: Handle, Title, Body (HTML), Vendor, Option1/2/3, Variant SKU, Price, Image Src…
When the old URL paths are different from Shopify's `/products/<handle>`, you also get a `Redirect from,Redirect to` CSV that you can import in Shopify admin (URL Redirects → Import).

## Price
- $0.05 per store run + $0.001 per product exported
- A 500-product store costs about **$0.55**.

## How to use (3 steps)
1. Open https://apify.com/deepaksheoran172/store-catalog-redirect-extractor and click **Try for free**.
2. Pick the `platform` and paste the `storeUrl`.
3. Click **Start**, then download the products CSV and the redirects CSV and import both into Shopify.

## What it does NOT do
- It only reads public product data: no customers, orders or private products.
- If the store hides its product API, there is nothing to extract.
- Shopify → Shopify with the same paths gives an empty redirect file. That is expected, because nothing needs redirecting.
