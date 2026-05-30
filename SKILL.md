---
name: chokepoint-alpha
description: Research A-share and Hong Kong-listed stocks using an industrial chokepoint alpha framework. Use when the user asks to screen A/H stocks for "产业链瓶颈", small-cap mismatch, trend exposure, bottleneck thesis cards, auditable research reports, or to evaluate a ticker without producing buy/sell/target-price recommendations.
---

# Chokepoint Alpha

Use this skill to evaluate A 股 / 港股 companies through a traceable "大产业趋势 + 供给瓶颈 + 公司验证 + 市场错配 - 风险惩罚" framework.

## Non-Negotiables

- Do not give buy, sell, hold, target price, position sizing, or certainty language.
- Output only research priority: `值得深研`, `观察`, or `暂不研究`.
- Mark unavailable fields as `unknown`; do not impute, backfill, or invent.
- Preserve source, date, and quality for every data field when building datasets.
- Treat theme keyword matches as candidate recall only, not bottleneck evidence.
- For current market data, recent filings, or company facts, verify with fresh sources before scoring.

## Workflow

1. Normalize ticker and market.
   - A 股: `000001.SZ`, `600000.SH`, `430000.BJ`.
   - 港股: `0700.HK`; pad numeric HK tickers to four digits.
2. Gather evidence.
   - Prefer official filings, exchange disclosures, company annual reports, and primary announcements.
   - Use AkShare/Tushare/yfinance only as configurable data sources; note coverage and quality limits.
   - Use third-party pages only with `third_party_snapshot` quality.
3. Build a candidate row.
   - Required fields and scoring details are in `references/schema.md`.
   - If using a workspace project that has `python -m src.main`, prefer that CLI.
   - Otherwise use `scripts/score_candidates.py` for a standalone CSV-to-report path.
4. Score with the framework.
   - `total_score = trend_exposure_score + bottleneck_score + company_validation_score + mispricing_score - risk_penalty`
   - Apply risk penalties aggressively when financial verification is weak, recent gains are excessive, cash flow is poor, or the thesis is only a concept story.
5. Generate thesis cards and report.
   - Include data gaps and manual verification questions.
   - Keep conclusions to `值得深研 / 观察 / 暂不研究`.

## Preferred Workspace CLI

If the current workspace contains this project structure, use:

```bash
python -m src.main fetch --market A
python -m src.main screen --market A --theme power_equipment --top 50
python -m src.main research --ticker 301291.SZ
python -m src.main report --market A --theme power_equipment --format markdown
```

For local CSV-only research, create a data config that points `local_csv.path` at the CSV and run the same CLI. Do not run `fetch` and `screen/research` in parallel because `screen` reads processed files written by `fetch`.

## Standalone Script

Use `scripts/score_candidates.py` when the project CLI is unavailable:

```bash
python scripts/score_candidates.py --input candidates.csv --output reports/chokepoint_report.md
```

The input CSV should contain direct dimension scores and thesis-card fields from `references/schema.md`. The script does not fetch data and does not invent missing fields.

## References

- Read `references/schema.md` when creating candidate CSV rows or thesis cards.
- Read `references/guardrails.md` when deciding whether a theme is a true bottleneck or just concept exposure.
