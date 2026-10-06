"""
src/datafun/home_sales_report.py - Home Sales HTML Report.

Builds a Northwest Missouri State University branded HTML report
for the Home Sales Analysis project.
"""

from pathlib import Path
from typing import Any

import pandas as pd

# ============================================================
# REPORT INFORMATION
# ============================================================

REPORT_PATH = Path("docs") / "home_sales" / "index.html"

IMAGE_DIR = Path("docs") / "home_sales" / "images"

ASSET_DIR = Path("docs") / "home_sales" / "assets"

LOGO_PATH = ASSET_DIR / "northwest-logo.svg"

STUDENT_NAME = "Micah Manuel"

COURSE_NAME = "Data Analytics Fundamentals"

SEMESTER = "FA26"

UNIVERSITY_NAME = "Northwest Missouri State University"


# ============================================================
# FORMATTING FUNCTIONS
# ============================================================


def format_currency(value: float) -> str:
    """Format a number as U.S. currency."""
    return f"${value:,.0f}"


def format_number(value: float) -> str:
    """Format a number with commas."""
    return f"{value:,.0f}"


def image_html(filename: str, alt_text: str) -> str:
    """Return HTML for a report image."""
    return f"""
    <figure class="chart">
        <img src="images/{filename}" alt="{alt_text}">
        <figcaption>{alt_text}</figcaption>
    </figure>
    """


# ============================================================
# REPORT BUILDER
# ============================================================


def build_report(
    df: pd.DataFrame,
    eda_results: dict[str, Any],
    regression_results: dict[str, Any],
) -> None:
    """Build the complete HTML report."""

    REPORT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    IMAGE_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    ASSET_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # ========================================================
    # DATASET INFORMATION
    # ========================================================

    row_count = eda_results["row_count"]

    column_count = eda_results["column_count"]

    columns = eda_results["columns"]

    missing_values = eda_results["missing_values"]

    price_stats = eda_results["price_stats"]

    sqft_stats = eda_results["sqft_stats"]

    correlations = eda_results["correlations"]

    # ========================================================
    # REGRESSION INFORMATION
    #
    # These names match home_sales_regression.py exactly.
    # ========================================================

    slope = regression_results["slope"]

    intercept = regression_results["intercept"]

    equation = regression_results["equation"]

    baseline_rmse = regression_results["baseline_rmse"]

    baseline_r2 = regression_results["baseline_r2"]

    model_rmse = regression_results["model_rmse"]

    model_r2 = regression_results["model_r2"]

    rmse_improvement = regression_results["rmse_improvement"]

    mean_residual = regression_results["mean_residual"]

    mean_absolute_residual = regression_results["mean_absolute_residual"]

    # ========================================================
    # FIND STRONGEST CORRELATION
    # ========================================================

    correlation_items = [
        (column, value) for column, value in correlations.items() if column != "price"
    ]

    if correlation_items:
        strongest_feature, strongest_correlation = max(
            correlation_items,
            key=lambda item: abs(item[1]),
        )
    else:
        strongest_feature = "None"
        strongest_correlation = 0.0

    # ========================================================
    # CORRELATION TABLE
    # ========================================================

    correlation_rows = ""

    for column, value in correlations.items():
        correlation_rows += f"""
        <tr>
            <td>{column}</td>
            <td>{value:.3f}</td>
        </tr>
        """

    # ========================================================
    # MISSING VALUE TABLE
    # ========================================================

    missing_rows = ""

    for column, value in missing_values.items():
        missing_rows += f"""
        <tr>
            <td>{column}</td>
            <td>{value}</td>
        </tr>
        """

    # ========================================================
    # COLUMN LIST
    # ========================================================

    column_list = ""

    for column in columns:
        column_list += f"""
        <li><code>{column}</code></li>
        """

    # ========================================================
    # DATA QUALITY SUMMARY
    # ========================================================

    total_missing = sum(missing_values.values())

    if total_missing == 0:
        data_quality_message = (
            "The dataset contains no missing values, so all "
            "250 observations were available for analysis."
        )
    else:
        data_quality_message = (
            f"The dataset contains {total_missing} missing "
            "values that should be considered during analysis."
        )

    # ========================================================
    # MODEL INTERPRETATION
    # ========================================================

    if model_r2 >= 0.70:
        r2_interpretation = (
            "The model explains a substantial portion of the variation in home prices."
        )
    elif model_r2 >= 0.40:
        r2_interpretation = (
            "The model explains a moderate portion of the variation in home prices."
        )
    elif model_r2 >= 0:
        r2_interpretation = (
            "The model explains some variation in home prices, "
            "but substantial variation remains unexplained."
        )
    else:
        r2_interpretation = (
            "The model does not explain the variation in home "
            "prices better than the baseline according to R²."
        )

    if strongest_correlation >= 0.70:
        correlation_interpretation = (
            f"{strongest_feature} has a strong positive linear relationship with price."
        )
    elif strongest_correlation >= 0.40:
        correlation_interpretation = (
            f"{strongest_feature} has a moderate positive "
            "linear relationship with price."
        )
    elif strongest_correlation > 0:
        correlation_interpretation = (
            f"{strongest_feature} has a weak positive linear relationship with price."
        )
    elif strongest_correlation <= -0.70:
        correlation_interpretation = (
            f"{strongest_feature} has a strong negative linear relationship with price."
        )
    elif strongest_correlation <= -0.40:
        correlation_interpretation = (
            f"{strongest_feature} has a moderate negative "
            "linear relationship with price."
        )
    else:
        correlation_interpretation = (
            f"{strongest_feature} has a relatively weak linear relationship with price."
        )

    # ========================================================
    # LOGO
    # ========================================================

    if LOGO_PATH.exists():
        logo_html = """
        <img
            src="assets/northwest-logo.svg"
            alt="Northwest Missouri State University Bearcats"
            class="university-logo"
        >
        """
    else:
        logo_html = """
        <div class="logo-placeholder">
            NORTHWEST
        </div>
        """

    # ========================================================
    # HTML DOCUMENT
    # ========================================================

    html = f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>
    Home Sales Analysis | {STUDENT_NAME}
