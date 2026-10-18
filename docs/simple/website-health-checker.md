# Website Broken Link & Health Checker

**In one line:** Give it one website. It crawls the pages and lists every broken link (404/500), redirect, and page error, with the page where each one was found.

## Who is this for
- **SEO agencies and freelancers**: fast technical check before a client audit or a monthly report.
- **Web agencies**: check a site after a redesign or migration before you hand it over.

## What you give
```json
{ "startUrl": "https://yourclient.com", "maxPages": 20 }
```

## What you get (real output, scanned on 2026-10-18)
- noa.agency: crawled 19 pages, checked 146 links, **1 broken**: `/caso-studio-e-commerce-calzature-raf-brand/` → 404
- theplanetsoft.com: crawled 25 pages, checked 584 links, 0 broken

Each row shows: the broken URL, its status code, the page that links to it, and the redirect chain.

## Price
- $0.001 per URL checked, $0.002 per page deep-audited
- A 20-page site with ~150 links costs about **$0.20**.

## How to use (3 steps)
1. Open https://apify.com/deepaksheoran172/website-health-checker and click **Try for free**.
2. Put the homepage in `startUrl`. Start with `maxPages: 20`.
3. Click **Start** and download the list of broken links.

## What it does NOT do
- Some sites block bots (Cloudflare and similar). In our test, 3 of 10 sites blocked the crawl. When that happens you get no findings. It does not invent any.
- It does not measure page speed or Core Web Vitals.
