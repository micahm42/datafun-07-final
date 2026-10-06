# datafun-07-final

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://docs.astral.sh/ruff/)

[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)

[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: exploratory data analysis and linear regression using home sales data.

## Project Goal

This project applies the data analytics and machine learning workflow to a real-world-style **home sales dataset**.

The project explores factors associated with home prices and uses **linear regression** to predict home price from square footage.

The analysis asks questions such as:

* How are home prices distributed?
* How does square footage relate to home price?
* How do bedrooms and bathrooms relate to price?
* How do prices vary by neighborhood?
* How do prices vary by property type?
* Is there a relationship between year built and home price?
* Does customer satisfaction show a relationship with price?
* How well can square footage predict home price?

The project combines **exploratory data analysis (EDA)**, data visualization, statistical analysis, and machine learning.

## Dataset

The project uses:

```text
data/raw/home_sales.csv
```

The dataset contains **250 home sales records** and the following variables:

| Column          | Description                                |
| --------------- | ------------------------------------------ |
| `neighborhood`  | Neighborhood where the property is located |
| `property_type` | Type of property                           |
| `price`         | Home sale price                            |
| `sqft`          | Square footage                             |
| `bedrooms`      | Number of bedrooms                         |
| `bathrooms`     | Number of bathrooms                        |
| `year_built`    | Year the property was built                |
| `satisfaction`  | Satisfaction rating                        |

The dataset contains 250 rows and 8 columns with no missing values.

## Analysis Process

The project follows a structured analytics workflow:

```text
OBSERVE
DECLARE
PREPARE
EXPLORE
SPLIT
BASELINE
TRAIN
PREDICT
EVALUATE
VISUALIZE
ASSESS
REPORT
```

### Exploratory Data Analysis

The EDA phase examines the structure and characteristics of the dataset.

The project generates visualizations including:

* Home price distribution
* Square footage distribution
* Square footage vs. home price
* Bedrooms vs. home price
* Bathrooms vs. home price
* Average price by neighborhood
* Average price by property type
* Average price by number of bedrooms
* Average price by number of bathrooms
* Year built vs. home price
* Satisfaction vs. home price

These visualizations help identify patterns and relationships before building the predictive model.

### Linear Regression

The regression model uses:

```text
Feature: sqft
Target: price
Model: LinearRegression
```

The dataset is divided into training and testing sets.

The project also establishes a **mean baseline model** so the linear regression model can be compared against a simple prediction strategy.

The model is evaluated using:

* RMSE — Root Mean Squared Error
* R² — coefficient of determination
* RMSE improvement compared with the baseline
* Mean residual
* Mean absolute residual

The project also generates:

* Actual vs. predicted home price chart
* Regression residual chart

## Project Structure

```text
datafun-07-final/
│
├── data/
│   └── raw/
│       └── home_sales.csv
│
├── docs/
│   └── home_sales/
│       ├── index.html
│       ├── images/
│       └── assets/
│           └── northwest-logo.svg
│
├── src/
│   └── datafun/
│       ├── __init__.py
│       ├── home_sales.py
│       ├── home_sales_eda.py
│       ├── home_sales_regression.py
│       └── home_sales_report.py
│
├── pyproject.toml
├── uv.lock
└── README.md
```

## Important Files

### `src/datafun/home_sales.py`

Main project controller.

This module:

1. Loads the home sales CSV.
2. Displays the dataset structure.
3. Checks for missing values.
4. Runs exploratory data analysis.
5. Runs the linear regression model.
6. Builds the HTML report.
7. Opens the completed report in the default browser.

### `src/datafun/home_sales_eda.py`

Performs exploratory data analysis and creates the project's EDA charts.

### `src/datafun/home_sales_regression.py`

Builds and evaluates the linear regression model.

The model predicts:

```text
Home Price = f(Square Footage)
```

The module also compares the regression model against a mean baseline.

### `src/datafun/home_sales_report.py`

Creates the final HTML report containing:

* Dataset overview
* Descriptive statistics
* Exploratory analysis
* Correlation analysis
* Regression results
* Model evaluation
* Visualizations
* Residual analysis
* Conclusions

The report is saved to:

```text
docs/home_sales/index.html
```

## Common Workflow

The project uses **uv** to manage the Python environment and dependencies.

### Open the Project

From the `Repos` directory:

```shell
cd datafun-07-final

code .
```

### Set Up the Environment

```shell
uv self update

uv python pin 3.14

uv python install

uv lock --upgrade

uv sync
```

### Run the Project

The primary command for this project is:

```shell
uv run python -m datafun.home_sales
```

This runs the complete analysis pipeline.

The program will:

```text
Load Data
    ↓
Inspect Data
    ↓
Run EDA
    ↓
Create EDA Charts
    ↓
Train Regression Model
    ↓
Evaluate Model
    ↓
Create Regression Charts
    ↓
Build HTML Report
    ↓
Open Report in Browser
```

The completed report can also be found at:

```text
docs/home_sales/index.html
```

## Code Quality

The project uses Ruff for formatting and linting:

```shell
uv run ruff format .

uv run ruff check . --fix
```

Type checking:

```shell
uv run ty check
```

Tests:

```shell
uv run python -m pytest
```

## Documentation

The generated project report is located at:

```text
docs/home_sales/index.html
```

The report is branded for:

**Northwest Missouri State University**

**Data Analytics Fundamentals — FA26**

**Micah Manuel**

The report presents the exploratory data analysis and linear regression findings in a professional HTML format.

## Helpful Tips

Use the **UP ARROW** and **DOWN ARROW** keys in the terminal to scroll through previous commands.

Use:

```text
CTRL + F
```

to find and replace text within a file in VS Code.

## VS Code Python Environment

If VS Code does not automatically use the project's `.venv` environment:

1. Open the Command Palette with `Ctrl+Shift+P`.
2. Select **Python: Select Interpreter**.
3. Select the interpreter from this project's `.venv` folder.

If VS Code still does not recognize the environment or installed tools:

1. Open the Command Palette with `Ctrl+Shift+P`.
2. Run **Developer: Reload Window**.

## Troubleshooting

### Python Interactive Mode

If you see:

```text
>>>
```

or:

```text
...
```

in the terminal, you may have accidentally entered Python interactive mode.

On Windows, press:

```text
Ctrl + C
```

or:

```text
Ctrl + Z
```

then press **Enter**.

### Wrong Virtual Environment

If uv reports that `VIRTUAL_ENV` does not match the project environment, make sure the terminal is using the `.venv` associated with:

```text
datafun-07-final
```

Then run:

```shell
uv sync
```

and:

```shell
uv run python -m datafun.home_sales
```

Using `uv run` ensures the command uses the project's managed environment.

## Project Output

The project produces two main types of output.

### Analysis Charts

Charts are saved to:

```text
docs/home_sales/images/
```

These include the EDA visualizations and regression evaluation charts.

### HTML Report

The completed report is:

```text
docs/home_sales/index.html
```

The report combines the analysis, model results, charts, and conclusions into one presentation.

## Git Workflow

Save progress with:

```shell
git add -A

git commit -m "Update home sales analysis"

git push -u origin main
```

For future changes:

```shell
git add -A

git commit -m "Describe your changes"

git push
```

## License

This project is licensed under the [MIT License](./LICENSE).


Example:

```text
TRAIN       LinearRegression
PREDICT     on X_test
EVALUATE    baseline vs model on y_test
```

## Important Folders and Files

- **data/raw** - raw data
- **docs/** - project narrative and documentation\
- **src/datafun** - supporting Python code
- **pyproject.toml** - project configuration
- **zensical.toml** - documentation configuration

## Common Workflow

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
carefully.

## Success

After completing Phase 1. **Start & Run**, you'll have the example project,
running on your machine.
A new file `project.log` will appear in the root project folder
and running the example script will print out:

```shell
===================================
END main() - Executed successfully!
===================================
```

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

Open a machine terminal in your `Repos` folder:

```shell
git clone https://github.com/denisecase/datafun-06-ml

cd datafun-06-ml
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal**
in the root project folder.
Copy each command, paste into your terminal, and hit ENTER,
to run each command one at a time.

```shell
uv self update
uv python pin 3.14

uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made by pre-commit tasks
git add -A
uv run pre-commit run --all-files

# run the penguin example: is there a linear relationship?
uv run python -m datafun.app

# do chores
uv run ruff format .
uv run ruff check . --fix
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress as you work
git add -A
git commit -m "your message here"
# repeat if changes were made (try the UP ARROW)
git add -A
git commit -m "your message here"

git push -u origin main
```

</details>

## Helpful Tips

- Use the **UP ARROW** and **DOWN ARROW** in the terminal
  to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Much Can Be Ignored

- You do not need to add to or modify `tests/`.
  Tests are recommended and provided for example only.
- Many files are silent helpers.
  [Explore](https://denisecase.github.io/professional-python-project-explainer/)
  as you like, but most files are never touched.
- You do NOT need to understand everything;
  let understanding build over time.

## As Needed

If VS Code does not automatically use the new `.venv` environment:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Python: Select Interpreter**.
3. Select the interpreter from this project's `.venv` folder.

If VS Code still does not recognize the environment or newly installed tools:

1. Open the Command Palette (`Ctrl+Shift+P`).
2. Run **Developer: Reload Window**.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Documentation

- [Documentation](https://github.com/micahm42/datafun-06-ml)

## Data Card

- [Palmer Penguins Data Card](./docs/data-card.md)

## Annotations

- [.annotations/annotations.md](./.annotations/annotations.md)

## Citation

- [CITATION.cff](./CITATION.cff)

## License

This project is licensed under the [MIT License](./LICENSE).