</title>

<style>

    /* ======================================================
       NORTHWEST MISSOURI STATE UNIVERSITY BRANDING
       ====================================================== */

    :root {{
        --nw-green: #006747;
        --nw-dark-green: #004d38;
        --nw-light-green: #e8f1ee;
        --nw-gray: #babbbc;
        --nw-dark-gray: #333333;
        --nw-light-gray: #f4f4f4;
        --nw-white: #ffffff;
    }}

    * {{
        box-sizing: border-box;
    }}

    body {{
        margin: 0;
        padding: 0;

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        background: var(--nw-light-gray);

        color: var(--nw-dark-gray);

        line-height: 1.6;
    }}

    /* ======================================================
       HEADER
       ====================================================== */

    .header {{
        background: var(--nw-green);

        color: var(--nw-white);

        padding:
            45px 30px 40px;

        text-align: center;

        border-bottom:
            8px solid var(--nw-gray);
    }}

    .university-logo {{
        display: block;

        width: 260px;

        max-width: 80%;

        height: auto;

        margin:
            0 auto 25px;

        background: white;

        padding: 12px;

        border-radius: 6px;
    }}

    .logo-placeholder {{
        display: inline-block;

        background: white;

        color: var(--nw-green);

        font-size: 32px;

        font-weight: bold;

        padding:
            15px 30px;

        margin-bottom: 25px;

        border-radius: 6px;
    }}

    .header h1 {{
        margin: 10px 0;

        font-size: 42px;

        letter-spacing: 1px;
    }}

    .header h2 {{
        margin: 5px 0;

        font-size: 22px;

        font-weight: normal;
    }}

    .header .student {{
        margin-top: 20px;

        font-size: 20px;

        font-weight: bold;
    }}

    .header .subtitle {{
        margin-top: 8px;

        font-size: 17px;
    }}

    /* ======================================================
       MAIN CONTENT
       ====================================================== */

    .container {{
        max-width: 1200px;

        margin: 35px auto;

        padding: 0 25px;
    }}

    section {{
        background: var(--nw-white);

        margin-bottom: 30px;

        padding: 30px;

        border-radius: 8px;

        box-shadow:
            0 2px 8px rgba(0, 0, 0, 0.08);

        border-left:
            5px solid var(--nw-green);
    }}

    section h2 {{
        color: var(--nw-green);

        margin-top: 0;

        padding-bottom: 10px;

        border-bottom:
            2px solid var(--nw-gray);
    }}

    section h3 {{
        color: var(--nw-dark-green);
    }}

    /* ======================================================
       SUMMARY CARDS
       ====================================================== */

    .summary-grid {{
        display: grid;

        grid-template-columns:
            repeat(auto-fit, minmax(200px, 1fr));

        gap: 18px;

        margin: 20px 0;
    }}

    .summary-card {{
        background: var(--nw-light-green);

        border-top:
            4px solid var(--nw-green);

        padding: 20px;

        border-radius: 6px;

        text-align: center;
    }}

    .summary-card .value {{
        display: block;

        color: var(--nw-green);

        font-size: 28px;

        font-weight: bold;
    }}

    .summary-card .label {{
        display: block;

        margin-top: 5px;

        font-size: 14px;
    }}

    /* ======================================================
       TABLES
       ====================================================== */

    table {{
        width: 100%;

        border-collapse: collapse;

        margin: 20px 0;
    }}

    th {{
        background: var(--nw-green);

        color: white;

        padding: 12px;

        text-align: left;
    }}

    td {{
        padding: 10px;

        border-bottom:
            1px solid var(--nw-gray);
    }}

    tr:nth-child(even) {{
        background: var(--nw-light-gray);
    }}

    /* ======================================================
       CHARTS
       ====================================================== */

    .chart {{
        margin: 30px auto;

        text-align: center;
    }}

    .chart img {{
        display: block;

        max-width: 100%;

        height: auto;

        margin: 0 auto;

        border:
            1px solid var(--nw-gray);

        border-radius: 5px;
    }}

    figcaption {{
        margin-top: 8px;

        color: #555555;

        font-size: 14px;

        font-style: italic;
    }}

    .chart-grid {{
        display: grid;

        grid-template-columns:
            repeat(auto-fit, minmax(450px, 1fr));

        gap: 25px;
    }}

    .chart-grid .chart {{
        margin: 10px 0;
    }}

    /* ======================================================
       CALLOUTS
       ====================================================== */

    .callout {{
        background: var(--nw-light-green);

        border-left:
            5px solid var(--nw-green);

        padding:
            18px 22px;

        margin: 20px 0;

        border-radius: 4px;
    }}

    .callout strong {{
        color: var(--nw-green);
    }}

    /* ======================================================
       FINDINGS
       ====================================================== */

    .finding-list {{
        margin: 15px 0;

        padding-left: 25px;
    }}

    .finding-list li {{
        margin-bottom: 12px;
    }}

    /* ======================================================
       LIMITATIONS
       ====================================================== */

    .limitations {{
        background: #f8f8f8;

        border-left:
            5px solid var(--nw-gray);

        padding:
            18px 22px;

        margin: 20px 0;

        border-radius: 4px;
    }}

    .limitations li {{
        margin-bottom: 10px;
    }}

    /* ======================================================
       CODE
       ====================================================== */

    code {{
        background: #eeeeee;

        padding:
            2px 6px;

        border-radius: 3px;

        font-family:
            Consolas,
            "Courier New",
            monospace;
    }}

    /* ======================================================
       FOOTER
       ====================================================== */

    footer {{
        background: var(--nw-green);

        color: white;

        text-align: center;

        padding: 25px;

        margin-top: 40px;
    }}

    footer strong {{
        font-size: 16px;
    }}

    footer p {{
        margin: 5px 0;
    }}

    /* ======================================================
       MOBILE
       ====================================================== */

    @media (max-width: 700px) {{

        .header h1 {{
            font-size: 30px;
        }}

        .header h2 {{
            font-size: 18px;
        }}

        .container {{
            padding: 0 12px;
        }}

        section {{
            padding: 20px;
        }}

        .chart-grid {{
            grid-template-columns: 1fr;
        }}

    }}

