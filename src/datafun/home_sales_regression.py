"""
src/datafun/home_sales_regression.py - Home Sales Regression Analysis.

Predict home price using square footage with linear regression
and compare the results with an extended model using additional
housing characteristics.
"""

import logging
from pathlib import Path
from typing import Final

import matplotlib.pyplot as plt
from ml_vizkit import save_chart
import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split

# ============================================================
# CONSTANTS
# ============================================================

LOG = logging.getLogger("P06-HOME-SALES-REGRESSION")

CHART_DIR = Path("docs") / "home_sales" / "images"

TARGET: Final = "price"

FEATURE: Final = "sqft"

EXTENDED_FEATURES: Final = [
    "sqft",
    "bedrooms",
    "bathrooms",
    "year_built",
]

TEST_SIZE: Final = 0.20

RANDOM_STATE: Final = 42

BASELINE_STRATEGY: Final = "mean"

REGRESSION_PREDICTIONS_CHART = CHART_DIR / "regression-predictions.png"

REGRESSION_RESIDUALS_CHART = CHART_DIR / "regression-residuals.png"


# ============================================================
# REGRESSION FUNCTION
# ============================================================


def run_regression(df: pd.DataFrame) -> dict:
    """Run baseline, primary, and extended regression models."""

    CHART_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # ========================================================
    # PREPARE DATA
    # ========================================================

    model_df = df[
        [
            TARGET,
            *EXTENDED_FEATURES,
        ]
    ].dropna()

    X = model_df[[FEATURE]]

    y = model_df[TARGET]

    (
        X_train,
        X_test,
        y_train,
        y_test,
    ) = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    # ========================================================
    # BASELINE MODEL
    # ========================================================

    baseline = DummyRegressor(
        strategy=BASELINE_STRATEGY,
    )

    baseline.fit(
        X_train,
        y_train,
    )

    baseline_predictions = baseline.predict(
        X_test,
    )

    baseline_rmse = root_mean_squared_error(
        y_test,
        baseline_predictions,
    )

    baseline_r2 = r2_score(
        y_test,
        baseline_predictions,
    )

    # ========================================================
    # PRIMARY MODEL
    #
    # price ~ sqft
    # ========================================================

    model = LinearRegression()

    model.fit(
        X_train,
        y_train,
    )

    predictions = model.predict(
        X_test,
    )

    slope = float(
        model.coef_[0],
    )

    intercept = float(
        model.intercept_,
    )

    model_rmse = root_mean_squared_error(
        y_test,
        predictions,
    )

    model_r2 = r2_score(
        y_test,
        predictions,
    )

    # ========================================================
    # PRIMARY MODEL IMPROVEMENT
    # ========================================================

    if baseline_rmse != 0:
        rmse_improvement = (baseline_rmse - model_rmse) / baseline_rmse * 100
    else:
        rmse_improvement = 0.0

    # ========================================================
    # PRIMARY MODEL RESIDUALS
    # ========================================================

    residuals = y_test.to_numpy() - predictions

    mean_residual = float(
        np.mean(residuals),
    )

    mean_absolute_residual = float(
        np.mean(
            np.abs(residuals),
        ),
    )

    # ========================================================
    # EXTENDED MODEL
    #
    # price ~ sqft + bedrooms + bathrooms + year_built
    # ========================================================

    extended_df = df[
        [
            TARGET,
            *EXTENDED_FEATURES,
        ]
    ].dropna()

    X_extended = extended_df[EXTENDED_FEATURES]

    y_extended = extended_df[TARGET]

    (
        X_extended_train,
        X_extended_test,
        y_extended_train,
        y_extended_test,
    ) = train_test_split(
        X_extended,
        y_extended,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    extended_model = LinearRegression()

    extended_model.fit(
        X_extended_train,
        y_extended_train,
    )

    extended_predictions = extended_model.predict(
        X_extended_test,
    )

    extended_rmse = root_mean_squared_error(
        y_extended_test,
        extended_predictions,
    )

    extended_r2 = r2_score(
        y_extended_test,
        extended_predictions,
    )

    # ========================================================
    # EXTENDED MODEL IMPROVEMENT
    # ========================================================

    if baseline_rmse != 0:
        extended_rmse_improvement = (
            (baseline_rmse - extended_rmse) / baseline_rmse * 100
        )
    else:
        extended_rmse_improvement = 0.0

    # ========================================================
    # EXTENDED MODEL COEFFICIENTS
    # ========================================================

    extended_coefficients = {
        feature: float(coefficient)
        for feature, coefficient in zip(
            EXTENDED_FEATURES,
            extended_model.coef_,
        )
    }

    extended_intercept = float(
        extended_model.intercept_,
    )

    # ========================================================
    # EXTENDED MODEL COMPARISON
    # ========================================================

    rmse_difference = model_rmse - extended_rmse

    r2_difference = extended_r2 - model_r2

    if extended_rmse < model_rmse:
        better_model = "Extended Model"
    elif extended_rmse > model_rmse:
        better_model = "Square Footage Model"
    else:
        better_model = "Both Models"

    # ========================================================
    # CHART 1
    #
    # Actual vs. Predicted
    # ========================================================

    plt.figure(figsize=(10, 6))

    plt.scatter(
        y_test,
        predictions,
        alpha=0.7,
        label="Predicted values",
    )

    min_value = min(
        y_test.min(),
        predictions.min(),
    )

    max_value = max(
        y_test.max(),
        predictions.max(),
    )

    plt.plot(
        [
            min_value,
            max_value,
        ],
        [
            min_value,
            max_value,
        ],
        linestyle="--",
        label="Perfect prediction",
    )

    plt.title(
        "Actual vs. Predicted Home Prices",
    )

    plt.xlabel(
        "Actual Home Price",
    )

    plt.ylabel(
        "Predicted Home Price",
    )

    plt.legend()

    plt.grid(
        alpha=0.3,
    )

    plt.tight_layout()

    save_chart(
        plt.gca(),
        REGRESSION_PREDICTIONS_CHART,
    )

    plt.close()

    # ========================================================
    # CHART 2
    #
    # Residuals
    # ========================================================

    plt.figure(figsize=(10, 6))

    plt.scatter(
        predictions,
        residuals,
        alpha=0.7,
    )

    plt.axhline(
        y=0,
        linestyle="--",
    )

    plt.title(
        "Regression Residuals",
    )

    plt.xlabel(
        "Predicted Home Price",
    )

    plt.ylabel(
        "Residual",
    )

    plt.grid(
        alpha=0.3,
    )

    plt.tight_layout()

    save_chart(
        plt.gca(),
        REGRESSION_RESIDUALS_CHART,
    )

    plt.close()

    # ========================================================
    # RESULTS
    # ========================================================

    results = {
        # Primary model
        "feature": FEATURE,
        "target": TARGET,
        "training_rows": len(X_train),
        "testing_rows": len(X_test),
        "baseline_strategy": BASELINE_STRATEGY,
        "baseline_rmse": float(
            baseline_rmse,
        ),
        "baseline_r2": float(
            baseline_r2,
        ),
        "model_rmse": float(
            model_rmse,
        ),
        "model_r2": float(
            model_r2,
        ),
        "rmse_improvement": float(
            rmse_improvement,
        ),
        "slope": slope,
        "intercept": intercept,
        "mean_residual": mean_residual,
        "mean_absolute_residual": (mean_absolute_residual),
        "equation": (f"{TARGET} = {slope:.2f} * {FEATURE} + {intercept:.2f}"),
        # Extended model
        "extended_features": EXTENDED_FEATURES,
        "extended_training_rows": len(
            X_extended_train,
        ),
        "extended_testing_rows": len(
            X_extended_test,
        ),
        "extended_rmse": float(
            extended_rmse,
        ),
        "extended_r2": float(
            extended_r2,
        ),
        "extended_rmse_improvement": float(
            extended_rmse_improvement,
        ),
        "extended_coefficients": (extended_coefficients),
        "extended_intercept": (extended_intercept),
        "extended_equation": (
            "price = "
            f"{extended_coefficients['sqft']:.2f} * sqft + "
            f"{extended_coefficients['bedrooms']:.2f} * bedrooms + "
            f"{extended_coefficients['bathrooms']:.2f} * bathrooms + "
            f"{extended_coefficients['year_built']:.2f} * year_built + "
            f"{extended_intercept:.2f}"
        ),
        # Model comparison
        "rmse_difference": float(
            rmse_difference,
        ),
        "r2_difference": float(
            r2_difference,
        ),
        "better_model": better_model,
        # Charts
        "charts": {
            "predictions": str(
                REGRESSION_PREDICTIONS_CHART,
            ),
            "residuals": str(
                REGRESSION_RESIDUALS_CHART,
            ),
        },
    }

    LOG.info("Linear regression analysis complete.")

    LOG.info(
        "Primary model RMSE: %.2f",
        model_rmse,
    )

    LOG.info(
        "Primary model R2: %.3f",
        model_r2,
    )

    LOG.info(
        "Extended model RMSE: %.2f",
        extended_rmse,
    )

    LOG.info(
        "Extended model R2: %.3f",
        extended_r2,
    )

    LOG.info(
        "Better model based on RMSE: %s",
        better_model,
    )

    return results
