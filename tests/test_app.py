"""Smoke tests for the Home Sales Analysis project.

WHY a smoke test:
    A smoke test verifies that the project's main module can be imported
    successfully and that its main() function is available.

    This catches common problems such as syntax errors, missing imports,
    and incorrect module names before the full analysis is executed.

Run from the project root:

    uv run pytest
"""


def test_home_sales_module_imports() -> None:
    """Confirm the Home Sales module imports and exposes main()."""
    from datafun.home_sales import main

    assert callable(main)
