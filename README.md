# A Churn Prediction on an Iranian Telco's Customers

![header.png](assets/header.png)
*Image by [freepik](https://www.freepik.com/free-photo/collage-customer-experience-concept_25053721.htm#fromView=search&page=1&position=7&uuid=f75c616d-0c0a-4544-8617-b8f768f38775).*

## Dataset

The dataset originally came from the [Iranian Churn Dataset](https://archive.ics.uci.edu/dataset/563/iranian+churn+dataset) from UC Irvine Machine Learning Repository (License: CC BY 4.0).

## Introduction

I have always been fascinated by observing people's behaviors and decision making. This interest becomes even more captivating when expanded to a larger scale, say, to uncover patterns within a group.

Customer churn analysis presents a unique opportunity to delve into customer behaviors through data. By examining why customers leave a service, we can gain valuable insights into their preferences and pain points (for the company). This project excites me because it combines my passion for behavioral analysis with the power of data science.

## Objectives

The main objective of this project is: 

> **To perform EDA on churn data to develop insights about the telco company's reasons for churning and make a churn prediction model.**

To achieve this objective, I broke it down to 3 smaller objectives:

1. Look at the individual distributions of the numerical features like call fails and subscription length.
2. Perform bivariate analysis on indepedent variables vs. target feature 'churn' using violin plots and bar charts, and identify which features are best for the model.
3. Construct a model that predicts if a customer is going to churn.

## Methodology

1. **Data Cleaning**: Ensure the dataset is free from missing values and inconsistencies.
2. **Exploratory Data Analysis**: Use statistical methods and visualizations to explore the data.
3. **Feature Analysis**: Soon!
4. **Modeling**: Also soon.

## Main Insights

From the exploratory data analysis, we discovered the following insights from the dataset:

* **Churn Rate**: 1 out of 6 customers have churned from the telco service.
* **Important Numerical Predictors**: Charged amount, total call length, call frequency, SMS frequency, unique contacts called, and customer value are potentially important predictors of customer churn.
* **Important Categorical Predictors**: Complained, tariff plan, account status, and age bracket (treated as ordinal categories) are identified as significant categorical predictors of churn.
* **Multicollinearity**: Multicollinearity is present among the numerical features, suggesting that feature combination or reduction would be a beneficial approach moving forward.

## Author

* [**Marco Lacsa Cuadra**](https://github.com/mlcuadra1)