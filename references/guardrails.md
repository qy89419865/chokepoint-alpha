# Guardrails

## Avoid Concept Hype

Do not treat theme exposure as a bottleneck. A company needs evidence such as:

- Long customer certification cycles
- Long supply expansion cycle
- Scarce competitors
- Capacity, material, equipment, qualification, patent, or process constraints
- Customer lock-in, long-term contracts, prepayments, strategic investment, or acquisition interest
- Financial or operating validation: revenue growth, margin resilience, cash flow, capex, R&D, order book, or capacity announcements

If evidence is mainly keywords, investor presentation language, or a hot concept, lower `bottleneck_score` and increase `risk_penalty`.

## Avoid Survivor Bias

- Preserve `listing_status` when available.
- Record `as_of_date`; do not use future data for historical screening.
- Note when a sample is manually selected rather than full-market scanned.
- Include ST, delisted, suspended, or weak companies when doing historical backtests.

## Risk Penalty Cues

Penalize for:

- 12-month price move already excessive
- Concept story without financial validation
- Gross margin deterioration
- Weak or negative operating cash flow
- Customer concentration
- Shareholder pledge or reduction
- Frequent private placements or dilution
- Goodwill, inventory, or receivable abnormality
- Abnormal audit opinion, filing delay, or regulatory inquiry
- Low liquidity that makes real execution difficult

## Output Discipline

Use cautious language. Prefer:

- `值得深研`: enough evidence for deeper research
- `观察`: promising but missing proof or high risk
- `暂不研究`: does not fit the framework or risk overwhelms thesis

Never output investment advice.
