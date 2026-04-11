"""Session-scoped fixtures for the Engineer Impact Framework test suite."""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Root of the aieos-engineer-impact project."""
    return Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def docs_root(project_root: Path) -> Path:
    return project_root / "docs"


# --- Raw file content fixtures ---


@pytest.fixture(scope="session")
def framework_content(docs_root: Path) -> str:
    return (docs_root / "framework.md").read_text()


@pytest.fixture(scope="session")
def process_guide_content(docs_root: Path) -> str:
    return (docs_root / "process-guide.md").read_text()


@pytest.fixture(scope="session")
def integration_content(docs_root: Path) -> str:
    return (docs_root / "aieos-integration.md").read_text()


@pytest.fixture(scope="session")
def contribution_rubric_content(docs_root: Path) -> str:
    return (docs_root / "rubrics" / "contribution-factor.md").read_text()


@pytest.fixture(scope="session")
def complexity_rubric_content(docs_root: Path) -> str:
    return (docs_root / "rubrics" / "complexity-factor.md").read_text()


@pytest.fixture(scope="session")
def gaming_detection_content(docs_root: Path) -> str:
    return (docs_root / "rubrics" / "gaming-detection.md").read_text()


@pytest.fixture(scope="session")
def tier1_content(docs_root: Path) -> str:
    return (docs_root / "templates" / "tier1-assessment.md").read_text()


@pytest.fixture(scope="session")
def tier2_content(docs_root: Path) -> str:
    return (docs_root / "templates" / "tier2-assessment.md").read_text()


@pytest.fixture(scope="session")
def calibration_content(docs_root: Path) -> str:
    return (docs_root / "templates" / "calibration-agenda.md").read_text()


@pytest.fixture(scope="session")
def claude_md_content(project_root: Path) -> str:
    return (project_root / "CLAUDE.md").read_text()


@pytest.fixture(scope="session")
def all_doc_contents(project_root: Path) -> dict[str, str]:
    """Map relative path -> content for every .md file in the project."""
    result = {}
    for md_file in project_root.rglob("*.md"):
        rel = md_file.relative_to(project_root)
        # Skip tests directory
        if str(rel).startswith("tests"):
            continue
        result[str(rel)] = md_file.read_text()
    return result
