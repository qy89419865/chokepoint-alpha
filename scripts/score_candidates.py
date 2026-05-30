#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

UNKNOWN = "unknown"

CARD_FIELDS = [
    ("股票代码", "ticker"),
    ("股票名称", "name"),
    ("市场", "market"),
    ("行业", "industry"),
    ("市值", "market_cap"),
    ("主题标签", "theme_tags"),
    ("瓶颈 thesis", "bottleneck_thesis"),
    ("它卡住的是产业链哪一环", "bottleneck_segment"),
    ("为什么这个环节可能供给紧张", "supply_tightness_reason"),
    ("替代难度", "substitution_difficulty"),
    ("下游客户/应用场景", "downstream_customers_or_applications"),
    ("已有证据", "existing_evidence"),
    ("财务验证", "financial_validation"),
    ("估值与市值错配", "valuation_market_cap_mismatch"),
    ("主要风险", "major_risks"),
    ("需要人工进一步核查的问题", "manual_check_questions"),
    ("数据缺失项", "missing_data_items"),
    ("信心等级", "confidence_level"),
    ("结论", "conclusion"),
]

SCORE_FIELDS = [
    "trend_exposure_score",
    "bottleneck_score",
    "company_validation_score",
    "mispricing_score",
    "risk_penalty",
]


def norm(value: Any) -> str:
    if value is None:
        return UNKNOWN
    text = str(value).strip()
    return text if text else UNKNOWN


def as_float(value: Any) -> float | None:
    text = norm(value)
    if text == UNKNOWN:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def score(row: dict[str, str]) -> dict[str, str]:
    trend = as_float(row.get("trend_exposure_score"))
    bottleneck = as_float(row.get("bottleneck_score"))
    validation = as_float(row.get("company_validation_score"))
    mispricing = as_float(row.get("mispricing_score"))
    penalty = as_float(row.get("risk_penalty"))

    known = [value for value in [trend, bottleneck, validation, mispricing, penalty] if value is not None]
    if not known or all(value is None for value in [trend, bottleneck, validation, mispricing]):
        total = UNKNOWN
    else:
        total = round((trend or 0) + (bottleneck or 0) + (validation or 0) + (mispricing or 0) - (penalty or 0), 2)

    coverage = round(len(known) / 5, 2)
    if total == UNKNOWN:
        conclusion = "暂不研究"
        priority = "insufficient_data"
    elif coverage < 0.4:
        conclusion = "观察"
        priority = "watchlist_needs_evidence"
    elif total >= 60:
        conclusion = "值得深研"
        priority = "priority_follow_up"
    elif total >= 45:
        conclusion = "观察"
        priority = "priority_watchlist"
    else:
        conclusion = "暂不研究"
        priority = "low_priority"

    missing = [field for field in SCORE_FIELDS if norm(row.get(field)) == UNKNOWN]
    card_fields = [
        "theme_tags",
        "bottleneck_thesis",
        "bottleneck_segment",
        "supply_tightness_reason",
        "substitution_difficulty",
        "downstream_customers_or_applications",
        "existing_evidence",
        "financial_validation",
        "valuation_market_cap_mismatch",
        "major_risks",
        "manual_check_questions",
    ]
    missing.extend(field for field in card_fields if norm(row.get(field)) == UNKNOWN)

    result = dict(row)
    result["total_score"] = str(total)
    result["score_coverage"] = str(coverage)
    result["research_priority"] = priority
    result["missing_data_items"] = "、".join(missing) if missing else "none"
    result["confidence_level"] = "High" if coverage >= 0.75 else "Medium" if coverage >= 0.4 else "Low"
    result["conclusion"] = conclusion
    return result


def build_card(row: dict[str, str]) -> str:
    name = norm(row.get("name"))
    ticker = norm(row.get("ticker"))
    lines = [f"## {name}（{ticker}）", ""]
    for label, key in CARD_FIELDS:
        lines.append(f"{label}：{norm(row.get(key))}")
    lines.extend(
        [
            "",
            f"total_score：{norm(row.get('total_score'))}",
            f"research_priority：{norm(row.get('research_priority'))}",
            f"score_coverage：{norm(row.get('score_coverage'))}",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    with input_path.open("r", encoding="utf-8-sig", newline="") as file:
        rows = [score(row) for row in csv.DictReader(file)]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cards = "\n\n".join(build_card(row) for row in rows)
    output_path.write_text(
        "# Industrial Chokepoint Thesis Cards\n\n"
        "This report is for research priority only, not investment advice.\n\n"
        + cards
        + "\n",
        encoding="utf-8",
    )
    print(f"wrote {len(rows)} cards to {output_path}")


if __name__ == "__main__":
    main()