</style>

</head>


<body>


<!-- ======================================================
     REPORT HEADER
     ====================================================== -->

<header class="header">

    {logo_html}

    <h1>Home Sales Analysis</h1>

    <h2>{UNIVERSITY_NAME}</h2>

    <div class="student">
        {STUDENT_NAME}
    </div>

    <div class="subtitle">
        {COURSE_NAME} — {SEMESTER}
    </div>

    <div class="subtitle">
        Exploratory Data Analysis &amp; Linear Regression
    </div>

</header>


<main class="container">


<!-- ======================================================
     1. KEY FINDINGS
     ====================================================== -->

<section>

    <h2>1. Key Findings</h2>

    <p>
        The analysis examined
        <strong>{format_number(row_count)} homes</strong>
        across
        <strong>{column_count} variables</strong>.
        The dataset contained no missing values, allowing all
        observations to be considered during the analysis.
    </p>

    <ul class="finding-list">

        <li>
            The average home price was
            <strong>
                {format_currency(price_stats["mean"])}
            </strong>,
            with prices ranging from
            <strong>
                {format_currency(price_stats["min"])}
            </strong>
            to
            <strong>
                {format_currency(price_stats["max"])}
            </strong>.
        </li>

        <li>
            The average home contained approximately
            <strong>
                {format_number(sqft_stats["mean"])}
                square feet
            </strong>.
        </li>

        <li>
            <strong>{strongest_feature}</strong> had the
            strongest numerical relationship with price, with a
            correlation of
            <strong>
                {strongest_correlation:.3f}
            </strong>.
        </li>

        <li>
            The square-footage regression model achieved an
            R² score of
            <strong>
                {model_r2:.3f}
            </strong>.
        </li>

        <li>
            The regression model reduced RMSE compared with the
            mean-price baseline by approximately
            <strong>
                {rmse_improvement:.1f}%
            </strong>.
        </li>

    </ul>

    <div class="callout">

        <strong>Overall Finding:</strong>

        Square footage provides useful information for
        predicting home price, but the remaining prediction
        error indicates that other characteristics also
        contribute to differences in home prices.

    </div>

