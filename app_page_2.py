import pandas as pd
import streamlit as st

def app_page_2():
    st.markdown('<h1 style="color: #008080;">Data Collection</h1>', unsafe_allow_html=True)
    #st.title("Data Collection")

    st.markdown("<h1 style='color: #800080;'>Packages</h1>", unsafe_allow_html=True)
    st.markdown("<span style='color:#800080;'>Pandas</h1>", unsafe_allow_html=True)
    st.markdown("<span style='color:#800080;'>Streamlit</h1>", unsafe_allow_html=True)

    # Data Collection
     # Introduction
    st.markdown("<h2 style='color: #800080;'>Introduction</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: justify">
        Data collection is the process of gathering information from various sources using various research methods and organizing it into a single database or repository. The data collection process provides information that companies, organizations, and researchers use to track advancement, solve problems, and make decisions.
    </div>
""", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: justify">
        The two different approaches to collecting data are primary and secondary data collection. Primary data collection is the act of getting information directly from sources. One of the most important elements of primary data is that the researchers get direct communication with respondents. Secondary data collection is the process of gathering easily accessible information that has previously been obtained by another party. In this project, the main source of data is secondary. We employ the 2018 HBCU data for this analysis. The first and the last five rows of the data are displayed below.
    </div>
""", unsafe_allow_html=True)

    
    # Importing the data
    hbcus_1 = pd.read_csv('hbcus_2018.csv')
    
    # Button to toggle displaying data
    if st.button("Data"):
        # Display first 5 rows of the dataset
        st.subheader("First 5 rows of the dataset:")
        st.write(hbcus_1.head())

        st.subheader("Last 5 rows of the dataset:")
        st.write(hbcus_1.tail())
# Call the function to run the Streamlit app
if __name__ == "__main__":
    app_page_2()
