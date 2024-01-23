import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


import joblib
import requests



FILTERD_BOOKS = r'models\content base\filtired_books_cb.pkl'
SIM_MATRIX = r'models\content base\similarity_matrix_cb.pkl'



books_df = pd.read_csv(FILTERD_BOOKS)
sim_martix = joblib.load(SIM_MATRIX)



def get_top_n_books(n):
    '''
    This fun return books recommendation based on popularity
    '''
    df = books_df.sort_values(by=['Rating_count', 'Avg_rating'], ascending=False).head(n)
    return df

# print(get_top_n_books( n = 20))





def recommmendation_by_id(book_id):   

    try: 
        recomm_movies= pd.DataFrame(sim_martix[book_id].sort_values(ascending=True).head(10)).reset_index()[1:]
        recom_df = pd.DataFrame(columns=books_df.columns)
        for title in recomm_movies['Title']:
            recom =  books_df[books_df['Title'] == title] 
            recom_df = pd.concat([recom_df , recom])
        return recom_df
    except KeyError:
        print('Book not found in the similarity matrix. Please choose another book.')

print(recommmendation_by_id('1567407781'))