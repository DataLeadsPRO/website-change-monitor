# Website Change Monitor API

> Track page and price changes over time: diffs, history, and alerts through simple tracking endpoints.

Part of the **DataLeads** API suite (Monitoring category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/diff` | V1 Diff |
| POST | `/track/register` | V1 Track Register |
| POST | `/track/check` | V1 Track Check |
| POST | `/track/history` | V1 Track History |
| POST | `/price/track` | V1 Price Track |

## Quick start

```bash
curl -X POST https://data.dataleads.pro/v1/diff \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "url": "https://example.com"}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://data.dataleads.pro](https://data.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://data.dataleads.pro/mcp/website-change-monitor`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/website-change-monitor-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://data.dataleads.pro](https://data.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