</section>


<!-- ======================================================
     2. DATASET OVERVIEW
     ====================================================== -->

<section>

    <h2>2. Dataset Overview</h2>

    <p>
        This project analyzes residential home sales data using
        exploratory data analysis and linear regression. The
        dataset contains information about home characteristics,
        sale prices, and satisfaction ratings.
    </p>

    <div class="summary-grid">

        <div class="summary-card">
            <span class="value">
                {format_number(row_count)}
            </span>

            <span class="label">
                Homes
            </span>
        </div>

        <div class="summary-card">
            <span class="value">
                {column_count}
            </span>

            <span class="label">
                Variables
            </span>
        </div>

        <div class="summary-card">
            <span class="value">
                {format_currency(price_stats["mean"])}
            </span>

            <span class="label">
                Average Price
            </span>
        </div>

        <div class="summary-card">
            <span class="value">
                {format_number(sqft_stats["mean"])}
            </span>

            <span class="label">
                Average Square Feet
            </span>
        </div>

    </div>


    <h3>Variables</h3>

    <ul>
        {column_list}
    </ul>


    <h3>Data Quality</h3>

    <p>
        {data_quality_message}
    </p>

    <table>

        <thead>

            <tr>
                <th>Column</th>
                <th>Missing Values</th>
            </tr>

        </thead>

        <tbody>
            {missing_rows}
        </tbody>

    </table>

</section>


<!-- ======================================================
     3. HOME PRICE ANALYSIS
     ====================================================== -->

