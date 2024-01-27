# Hybrid-based Book Recommendation System

## Content

1. [Project Overview](#project-overview)
   - [System Components](#system-components)
2. [Data Exploration and Cleaning](#data-exploration-and-cleaning)
3. [Content-Based Recommendation System](#content-based-recommendation-system)
4. [Collaborative Filtering Recommendation System](#collaborative-filtering-recommendation-system)
5. [Web Application](#web-application)
6. [How to Clean and Start the App](#how-to-clean-and-start-the-app)
7. [Developer Information](#developer-information)

---

## Project Overview

The Hybrid-based Book Recommendation System encompasses an end-to-end development process, incorporating data exploration, cleaning, and the implementation of both content-based and collaborative filtering recommendation systems using Python.

For a detailed walkthrough, please refer to the project article: [Book Recommendation System](https://medium.com/@abdelrahman.m2922/book-recommendation-system-fa510e2d5a24).

![RS1](https://github.com/Veto2922/hybrid-based-book-recommender-systems/assets/114834171/4879f6fc-6e3b-4749-b41e-f94b36ac0329)

![RS2](https://github.com/Veto2922/hybrid-based-book-recommender-systems/assets/114834171/bc9c011d-4c38-4108-9c63-156e7f4bac58)


## Project block diagram:
![Block digram](https://github.com/Veto2922/hybrid-based-book-recommender-systems/assets/114834171/3646c290-647b-4802-97c2-341a1eaa01eb)


### System Components

1. **Data Exploration and Cleaning:** Involves preprocessing steps to ensure data quality and relevance by filtering out noise and enhancing dataset integrity.
2. **Content-Based Recommendation System:** Engages in feature engineering to uncover book popularity metrics and constructs a similarity matrix using cosine similarity for personalized recommendations.
3. **Collaborative Filtering Recommendation System:** Conducts feature engineering to optimize collaborative filtering, exploring different models such as ALS (Alternating Least Squares), and implements prediction functions for personalized book recommendations.
4. **Web Application:** Develops a Streamlit application to integrate recommendation systems, offering a user-friendly interface for users to explore top books and receive personalized recommendations.

## Data Exploration and Cleaning

The project utilizes a subset of books available on Amazon, including user ratings and information compiled by Cai-Nicolas Ziegler in 2004. The dataset comprises three tables: users, books, and ratings, with explicit ratings ranging from 1 to 10 and implicit ratings expressed as 0.

Data Source:
https://www.kaggle.com/datasets/saurabhbagchi/books-dataset/data

## Content-Based Recommendation System

Feature engineering is employed to unveil book popularity metrics, and a similarity matrix using cosine similarity is constructed to provide recommendations for new users based on book similarity.

## Collaborative Filtering Recommendation System

Feature engineering optimizes collaborative filtering, exploring different models like ALS. A user-item matrix captures user preferences, enabling the implementation of prediction functions for personalized book recommendations.

## Web Application

A Streamlit application is developed to integrate recommendation systems, providing a user-friendly interface for users to explore top books and receive personalized recommendations based on their preferences and interactions.

### How to Use

1. **New User**: View top books and receive recommendations based on popular choices.
2. **Old User**: Receive personalized recommendations based on your profile and past interactions.

### How to Clone and Start the App

### Important Notes:

After downloading the project, you must add a file called Data, download the data from the main source, put it in a file called Raw, and create a second file called Processing. All of this is inside the data file with the same outline:

```
├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
```

Make sure you are using Python v == 3.7.16.

After that, you must restart all the notebooks inside the notebooks file and add any file that does not exist for the project to work correctly (note that the reason for not uploading these files is their large size, with space restrictions in GitHub).

To Clone and start the application, follow these steps:

1. **Clone the Repository**:

    ```
    git clone https://github.com/Veto2922/hybrid-based-book-recommender-systems.git
    ```

2. **Navigate to the Project Directory**:

    ```
    cd hybrid-based-book-recommender-systems
    ```

3. **Install Requirements**:

    ```
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```
    streamlit run app.py
    ```

## Developer Information

- **Developer**: Abdelrahman Mohamed
- **LinkedIn**: [Abdelrahman Mohamed](https://www.linkedin.com/in/abdelrahman-mohamed-28649120b/)
- **GitHub**: [Veto2922](https://github.com/Veto2922/hybrid-based-book-recommender-systems)

Thank you for using the Hybrid-based Book Recommendation System! 📚

## Project Organization

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
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
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

```

---

Project based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/). #cookiecutterdatascience
