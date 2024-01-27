# Hypier-based Book Recommendation System

## Content

1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
   - [System Components](#system-components)
3. [Data Exploration and Cleaning](#data-exploration-and-cleaning)
4. [Content-Based Recommendation System](#content-based-recommendation-system)
5. [Collaborative Filtering Recommendation System](#collaborative-filtering-recommendation-system)
6. [Web Application](#web-application)
7. [Conclusion](#conclusion)

---

## Introduction
Book recommendation systems are essential tools for enhancing user experience and guiding readers to discover relevant content in the vast world of available books. Hybrid-based systems, combining content-based and collaborative filtering techniques, have proven highly effective in providing personalized recommendations to users.

## Project Overview
The Hypier-based Book Recommendation System follows an end-to-end development process, incorporating data exploration, cleaning, and the implementation of both content-based and collaborative filtering recommendation systems using Python.

### System Components
1. **Data Exploration and Cleaning:** Involves preprocessing steps to ensure data quality and relevance by filtering out noise and enhancing dataset integrity.
2. **Content-Based Recommendation System:** Engages in feature engineering to uncover book popularity metrics and constructs a similarity matrix using cosine similarity for personalized recommendations.
3. **Collaborative Filtering Recommendation System:** Conducts feature engineering to optimize collaborative filtering, exploring different models such as ALS (Alternating Least Squares), and implements prediction functions for personalized book recommendations.
4. **Web Application:** Develops a Streamlit application to integrate recommendation systems, offering a user-friendly interface for users to explore top books and receive personalized recommendations.

## Data Exploration and Cleaning
The project utilizes a subset of books available on Amazon, including user ratings and information compiled by Cai-Nicolas Ziegler in 2004. The dataset comprises three tables: users, books, and ratings, with explicit ratings ranging from 1 to 10 and implicit ratings expressed as 0.

## Content-Based Recommendation System
Feature engineering is employed to unveil book popularity metrics, and a similarity matrix using cosine similarity is constructed to provide recommendations for new users based on book similarity.

## Collaborative Filtering Recommendation System
Feature engineering optimizes collaborative filtering, exploring different models like ALS. A user-item matrix captures user preferences, enabling the implementation of prediction functions for personalized book recommendations.

## Web Application
A Streamlit application is developed to integrate recommendation systems, providing a user-friendly interface for users to explore top books and receive personalized recommendations based on their preferences and interactions.

## Conclusion
The Hypier-based Book Recommendation System represents a comprehensive approach to enhancing user engagement and satisfaction in the domain of book recommendations. By combining content-based and collaborative filtering techniques, the system leverages user preferences and book features to deliver accurate and personalized recommendations. The integration of a web application further enhances accessibility, enabling users to discover new reads seamlessly. Overall, the system underscores the importance of leveraging advanced recommendation algorithms to enrich user experiences and promote engagement in the realm of book exploration.

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