<section>

    <h2>3. Home Price Analysis</h2>

    <p>
        Home prices in the dataset range from
        <strong>
            {format_currency(price_stats["min"])}
        </strong>
        to
        <strong>
            {format_currency(price_stats["max"])}
        </strong>.
        The average home price is
        <strong>
            {format_currency(price_stats["mean"])}
        </strong>,
        while the median home price is
        <strong>
            {format_currency(price_stats["median"])}
        </strong>.
    </p>

    <p>
        Comparing the mean and median helps describe the
        distribution of home prices. A noticeable difference
        between these values can indicate that higher- or
        lower-priced homes are influencing the overall average.
    </p>

    {
        image_html(
            "price-distribution.png",
            "Distribution of Home Prices",
        )
    }

</section>


<!-- ======================================================
     4. SQUARE FOOTAGE ANALYSIS
     ====================================================== -->

<section>

    <h2>4. Square Footage Analysis</h2>

    <p>
        Square footage is the primary predictor used in the
        linear regression model. The average home contains
        approximately
        <strong>
            {format_number(sqft_stats["mean"])}
            square feet
        </strong>,
        while the median home contains approximately
        <strong>
            {format_number(sqft_stats["median"])}
            square feet
        </strong>.
    </p>

    <p>
        The relationship between square footage and price is
        examined visually before building the regression model.
        This provides an initial indication of whether a linear
        model is reasonable.
    </p>

    {
        image_html(
            "sqft-distribution.png",
            "Distribution of Home Square Footage",
        )
    }

</section>


<!-- ======================================================
     5. EXPLORATORY DATA ANALYSIS
     ====================================================== -->

<section>

    <h2>5. Exploratory Data Analysis</h2>

    <p>
        The following visualizations examine relationships
        between home characteristics and sale price. These
        comparisons help identify patterns that may be useful
        for understanding differences in home prices.
    </p>

    <div class="chart-grid">

        {
        image_html(
            "sqft-vs-price.png",
            "Square Footage vs. Home Price",
        )
    }

        {
        image_html(
            "bedrooms-vs-price.png",
            "Bedrooms vs. Home Price",
        )
    }

        {
        image_html(
            "bathrooms-vs-price.png",
            "Bathrooms vs. Home Price",
        )
    }

        {
        image_html(
            "year-built-vs-price.png",
            "Year Built vs. Home Price",
        )
    }

        {
        image_html(
            "satisfaction-vs-price.png",
            "Satisfaction vs. Home Price",
        )
    }

    </div>


    <h3>Categorical Comparisons</h3>

    <div class="chart-grid">

        {
        image_html(
            "average-price-neighborhood.png",
            "Average Price by Neighborhood",
        )
    }

        {
        image_html(
            "average-price-property-type.png",
            "Average Price by Property Type",
        )
    }

        {
        image_html(
            "average-price-bedrooms.png",
            "Average Price by Number of Bedrooms",
        )
    }

        {
        image_html(
            "average-price-bathrooms.png",
            "Average Price by Number of Bathrooms",
        )
    }

    </div>

</section>


<!-- ======================================================
     6. CORRELATION ANALYSIS
     ====================================================== -->

<section>

    <h2>6. Correlation Analysis</h2>

    <p>
        Correlation measures the strength and direction of a
        linear relationship between numerical variables. Values
        closer to 1 indicate a strong positive relationship,
        while values closer to -1 indicate a strong negative
        relationship. A value near 0 indicates a weak linear
        relationship.
    </p>

    <div class="callout">

        <strong>
            Strongest numerical relationship with price:
        </strong>

        {strongest_feature}

        with a correlation of

        <strong>
            {strongest_correlation:.3f}
        </strong>.

        <br><br>

        {correlation_interpretation}

    </div>


    <table>

        <thead>

            <tr>
                <th>Variable</th>
                <th>Correlation with Price</th>
            </tr>

        </thead>

        <tbody>
            {correlation_rows}
        </tbody>

    </table>


    <h3>Correlation Heatmap</h3>

    <p>
        The heatmap provides a visual summary of the
        relationships among the numerical variables in the
        dataset. Darker relationships indicate stronger
        positive or negative correlations.
    </p>

    {
        image_html(
            "correlation-heatmap.png",
            "Correlation Heatmap of Home Sales Variables",
        )
    }

    <p>
        Correlation should be interpreted as a measure of
        association rather than causation. A strong correlation
        between two variables does not prove that one variable
        directly causes changes in the other.
    </p>

