"""
src/datafun/home_sales_eda.py - Home Sales Exploratory Data Analysis.

Explore home sales data through descriptive statistics,
correlations, and visualizations.
"""

from pathlib import Path
from typing import Final

import matplotlib.pyplot as plt
from ml_vizkit import save_chart
import pandas as pd

# === CONSTANTS ===

CHART_DIR: Final = Path("docs") / "home_sales" / "images"

PRICE: Final = "price"
SQFT: Final = "sqft"
BEDROOMS: Final = "bedrooms"
BATHROOMS: Final = "bathrooms"
YEAR_BUILT: Final = "year_built"
SATISFACTION: Final = "satisfaction"
NEIGHBORHOOD: Final = "neighborhood"
PROPERTY_TYPE: Final = "property_type"


# === MAIN EDA FUNCTION ===


def run_eda(df: pd.DataFrame) -> dict:
    """Run exploratory data analysis and create charts.

    Args:
        df: Home sales DataFrame.

    Returns:
        Dictionary containing EDA results and chart paths.
    """

    CHART_DIR.mkdir(parents=True, exist_ok=True)

    # === DATA QUALITY ===

    row_count = len(df)
    column_count = len(df.columns)

    missing_values = {column: int(value) for column, value in df.isna().sum().items()}

    # === DESCRIPTIVE STATISTICS ===

    price_stats = {
        "count": int(df[PRICE].count()),
        "mean": float(df[PRICE].mean()),
        "median": float(df[PRICE].median()),
        "min": float(df[PRICE].min()),
        "max": float(df[PRICE].max()),
        "std": float(df[PRICE].std()),
    }

    sqft_stats = {
        "count": int(df[SQFT].count()),
        "mean": float(df[SQFT].mean()),
        "median": float(df[SQFT].median()),
        "min": float(df[SQFT].min()),
        "max": float(df[SQFT].max()),
        "std": float(df[SQFT].std()),
    }

    # === CORRELATIONS ===

    correlation_columns = [
        PRICE,
        SQFT,
        BEDROOMS,
        BATHROOMS,
        YEAR_BUILT,
        SATISFACTION,
    ]

    correlation_matrix = df[correlation_columns].corr()

    correlations = {
        column: float(correlation_matrix.loc[PRICE, column])
        for column in correlation_columns
    }

    # === CHART PATHS ===

    price_distribution_chart = CHART_DIR / "price-distribution.png"
    sqft_distribution_chart = CHART_DIR / "sqft-distribution.png"
    sqft_price_chart = CHART_DIR / "sqft-vs-price.png"
    bedrooms_price_chart = CHART_DIR / "bedrooms-vs-price.png"
    bathrooms_price_chart = CHART_DIR / "bathrooms-vs-price.png"
    neighborhood_price_chart = CHART_DIR / "average-price-neighborhood.png"
    property_type_price_chart = CHART_DIR / "average-price-property-type.png"
    bedrooms_average_chart = CHART_DIR / "average-price-bedrooms.png"
    bathrooms_average_chart = CHART_DIR / "average-price-bathrooms.png"
    year_built_price_chart = CHART_DIR / "year-built-vs-price.png"
    satisfaction_price_chart = CHART_DIR / "satisfaction-vs-price.png"
    correlation_heatmap_chart = CHART_DIR / "correlation-heatmap.png"

    # === CHART 1: PRICE DISTRIBUTION ===

    plt.figure(figsize=(10, 6))
    plt.hist(df[PRICE], bins=20, edgecolor="black")
    plt.title("Distribution of Home Prices")
    plt.xlabel("Home Price")
    plt.ylabel("Number of Homes")
    plt.grid(alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), price_distribution_chart)
    plt.close()

    # === CHART 2: SQUARE FOOTAGE DISTRIBUTION ===

    plt.figure(figsize=(10, 6))
    plt.hist(df[SQFT], bins=20, edgecolor="black")
    plt.title("Distribution of Home Square Footage")
    plt.xlabel("Square Footage")
    plt.ylabel("Number of Homes")
    plt.grid(alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), sqft_distribution_chart)
    plt.close()

    # === CHART 3: SQUARE FOOTAGE VS PRICE ===

    plt.figure(figsize=(10, 6))
    plt.scatter(
        df[SQFT],
        df[PRICE],
        alpha=0.7,
    )
    plt.title("Home Price vs. Square Footage")
    plt.xlabel("Square Footage")
    plt.ylabel("Home Price")
    plt.grid(alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), sqft_price_chart)
    plt.close()

    # === CHART 4: BEDROOMS VS PRICE ===

    plt.figure(figsize=(10, 6))
    plt.scatter(
        df[BEDROOMS],
        df[PRICE],
        alpha=0.7,
    )
    plt.title("Home Price vs. Number of Bedrooms")
    plt.xlabel("Bedrooms")
    plt.ylabel("Home Price")
    plt.grid(alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), bedrooms_price_chart)
    plt.close()

    # === CHART 5: BATHROOMS VS PRICE ===

    plt.figure(figsize=(10, 6))
    plt.scatter(
        df[BATHROOMS],
        df[PRICE],
        alpha=0.7,
    )
    plt.title("Home Price vs. Number of Bathrooms")
    plt.xlabel("Bathrooms")
    plt.ylabel("Home Price")
    plt.grid(alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), bathrooms_price_chart)
    plt.close()

    # === CHART 6: AVERAGE PRICE BY NEIGHBORHOOD ===

    average_price_neighborhood = (
        df.groupby(NEIGHBORHOOD)[PRICE].mean().sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))
    average_price_neighborhood.plot(
        kind="bar",
        edgecolor="black",
    )
    plt.title("Average Home Price by Neighborhood")
    plt.xlabel("Neighborhood")
    plt.ylabel("Average Home Price")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), neighborhood_price_chart)
    plt.close()

    # === CHART 7: AVERAGE PRICE BY PROPERTY TYPE ===

    average_price_property_type = (
        df.groupby(PROPERTY_TYPE)[PRICE].mean().sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))
    average_price_property_type.plot(
        kind="bar",
        edgecolor="black",
    )
    plt.title("Average Home Price by Property Type")
    plt.xlabel("Property Type")
    plt.ylabel("Average Home Price")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), property_type_price_chart)
    plt.close()

    # === CHART 8: AVERAGE PRICE BY BEDROOMS ===

    average_price_bedrooms = df.groupby(BEDROOMS)[PRICE].mean().sort_index()

    plt.figure(figsize=(10, 6))
    average_price_bedrooms.plot(
        kind="bar",
        edgecolor="black",
    )
    plt.title("Average Home Price by Number of Bedrooms")
    plt.xlabel("Bedrooms")
    plt.ylabel("Average Home Price")
    plt.xticks(rotation=0)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), bedrooms_average_chart)
    plt.close()

    # === CHART 9: AVERAGE PRICE BY BATHROOMS ===

    average_price_bathrooms = df.groupby(BATHROOMS)[PRICE].mean().sort_index()

    plt.figure(figsize=(10, 6))
    average_price_bathrooms.plot(
        kind="bar",
        edgecolor="black",
    )
    plt.title("Average Home Price by Number of Bathrooms")
    plt.xlabel("Bathrooms")
    plt.ylabel("Average Home Price")
    plt.xticks(rotation=0)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), bathrooms_average_chart)
    plt.close()

    # === CHART 10: YEAR BUILT VS PRICE ===

    plt.figure(figsize=(10, 6))
    plt.scatter(
        df[YEAR_BUILT],
        df[PRICE],
        alpha=0.7,
    )
    plt.title("Home Price vs. Year Built")
    plt.xlabel("Year Built")
    plt.ylabel("Home Price")
    plt.grid(alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), year_built_price_chart)
    plt.close()

    # === CHART 11: SATISFACTION VS PRICE ===

    plt.figure(figsize=(10, 6))
    plt.scatter(
        df[SATISFACTION],
        df[PRICE],
        alpha=0.7,
    )
    plt.title("Home Price vs. Satisfaction")
    plt.xlabel("Satisfaction Score")
    plt.ylabel("Home Price")
    plt.grid(alpha=0.3)
    plt.tight_layout()

    save_chart(plt.gca(), satisfaction_price_chart)
    plt.close()

    # === CHART 12: CORRELATION HEATMAP ===

    plt.figure(figsize=(10, 8))

    plt.imshow(
        correlation_matrix,
        interpolation="nearest",
    )

    plt.colorbar(label="Correlation")

    plt.xticks(
        range(len(correlation_columns)),
        correlation_columns,
        rotation=45,
        ha="right",
    )

    plt.yticks(
        range(len(correlation_columns)),
        correlation_columns,
    )

    for row in range(len(correlation_columns)):
        for column in range(len(correlation_columns)):
            plt.text(
                column,
                row,
                f"{correlation_matrix.iloc[row, column]:.2f}",
                ha="center",
                va="center",
            )

    plt.title("Correlation Matrix of Home Sales Variables")
    plt.tight_layout()

    save_chart(plt.gca(), correlation_heatmap_chart)
    plt.close()

    # === RESULTS ===

    results = {
        "row_count": row_count,
        "column_count": column_count,
        "columns": list(df.columns),
        "missing_values": missing_values,
        "charts": {
            "price_distribution": str(price_distribution_chart),
            "sqft_distribution": str(sqft_distribution_chart),
            "sqft_vs_price": str(sqft_price_chart),
            "bedrooms_vs_price": str(bedrooms_price_chart),
            "bathrooms_vs_price": str(bathrooms_price_chart),
            "average_price_neighborhood": str(neighborhood_price_chart),
            "average_price_property_type": str(property_type_price_chart),
            "average_price_bedrooms": str(bedrooms_average_chart),
            "average_price_bathrooms": str(bathrooms_average_chart),
            "year_built_vs_price": str(year_built_price_chart),
            "satisfaction_vs_price": str(satisfaction_price_chart),
            "correlation_heatmap": str(correlation_heatmap_chart),
        },
        "price_stats": price_stats,
        "sqft_stats": sqft_stats,
        "correlations": correlations,
    }

    return results
