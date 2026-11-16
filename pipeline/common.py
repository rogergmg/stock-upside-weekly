"""Shared paths and helpers for the weekly pipeline."""
import json
import sys
from datetime import datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RESEARCH = ROOT / "research"
SITE = ROOT / "site"
sys.path.insert(0, str(ROOT / "engine"))

NY = ZoneInfo("America/New_York")
USER_CUTOFF_USD = 50_000_000_000      # user filter: strictly above $50B (skill floor is $20B)
PREFILTER_USD = 40_000_000_000        # screener prefilter, generous so intraday moves don't drop names
CAP_BAND = 0.02                       # +/-2% cap bounds: share counts can lag the close date
UNIVERSE_NAME = "US-listed equities (NYSE, Nasdaq, NYSE American) with whole-company market cap > US$50B"


def read(path):
    return json.loads(Path(path).read_text())


def write(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, allow_nan=False, default=str) + "\n")


def latest(folder):
    files = sorted(Path(folder).glob("*.json"))
    if not files:
        raise SystemExit(f"no files in {folder}")
    return files[-1]


def reference_session(now=None):
    """Latest completed regular US session date (weekends skipped; holidays resolved by price history)."""
    now = (now or datetime.now(NY)).astimezone(NY)
    day = now.date()
    if now.time() < time(16, 15):
        day -= timedelta(days=1)
    while day.weekday() >= 5:
        day -= timedelta(days=1)
    return day
