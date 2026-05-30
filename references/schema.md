# Schema

## Core Fields

Use these fields for each candidate row. Missing values must be `unknown`.

- `ticker`
- `name`
- `market`
- `exchange`
- `industry`
- `market_cap`
- `theme_tags`
- `main_business`
- `bottleneck_thesis`
- `bottleneck_segment`
- `supply_tightness_reason`
- `substitution_difficulty`
- `downstream_customers_or_applications`
- `existing_evidence`
- `financial_validation`
- `valuation_market_cap_mismatch`
- `major_risks`
- `manual_check_questions`
- `source`
- `data_quality`
- `updated_at`

For each non-audit field, add optional trace columns:

- `<field>_source`
- `<field>_as_of_date`
- `<field>_quality`

## Scores

Direct dimension scores:

- `trend_exposure_score`: 0-25
- `bottleneck_score`: 0-30
- `company_validation_score`: 0-25
- `mispricing_score`: 0-20
- `risk_penalty`: 0-30

Formula:

```text
total_score = trend_exposure_score
            + bottleneck_score
            + company_validation_score
            + mispricing_score
            - risk_penalty
```

Priority mapping:

- `total_score >= 75`: `值得深研`
- `60 <= total_score < 75`: `值得深研`
- `45 <= total_score < 60`: `观察`
- `total_score < 45`: `暂不研究`
- Low evidence coverage: downgrade to `观察` or `暂不研究`.

## Thesis Card Format

```text
股票代码：
股票名称：
市场：A 股 / 港股
行业：
市值：
主题标签：
瓶颈 thesis：
它卡住的是产业链哪一环：
为什么这个环节可能供给紧张：
替代难度：
下游客户/应用场景：
已有证据：
财务验证：
估值与市值错配：
主要风险：
需要人工进一步核查的问题：
数据缺失项：
信心等级：High / Medium / Low
结论：值得深研 / 观察 / 暂不研究
```
