# OpenRouter Model Prices + MCP Server List (as a dataset)

**In one line:** Get every OpenRouter model, with its price per 1M tokens, context size and free/vision flags, as a clean table you can filter. Optionally add a list of MCP servers.

## Who is this for
- **AI app / agent builders** who need to pick the cheapest model that fits a context size.
- **AI gateway or dashboard builders** who need model prices in their own database.

## What you give
```json
{ "mode": "models", "free_only": false, "multimodal_only": false, "min_context": 128000 }
```
`mode`: `models`, `mcp`, or `both`.

## What you get (real run, 2026-10-18)
- **471 models**, 19 of them free. Each row has `model_id`, `name`, `context_length`, `pricing_prompt_1m`, `pricing_completion_1m`, `is_free`, `is_multimodal`.
- Example: `x-ai/grok-4.20`: context 2,000,000, $1.25 per 1M input, $2.50 per 1M output, multimodal.
- If a model's price is missing or broken, it is marked `pricing_status: UNKNOWN`. We never guess it.

## Price
- $0.01 per run + $0.001 per model
- A full catalog of 471 models costs about **$0.48**. With `free_only: true` it is a few cents.

## How to use (3 steps)
1. Open https://apify.com/deepaksheoran172/openrouter-mcp-registry and click **Try for free**.
2. Set `mode` to `models` and your filters.
3. Click **Start**. Use the dataset API URL in your app, or schedule it daily so your prices stay current.

## What it does NOT do
- The MCP part is a small curated list (5 servers), not the full official registry.
- It does not call or benchmark the models.
