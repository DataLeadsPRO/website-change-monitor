import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://data.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('Website Change Monitor API')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "diff",
    "method": "POST",
    "path": "/diff",
    "description": "V1 Diff"
  },
  {
    "name": "track_register",
    "method": "POST",
    "path": "/track/register",
    "description": "V1 Track Register"
  },
  {
    "name": "track_check",
    "method": "POST",
    "path": "/track/check",
    "description": "V1 Track Check"
  },
  {
    "name": "track_history",
    "method": "POST",
    "path": "/track/history",
    "description": "V1 Track History"
  },
  {
    "name": "price_track",
    "method": "POST",
    "path": "/price/track",
    "description": "V1 Price Track"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