</section>


<!-- ======================================================
     7. LINEAR REGRESSION
     ====================================================== -->

<section>

    <h2>7. Linear Regression</h2>

    <p>
        A linear regression model was developed to predict
        home price using square footage as the independent
        variable. The data was divided into training and testing
        sets before the model was evaluated.
    </p>

    <div class="callout">

        <strong>Model equation:</strong>

        <br><br>

        <code>
            {equation}
        </code>

    </div>

    <p>
        The slope of the model is
        <strong>
            {slope:.2f}
        </strong>.
        This means that, according to the model, an additional
        square foot is associated with an estimated increase of
        approximately
        <strong>
            {format_currency(slope)}
        </strong>
        in home price.
    </p>

    <p>
        The intercept is
        <strong>
            {format_currency(intercept)}
        </strong>.
        The intercept represents the model's predicted price
        when square footage is zero. Because a zero-square-foot
        home is not realistic, the intercept is primarily a
        mathematical component of the regression equation rather
        than a practical housing interpretation.
    </p>

</section>


<!-- ======================================================
     8. MODEL EVALUATION
     ====================================================== -->

<section>

    <h2>8. Model Evaluation</h2>

    <div class="summary-grid">

        <div class="summary-card">

            <span class="value">
                {format_currency(model_rmse)}
            </span>

            <span class="label">
                Regression RMSE
            </span>

        </div>


        <div class="summary-card">

            <span class="value">
                {model_r2:.3f}
            </span>

            <span class="label">
                R² Score
            </span>

        </div>


        <div class="summary-card">

            <span class="value">
                {format_currency(baseline_rmse)}
            </span>

            <span class="label">
                Baseline RMSE
            </span>

        </div>


        <div class="summary-card">

            <span class="value">
                {rmse_improvement:.1f}%
            </span>

            <span class="label">
                RMSE Improvement
            </span>

        </div>

    </div>


    <p>
        The regression model achieved an R² score of
        <strong>
            {model_r2:.3f}
        </strong>.
        {r2_interpretation}
    </p>

    <p>
        The model's RMSE is
        <strong>
            {format_currency(model_rmse)}
        </strong>,
        compared with a baseline RMSE of
        <strong>
            {format_currency(baseline_rmse)}
        </strong>.
        The regression improves upon the baseline by
        approximately
        <strong>
            {rmse_improvement:.1f}%
        </strong>.
    </p>

    <p>
        The baseline R² score was
        <strong>
            {baseline_r2:.3f}
        </strong>,
        compared with the regression model's R² score of
        <strong>
            {model_r2:.3f}
        </strong>.
    </p>

    <div class="callout">

        <strong>Why the baseline matters:</strong>

        The mean-price baseline provides a simple benchmark.
        A useful predictive model should perform better than
        simply predicting the average home price for every
        observation.

    </div>

</section>


<!-- ======================================================
     9. REGRESSION CHARTS
     ====================================================== -->

<section>

    <h2>9. Regression Charts</h2>

    <p>
        The prediction chart compares actual home prices with
        prices predicted by the linear regression model.
        Predictions closer to the diagonal reference line
        represent smaller prediction errors.
    </p>

    {
        image_html(
            "regression-predictions.png",
            "Actual vs. Predicted Home Prices",
        )
    }

</section>


<!-- ======================================================
     10. RESIDUAL ANALYSIS
     ====================================================== -->

