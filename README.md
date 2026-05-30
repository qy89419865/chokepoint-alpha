# Chokepoint Alpha

Chokepoint Alpha is a Codex skill for traceable A-share and Hong Kong stock industrial chokepoint research.

It helps screen and document candidates through:

- trend exposure
- industrial bottleneck strength
- company validation
- market mispricing
- explicit risk penalties
- auditable thesis cards

The skill is designed for investment research engineering, not stock recommendation. It does not output buy, sell, hold, target price, or position sizing conclusions.

Allowed conclusions are:

- `值得深研`
- `观察`
- `暂不研究`

## Install

Clone or copy this folder into your Codex skills directory:

```bash
~/.codex/skills/chokepoint-alpha
```

Then invoke:

```text
Use $chokepoint-alpha to evaluate 301291.SZ
```

## Standalone Script

```bash
python scripts/score_candidates.py --input candidates.csv --output reports/chokepoint_report.md
```

Missing fields must be written as `unknown`. Theme keyword matches are candidate recall signals only, not bottleneck evidence.

