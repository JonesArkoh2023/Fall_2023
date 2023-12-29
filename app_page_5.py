import pandas as pd
import plotly.express as px
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import statsmodels.api as sm
import numpy as np
import streamlit as st

def app_page_5():
    st.markdown('<h1 style="color: #008080;">Data Preparation</h1>', unsafe_allow_html=True) 
    st.markdown("<h2 style='color: #800080;'>Introduction</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: justify">
    During the data exploration, we note that the correlation between acceptance rate and enrollment is negative. This negative correlation intuitively does not make sense. Again, we note from the scatter plot that there are many schools that have 100% acceptance rate which was stacked at the 100 percent line. Thus, we can engineer a new feature where if the acceptance rate is less than 90, we grouped such schools into one category, if else is 90 percent or greater, then, we form another category.")
    Further, we noted from the data exploration that the HBCU enrollment are in thousands. This large values may affect the performance of our model during training the data set. Therefore, we will take a quick display of the enrollment variable and transform this data into meaning values for the training of our data set. Specifically, we will take a natural logarithm of the enrollment variable to cater for extreme and large values in the data.
    </div>
""", unsafe_allow_html=True)


    hbcus_1 = pd.read_csv('hbcus_2018.csv')    
    # Drop missing values
    hbcus_2 = hbcus_1.dropna()
    st.write(hbcus_2.head())

# Display code
    st.subheader("Generating a New Feature-A Dummy of acceptance rate")
    code = '''
    def accept_cat(rate):
        return 1 if rate < 90 else 0
    hbcus_3_cc = hbcus_3.copy()
    hbcus_3_cc.loc[:, 'accept_cat'] = hbcus_3_cc['acceptance_rate'].apply(accept_cat)
    '''
    st.code(code, language='python')
    
# Perform operations
    def accept_cat(rate):
        return 1 if rate < 90 else 0
    hbcus_3 = hbcus_2.copy()
    #hbcus_3_cc = hbcus_3.copy()
    hbcus_3.loc[:,'accept_cat'] = hbcus_3['acceptance_rate'].apply(accept_cat) 
    

# Let test if the correlation iaccept_cat'
    st.subheader("Correlation Analysis")
    corrb = hbcus_3['accept_cat'].corr(hbcus_3['Enrollment'])
    st.write(f"The correlation coefficient is: {corrb:.2f}")


    st.title('Enrollment Distribution')
    st.subheader('Histogram of Enrollment')
    hist_values = hbcus_3['Enrollment']

    # Create a histogram using Matplotlib
    fig, ax = plt.subplots()
    ax.hist(hist_values, bins=20, alpha=0.7) 
    ax.set_xlabel('Enrollment')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)
    
    st.subheader("Generating a New Feature-Natural Logarithm")
    code = '''
    hbcus_4.loc[:,'ln_Enrollment'] = np.log(hbcus_4['Enrollment'])
    '''
    st.code(code, language='python')

    hbcus_4=hbcus_3.copy()
    hbcus_4.loc[:,'ln_Enrollment'] = np.log(hbcus_4['Enrollment'])

    st.subheader('Histogram of Enrollment Normalized')
    hist_values_l = hbcus_4['ln_Enrollment']

    # Create a histogram using Matplotlib
    fig_1, ax = plt.subplots()
    ax.hist(hist_values_l, bins=20, alpha=0.7) 
    ax.set_xlabel('ln_Enrollment')
    ax.set_ylabel('Frequency')
    st.pyplot(fig_1)




if __name__ == "__main__":
    app_page_5()