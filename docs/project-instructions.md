# Project-Specific Instructions

## Home Sales Analysis

This project analyzes residential home sales data using Python. The analysis includes exploratory data analysis, data visualization, correlation analysis, linear regression, model evaluation, residual analysis, and an extended regression model.

### How to Run the Project

From the project root directory, run:

```powershell
uv run python -m datafun.home_sales
```

The program will:

1. Load the home sales dataset from `data/raw/home_sales.csv`.
2. Perform exploratory data analysis.
3. Generate analysis charts in `docs/home_sales/images/`.
4. Train and evaluate linear regression models.
5. Compare the primary and extended regression models.
6. Generate the HTML analysis report.
7. Open the report in the default web browser.

### View the Report

The generated report is located at:

```text
docs/home_sales/index.html
```

The report presents the project findings, visualizations, regression results, model evaluation, and conclusions.

### Run Project Checks

The project includes automated code-quality and testing tools.

Run Ruff:

```powershell
uv run ruff check .
```

Run the type checker:

```powershell
uv run ty check
```

Run the tests:

```powershell
uv run pytest
```

### Build the Documentation

To build the project documentation:

```powershell
uv run python -m zensical build
```

To preview the documentation locally:

```powershell
uv run python -m zensical serve
```

The local documentation server is typically available at:

```text
http://127.0.0.1:8000
```

Press **Ctrl+C** in the PowerShell window to stop the documentation server.

## Project Organization

The primary project files are organized as follows:

```text
data/
└── raw/
    └── home_sales.csv

docs/
└── home_sales/
    ├── index.html
    ├── assets/
    └── images/

src/
└── datafun/
    ├── home_sales.py
    ├── home_sales_eda.py
    ├── home_sales_regression.py
    └── home_sales_report.py

tests/
└── test_app.py
```

The main entry point is:

```text
src/datafun/home_sales.py
```

The project uses a reproducible workflow that separates data loading, exploratory analysis, regression modeling, reporting, and testing.
