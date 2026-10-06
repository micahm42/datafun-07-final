"""
src/datafun/home_sales.py - Home Sales Analysis Project.

Loads home sales data, runs exploratory data analysis,
performs linear regression, builds an HTML report,
and opens the report in the default web browser.
"""

# === DECLARE IMPORTS ===

from pathlib import Path
from typing import Final
import webbrowser

from datafun_toolkit.logger import get_logger, log_header, log_path
import pandas as pd

from datafun.home_sales_eda import run_eda
from datafun.home_sales_regression import run_regression
from datafun.home_sales_report import build_report

# === CONFIGURE LOGGER ===

LOG = get_logger("P06-HOME-SALES", level="DEBUG")


# === DECLARE CONSTANTS ===

DATA_FILE_PATH: Final[Path] = Path("data") / "raw" / "home_sales.csv"

REPORT_PATH: Final[Path] = Path("docs") / "home_sales" / "index.html"


# === MAIN FUNCTION ===


def main() -> None:
    """Run the complete home sales analysis workflow."""

    # ---------------------------------------------------------
    # 1. LOAD DATA
    # ---------------------------------------------------------

    log_header(LOG, "HOME SALES ANALYSIS")

    log_path(LOG, "Input data", DATA_FILE_PATH)

    LOG.info("Loading home sales data...")

    df: pd.DataFrame = pd.read_csv(DATA_FILE_PATH)

    LOG.info("Loaded %d rows and %d columns.", len(df), len(df.columns))

    LOG.debug("Columns: %s", list(df.columns))

    # ---------------------------------------------------------
    # 2. DISPLAY BASIC DATA INFORMATION
    # ---------------------------------------------------------

    LOG.info("Preview of home sales data:")

    LOG.info("\n%s", df.head().to_string())

    LOG.info("Data types:")

    LOG.info("\n%s", df.dtypes.to_string())

    LOG.info("Missing values:")

    LOG.info("\n%s", df.isna().sum().to_string())

    # ---------------------------------------------------------
    # 3. RUN EXPLORATORY DATA ANALYSIS
    # ---------------------------------------------------------

    LOG.info("Running exploratory data analysis...")

    eda_results = run_eda(df)

    LOG.info("Exploratory data analysis complete.")

    # ---------------------------------------------------------
    # 4. RUN LINEAR REGRESSION
    # ---------------------------------------------------------

    LOG.info("Running linear regression...")

    regression_results = run_regression(df)

    LOG.info("Linear regression complete.")

    # ---------------------------------------------------------
    # 5. BUILD HTML REPORT
    # ---------------------------------------------------------

    LOG.info("Building HTML report...")

    build_report(
        df,
        eda_results,
        regression_results,
    )

    LOG.info("HTML report created: %s", REPORT_PATH)

    # ---------------------------------------------------------
    # 6. OPEN HTML REPORT
    # ---------------------------------------------------------

    report_uri = REPORT_PATH.resolve().as_uri()

    LOG.info("Opening HTML report in default browser...")

    webbrowser.open(report_uri)

    # ---------------------------------------------------------
    # 7. COMPLETE
    # ---------------------------------------------------------

    log_header(LOG, "HOME SALES ANALYSIS COMPLETE")


# === RUN MAIN ===

if __name__ == "__main__":
    main()
