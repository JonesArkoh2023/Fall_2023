import pandas as pd
import plotly.express as px
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import statsmodels.api as sm
import numpy as np
import streamlit as st

def app_page_6(): 
    st.markdown('<h1 style="color: #008080;">Model Training</h1>', unsafe_allow_html=True) 
    
    st.markdown("""
    <div style="text-align: justify"> 
We note from data exploration and preparation that acceptance rate, enrollment and type of HBCU are correlation. In the next data science process, i.e. model trainng, we are going to build a linear regression model using these three variables

Particulary, we will show the differences in model performance when we use the original variables (Non-transformed) versus the new features that we engineered; the dummy of the acceptance rate and the natural logarithm of the enollment variable")
    </div>
""", unsafe_allow_html=True)

    # Importing the data 
    hbcus_1 = pd.read_csv('hbcus_2018.csv')    
    # Drop missing values
    hbcus_2 = hbcus_1.dropna()
    
    
# Perform operations
    def accept_cat(rate):
        return 1 if rate < 90 else 0
    hbcus_3 = hbcus_2.copy()
    #hbcus_3_cc = hbcus_3.copy()
    hbcus_3.loc[:,'accept_cat'] = hbcus_3['acceptance_rate'].apply(accept_cat)

    hbcus_4=hbcus_3.copy()
    hbcus_4.loc[:,'ln_Enrollment'] = np.log(hbcus_4['Enrollment'])

    st.title("Linear Regression Analysis")
    st.subheader("Model 1: Non Transformed variables")
    st.markdown("""
    <div style="text-align: justify">
    The simple linear regression shows that the explained variables in the model is about 6%. All else equal, a 1% increase in acceptance rate  decrease enrollment by approxiately 16, which is significat at 5%. We can see the the skewness of the data is about 1.3.
    </div>
""", unsafe_allow_html=True)

    
    hbcus_5 = hbcus_4.copy()
    X = sm.add_constant(hbcus_5['acceptance_rate'])
    y = hbcus_5['Enrollment']
    # Fit the linear regression model
    model_1 = sm.OLS(y, X).fit(cov_type='HC3')
    # Print the regression summary in Streamlit app
    st.subheader('Regression Summary')
    st.text(model_1.summary())


    st.subheader("Model 2: Transformed acceptance rate (Dummy) and Level Enrollment")
    st.markdown("""
    <div style="text-align: justify">
    We see a significant change in the direction of associatioins and the level of significance. We also see an improvement in the model performance when we comapred the R square estimates of the Model 1 and Model 2.
    </div>
""", unsafe_allow_html=True)    
    
    a = sm.add_constant(hbcus_5['accept_cat'])
    n = hbcus_5['Enrollment']
    # Fit the linear regression model
    model_2 = sm.OLS(n, a).fit(cov_type='HC3')
    # Print the regression summary in Streamlit app
    st.subheader('Regression Summary')
    st.text(model_2.summary())

    st.subheader("Model 3: Both Transformed variables")
    st.markdown("""
    <div style="text-align: justify">
    After taking natural logarithm of the enrollment variable due to skewness, the acceptance rate explains enrollment about 11% of the variations. Again, all else equal, a 1% increase in acceptance rate decreases enrollment about 12% points for HBCUs with less than 90 percent acceptance rate which is significant at 1% alpha level. The result shows that the model skewness has improve dramatically. Standard errors are also heteroscedatically robust. That is the assumption of idd is relaxed.
        </div>
""", unsafe_allow_html=True)
    
    b = sm.add_constant(hbcus_5['accept_cat'])
    k = hbcus_5['ln_Enrollment']
    # Fit the linear regression model
    model_3 = sm.OLS(k, b).fit()
    # Print the regression summary in Streamlit app
    st.subheader('Regression Summary')
    st.text(model_3.summary())

    st.subheader("Model 4: Both Transformed variables and Type of HBCU")
    st.markdown("""
    <div style="text-align: justify">
There are few observation from the regression analysis. First, the model Enrollment and acceptance_rate has an R square of about 6% which significantly and acceptance_rate was negatively associated with Enrollment. The second model with Enrollment and accept_cat had an increase in R square (14%) and positive association between Enrollment and acceptance. This show an improvement in acceptance rate explaining enrollment. Then, we took natural logarithm of the Enrollment to cater to extreme values and we saw that the linear regression of acceptance_rate and Enrollment changed from 6% to 11 and that of accept_cat on Enrollment is about 19%. After adding the type of HBUC into the model, we note that the R square increased from 19% to about 50%.

That is acceptance rate and type of HBCU explains about 50% of variations in enrollment. We note that all else equal, if the HBCU has acceptance rate less than 90%, enrollment increae about 80% when compared with HBCUs with acceptance rate 90 percent and above and the result is significant at 1% alpha level. If the type of HBCU is public, Enrollment increase about 100% when compared with the private HBCUs. Although this analysis interestsing, we cannot assume causality as many factors that might affect enrollment HBCUs are not just acceptance_rate and the Type. But we can conclude that acceptance and Type of HBCU has a strong association with Enrollment in HBCUs.
    </div>
""", unsafe_allow_html=True)
                    
    hbcus_6=hbcus_5.copy()
    hbcus_6['Type']=hbcus_6['Type'].astype('category')
    hbcus_6 = pd.get_dummies(hbcus_6, columns=['Type'], prefix='Type', drop_first=True)

    hbcus_6['Type_Public']=hbcus_6['Type_Public'].astype('int')

    # Combine 'accept_cat' and 'Type' dummy variables
    c = sm.add_constant(hbcus_6[['accept_cat', 'Type_Public']])  
    d = hbcus_6['ln_Enrollment']
    # Fit the linear regression model
    model_4 = sm.OLS(d, c).fit()  

 # Print the regression summary in Streamlit app
    st.subheader('Regression Summary')
    st.text(model_4.summary())




if __name__ == "__main__":
    app_page_6()