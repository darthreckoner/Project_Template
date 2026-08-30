import unittest

from scripts.check_governance import profile_errors


class GovernanceProfileTests(unittest.TestCase):
    def test_template_mode_passes_without_project_intent_records(self) -> None:
        self.assertEqual(
            profile_errors("Status: Template\nSelected profile: Template\n", set(), ""),
            [],
        )

    def test_personal_baseline_reports_missing_brief_fields(self) -> None:
        errors = profile_errors(
            "Status: Active\nSelected profile: Personal Baseline\n", set(), ""
        )
        self.assertTrue(
            any("complete 'Validation declaration:' for the selected profile" in error for error in errors)
        )

    def test_governed_engineering_requires_durable_intent_records(self) -> None:
        brief = """Status: Active
Selected profile: Governed Engineering
Date: 2026-08-30
Validation declaration: python scripts/check_governance.py
External dependencies and integrations: None
Governed checklist: Complete
"""
        errors = profile_errors(brief, set(), "Governed Engineering Activation")
        self.assertTrue(any("required for Governed Engineering" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
