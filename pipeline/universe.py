#!/usr/bin/env python3
"""Download all US listings from the Nasdaq screener and keep candidates above the prefilter."""
import re
from datetime import datetime, timezone

import requests

from common import DATA, PREFILTER_USD, write

URL = "https://api.nasdaq.com/api/screener/stocks"
SKIP = re.compile(r"(preferred|depositary shares,? each representing|notes due|warrant|units?\b|rights?\b|debenture)", re.I)


def main():
    r = requests.get(URL, params={"tableonly": "true", "limit": "10000", "download": "true"},
                     headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"}, timeout=90)
    r.raise_for_status()
    rows = r.json()["data"]["rows"]
    out = []
    for x in rows:
        try:
            cap = float(x["marketCap"] or 0)
        except ValueError:
            continue
        if cap <= PREFILTER_USD or "^" in x["symbol"] or SKIP.search(x["name"]):
            continue
        out.append(dict(symbol=x["symbol"], yf_symbol=x["symbol"].replace("/", "-"), name=x["name"],
                        country=x["country"], sector=x["sector"], industry=x["industry"],
                        screener_cap_usd=cap))
    out.sort(key=lambda x: -x["screener_cap_usd"])
    write(DATA / "universe.json", dict(source=URL, retrieved_at=datetime.now(timezone.utc).isoformat(),
                                        listings_total=len(rows), prefilter_usd=PREFILTER_USD, candidates=out))
    print(f"{len(rows)} listings, {len(out)} candidates above ${PREFILTER_USD/1e9:.0f}B")


if __name__ == "__main__":
    main()
