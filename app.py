import streamlit as st
from src.models.content_base.con_b_predict_model import get_top_n_books, recommmendation_by_id
from src.models.CF.CF_predict_model import get_CF_n_recommendations , get_user_profile , get_random_user_id

MODEL = r'models\CF\FInal_model.pkl'

def main():
    st.set_page_config(layout="wide")

    # Header
    # st.title('📚 Book Recommendation System')
    st.markdown(
        """
        <h1 style='text-align: center; color: blue;'>📚 Hybrid based Book Recommendation System</h1>
        """,
        unsafe_allow_html=True
    )
    st.info('If you choose "new user," the rank and content-based recommendation system will work. If you choose "old user," the system will choose a random user ID from our database, and then the collaborative filtering recommendation will work.')
    st.markdown("---")

    # Instructions Section
    st.sidebar.title('ℹ️ How to Use')
    st.sidebar.markdown("""
        1. **New User**: See top books and recommendations.
        2. **Old User**: Get personalized recommendations based on your profile.
        """)

    # Display based on user type
    user_type = st.radio("Are you a new user or an old user?", ("New User", "Old User"))

    if user_type == "New User":
        # Display top books
        st.title('Top Books')
        num_columns = 6
        columns = st.columns(num_columns)

        for index, row in get_top_n_books(n=30).iterrows():
            with columns[index % num_columns]:
                st.image(row['Book_image'], caption=row['Title'], use_column_width=True)
                st.write(f"**Year of Publication:** {row['Publication_year']}")
                st.write(f"**Author:** {row['Author']}")
                if st.button(row['Title'], key=f"button_{index}"):
                    selected_book_id = row['ISBN']
                    recommendations = recommmendation_by_id(selected_book_id)

                    if recommendations is not None:
                        st.sidebar.title(f":red[Books similar to {row['Title']} :] ")
                        for _, rec_row in recommendations.iterrows():
                            st.sidebar.image(rec_row['Book_image'], caption=rec_row['Title'], use_column_width=True)
                            st.sidebar.write(f"**Year of Publication:** {rec_row['Publication_year']}")
                            st.sidebar.write(f"**Author:** {rec_row['Author']}")
                            st.sidebar.markdown("---")
                    else:
                        st.warning('Invalid book ID. Please enter a valid book ID.')

    elif user_type == 'Old User':
        user_id = get_random_user_id()
        st.write('Hello ' , user_id)
        st.title('Recommended Books')
        num_columns = 6
        columns = st.columns(num_columns)

        for index, row in get_CF_n_recommendations(user_id, n=30).iterrows():
            with columns[index % num_columns]:
                st.image(row['Book_image'], caption=row['Title'], use_column_width=True)
                st.write(f"**Year of Publication:** {row['Publication_year']}")
                st.write(f"**Author:** {row['Author']}")
                st.write(f"**Predicted Rating:** {round(row['pred_rating'], 2)}")

        st.sidebar.title(f":red[Books you have read and rated before :] ")
        for _, rec_row in get_user_profile(user_id).iterrows():
            st.sidebar.image(rec_row['Book_image'], caption=rec_row['Title'], use_column_width=True)
            st.sidebar.write(f"**Year of Publication:** {rec_row['Publication_year']}")
            st.sidebar.write(f"**Author:** {rec_row['Author']}")
            st.sidebar.write(f"**Your rating:** {rec_row['Usrt_rating']}")
            st.sidebar.markdown("---")

    # Footer and Additional Info
    st.markdown("---")
    st.markdown("Developed by Abdelrahman Mohamed")
    st.markdown('---')
    st.subheader('🚀 For more info about this project:')
    st.markdown('[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abdelrahman_Mohamed-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/abdelrahman-mohamed-28649120b/) [![GitHub](https://img.shields.io/badge/GitHub-Veto2922-darkgreen?style=flat&logo=github)](https://github.com/Veto2922/Movie-Recommender-System-content-based-)')

    if st.button('🚀 Show Support'):
        st.balloons()

    if st.button('🚀 Star on GitHub'):
        st.write('⭐️ Thank you for your support!')

if __name__ == '__main__':
    main()