<section>

    <h2>10. Residual Analysis</h2>

    <p>
        Residuals represent the difference between the actual
        home price and the price predicted by the regression
        model. Positive residuals indicate that the model
        underestimated the actual price, while negative
        residuals indicate that the model overestimated the
        actual price.
    </p>

    <div class="summary-grid">

        <div class="summary-card">

            <span class="value">
                {format_currency(mean_residual)}
            </span>

            <span class="label">
                Mean Residual
            </span>

        </div>


        <div class="summary-card">

            <span class="value">
                {format_currency(mean_absolute_residual)}
            </span>

            <span class="label">
                Mean Absolute Residual
            </span>

        </div>

    </div>


    {
        image_html(
            "regression-residuals.png",
            "Regression Residuals",
        )
    }

    <p>
        A residual pattern centered around zero is generally
        desirable because it indicates that the model does not
        consistently overpredict or underpredict prices in one
        direction.
    </p>

    <div class="callout">

        <strong>Residual interpretation:</strong>

        The mean residual provides an indication of whether the
        model has an overall tendency to overpredict or
        underpredict. The mean absolute residual provides a
        measure of the typical size of the prediction error
        without allowing positive and negative errors to cancel
        each other out.

    </div>

</section>


<!-- ======================================================
     11. MODEL LIMITATIONS
     ====================================================== -->

<section>

    <h2>11. Model Limitations</h2>

    <p>
        Although the regression model provides useful insight
        into the relationship between square footage and home
        price, several limitations should be considered when
        interpreting the results.
    </p>

    <div class="limitations">

        <ul>

            <li>
                The primary model uses only square footage to
                predict home price.
            </li>

            <li>
                Other characteristics such as neighborhood,
                property type, bedrooms, bathrooms, and year
                built may also influence home prices.
            </li>

            <li>
                The dataset contains 250 observations, which
                limits how broadly the results should be
                generalized.
            </li>

            <li>
                Linear regression assumes that the relationship
                between square footage and price can be
                reasonably represented by a straight line.
            </li>

            <li>
                Correlation does not establish causation.
                Relationships observed in the dataset do not
                prove that one characteristic directly causes
                changes in home price.
            </li>

            <li>
                Predictions outside the range of square footage
                represented in the dataset may be less reliable.
            </li>

        </ul>

    </div>

    <div class="callout">

        <strong>Opportunity for Improvement:</strong>

        A multiple linear regression model could incorporate
        additional housing characteristics to determine whether
        they improve predictive performance beyond square
        footage alone.

    </div>

</section>


<!-- ======================================================
     12. CONCLUSIONS
     ====================================================== -->

<section>

    <h2>12. Conclusions</h2>

    <p>
        The analysis demonstrates a measurable relationship
        between square footage and home price. The linear
        regression model provides a useful baseline for
        predicting price from a single housing characteristic.
    </p>

    <p>
        Exploratory analysis also shows that other
        characteristics, including bedrooms, bathrooms,
        neighborhood, property type, year built, and
        satisfaction, may contribute to differences in home
        prices.
    </p>

    <p>
        The correlation analysis provides additional evidence
        that home price is associated with multiple numerical
        characteristics. However, the regression model's
        remaining prediction error demonstrates that square
        footage alone cannot fully explain differences in home
        prices.
    </p>

    <div class="callout">

        <strong>Next Analytical Step:</strong>

        The next phase of the project will compare the
        square-footage-only model with an extended regression
        model using additional housing characteristics. This
        will determine whether adding variables improves
        predictive performance.

    </div>

    <p>
        Overall, the project demonstrates the use of Python,
        pandas, data visualization, exploratory data analysis,
        statistical relationships, and machine learning
        techniques to investigate a real-world style dataset and
        communicate analytical findings.
    </p>

</section>


</main>


<!-- ======================================================
     FOOTER
     ====================================================== -->

<footer>

    <p>
        <strong>{STUDENT_NAME}</strong>
    </p>

    <p>
        {COURSE_NAME} — {SEMESTER}
    </p>

    <p>
        {UNIVERSITY_NAME}
    </p>

    <p>
        Home Sales Analysis
    </p>

</footer>


</body>

</html>
"""

    # ========================================================
    # WRITE REPORT
    # ========================================================

    REPORT_PATH.write_text(
        html,
        encoding="utf-8",
    )
