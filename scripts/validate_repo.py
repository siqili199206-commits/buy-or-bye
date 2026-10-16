#!/usr/bin/env python3
"""Dependency-free structural checks for the Buy or Bye skill repository."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def main() -> int:
    skill_path = ROOT / "SKILL.md"
    require(skill_path.exists(), "SKILL.md is missing")
    if not skill_path.exists():
        return finish()

    skill = skill_path.read_text(encoding="utf-8")
    require(skill.startswith("---\n"), "SKILL.md must start with YAML front matter")
    frontmatter = skill.split("---", 2)[1] if skill.count("---") >= 2 else ""
    require(re.search(r"(?m)^name:\s*buy-or-bye\s*$", frontmatter) is not None, "Skill name must be buy-or-bye")
    require(re.search(r"(?m)^description:\s*\S.+$", frontmatter) is not None, "Skill description is missing")

    links = re.findall(r"\]\((references/[^)]+)\)", skill)
    require(bool(links), "SKILL.md should link to supporting references")
    for relative in links:
        require((ROOT / relative).is_file(), f"Missing referenced file: {relative}")

    for required in (
        "README.md",
        "README_EN.md",
        "LICENSE",
        "agents/openai.yaml",
        "references/decision-framework.md",
        "references/output-contract.md",
        "references/calibration-cases.md",
        "assets/running-shoes-decision-card.png",
        "assets/running-shoes-decision-card.svg",
        "evals/prompts.csv",
    ):
        require((ROOT / required).is_file(), f"Missing required repository file: {required}")

    openai_yaml = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    require("allow_implicit_invocation: true" in openai_yaml, "Implicit invocation policy changed unexpectedly")
    require("$buy-or-bye" in openai_yaml, "Default prompt must explicitly invoke $buy-or-bye")

    eval_path = ROOT / "evals/prompts.csv"
    if eval_path.exists():
        with eval_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
        require(len(rows) >= 10, "Evaluation set should contain at least 10 prompts")
        require(any(row.get("should_trigger") == "true" for row in rows), "Evaluation set needs positive cases")
        require(any(row.get("should_trigger") == "false" for row in rows), "Evaluation set needs negative controls")
        require(all(row.get("expected_behavior", "").strip() for row in rows), "Every evaluation needs expected behavior")

    text_files = [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]
    for path in text_files:
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        scaffold_marker = "[TO" + "DO"
        require(scaffold_marker not in content, f"Unfinished scaffold marker in {path.relative_to(ROOT)}")

    return finish()


def finish() -> int:
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Buy or Bye repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
