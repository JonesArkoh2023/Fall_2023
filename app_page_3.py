import pandas as pd
import streamlit as st

# Data cleaning
def app_page_3():
    # Data Collection
    # Importing the data
    hbcus_1 = pd.read_csv('hbcus_2018.csv')    
    st.markdown('<h1 style="color: #008080;">Data Cleaning</h1>', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #800080;'>Introduction</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: justify">
Data cleansing involves the process of locating missing, inaccurate, incomplete, or irrelevant data points and then removing, changing, or replacing the impure or coarse data. It entails finding erroneous or corrupt records in a record set, table, or database and fixing (or deleting) them. Interactive data cleansing can be done with data varying tools and packages. 

A data set ought to be consistent with other comparable data sets in the system after cleansing. This project, we identified a missing information in the data set. Particularly, three missing observations for the acceptance rate and enrollment and one missing information for the latitude and longitude. Since this missing observation invariably represents a small portion of the data set, we conveniently dropped these missing observations from the data. This cleaning in practicality should not affect the average of the acceptance rate and enrollment as well as all other variables in the data. Although, we may potentially drop a name of HBCU, a type of HBCU, and the state in which is located if it happens to be just the observation that we have dropped.
    </div>
""", unsafe_allow_html=True)
    
    # Determine the total number of columns in the data
    if st.button("Data Types"):
        names = hbcus_1.dtypes
        st.subheader("Data Types:")
        st.write(names)
    
    # Get the total number of observations
    if st.button("Total Observations"):
        total_obs = hbcus_1.shape[0]
        st.subheader("Total number of observations")
        st.write(f"The total number of observations in the dataset is {total_obs}")
    
    # Check for missing values
    if st.button("Missing Values"):
        st.subheader("Missing values:")
        st.write(hbcus_1.isnull().sum())
        st.write("The acceptance rate and enrollment have 3 missing observations each. Since the missing observations are not many, we can conveniently drop these observations without affecting our analysis. However, if the missing observations were many, there would be a trade-off between losing information. I expect that after dropping these observations, the total number of observations in the data should be 97.")
    
    # Drop missing values
    if st.button("Dropping Missing Values"):
        hbcus_2 = hbcus_1.dropna()
        null_check = hbcus_2.isnull().sum()
        total_obs_check = hbcus_2.shape[0]
        
        st.subheader("Dropping missing values:")
        st.write(null_check)  # Fixed variable name here (null_check)
        st.write(f"Checking the total number of observations after dropping missing values: {total_obs_check}")

# Call the function to run the Streamlit app
if __name__ == "__main__":
    app_page_3()
