# Data Card: Home Sales

This Data Card documents the dataset used by the Home Sales Analysis project.

It describes the dataset's composition, variables, intended use, processing, limitations, and considerations relevant to the analysis.

## Dataset Summary

| Item              | Description                                         |
| ----------------- | --------------------------------------------------- |
| Dataset           | Home Sales                                          |
| File              | `data/raw/home_sales.csv`                           |
| Observations      | 250 home sales                                      |
| Variables         | 8                                                   |
| Grain             | One home sale per observation                       |
| Primary use       | Exploratory data analysis and supervised regression |
| Target variable   | `price`                                             |
| Primary feature   | `sqft`                                              |
| Extended features | `bedrooms`, `bathrooms`, `year_built`               |
| Missing values    | None                                                |

## Purpose

The dataset provides information about residential home sales and selected characteristics of each property.

The project uses the dataset to explore relationships between home characteristics and sale price and to demonstrate a reproducible data analytics workflow.

The primary modeling question is:

> How well can home price be predicted using square footage?

An extended model also evaluates whether adding bedrooms, bathrooms, and year built improves predictive performance.

## Dataset Composition

The dataset contains 250 observations and eight variables:

* `neighborhood`
* `property_type`
* `price`
* `sqft`
* `bedrooms`
* `bathrooms`
* `year_built`
* `satisfaction`

### Variable Descriptions

| Variable        | Description                                      | Type        |
| --------------- | ------------------------------------------------ | ----------- |
| `neighborhood`  | Neighborhood associated with the property        | Categorical |
| `property_type` | Type of property                                 | Categorical |
| `price`         | Sale price of the property                       | Numeric     |
| `sqft`          | Square footage of the property                   | Numeric     |
| `bedrooms`      | Number of bedrooms                               | Numeric     |
| `bathrooms`     | Number of bathrooms                              | Numeric     |
| `year_built`    | Year the property was built                      | Numeric     |
| `satisfaction`  | Satisfaction rating associated with the property | Numeric     |

## Missing Data

The dataset contains **no missing values**.

All 250 observations contain values for each of the eight variables.

Because there are no missing values in the variables used for analysis, no imputation or row removal is required during data preparation.

## Intended Use

The dataset is appropriate for:

* exploratory data analysis
* data visualization
* descriptive statistics
* correlation analysis
* introductory predictive modeling
* supervised machine-learning experiments
* demonstrating reproducible analytical workflows

In this project, the dataset is used to investigate relationships among home characteristics and sale price and to compare linear regression models.

## Modeling Use

The primary regression experiment uses:

```text
sqft → price
```

The purpose is to determine how useful square footage is for predicting home price compared with a mean-value baseline.

An extended regression model uses:

```text
sqft + bedrooms + bathrooms + year_built → price
```

The extended model allows the project to determine whether additional property characteristics improve prediction beyond square footage alone.

## Data Processing

The project follows these general processing steps:

1. Loads `home_sales.csv`.
2. Examines the dataset structure and data types.
3. Checks for missing values.
4. Performs exploratory data analysis.
5. Examines relationships among numeric variables.
6. Splits the data into training and testing sets.
7. Establishes a mean-value baseline.
8. Trains the primary linear regression model.
9. Evaluates predictions using RMSE and R².
10. Examines residuals.
11. Trains and evaluates the extended regression model.
12. Compares the primary and extended models.
13. Communicates the findings through visualizations and an HTML report.

## Model Results

The square-footage-only model achieved:

| Metric |                 Result |
| ------ | ---------------------: |
| RMSE   | approximately $169,595 |
| R²     |    approximately 0.329 |

The extended model using square footage, bedrooms, bathrooms, and year built achieved:

| Metric |                 Result |
| ------ | ---------------------: |
| RMSE   | approximately $168,984 |
| R²     |    approximately 0.334 |

The extended model reduced RMSE by approximately **$610** and increased R² by approximately **0.005**.

The improvement is relatively small, suggesting that the additional variables provide limited predictive benefit within this dataset.

## Limitations

The dataset has several limitations that should be considered when interpreting the results.

### Dataset Size

The dataset contains only 250 observations. This is sufficient for an introductory analytics project but relatively small for developing a highly reliable real-world home-price prediction system.

### Available Variables

The dataset contains only a limited set of property characteristics.

Important factors that may influence home prices are not represented, such as:

* lot size
* property condition
* renovation history
* school districts
* property location at a more detailed geographic level
* local market conditions
* interest rates
* comparable nearby sales
* amenities

The absence of these variables limits the model's ability to explain differences in home prices.

### Generalization

Results from this dataset should not automatically be generalized to other housing markets, geographic regions, or time periods.

Housing prices are strongly influenced by local economic and geographic conditions.

### Correlation and Causation

Relationships identified through exploratory analysis and regression should not automatically be interpreted as cau


[◄ Back to Home](index.md)
