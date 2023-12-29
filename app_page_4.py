import pandas as pd
import plotly.express as px
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import statsmodels.api as sm
import streamlit as st

def app_page_4():
    # Data Collection
    # Importing the data
    hbcus = pd.read_csv('hbcus_2018.csv')        
    # Drop missing values
    hbcus= hbcus.dropna()
    st.markdown('<h1 style="color: #008080;">Data Exploration</h1>', unsafe_allow_html=True)
    st.markdown("<h2 style='color: #800080;'>Introduction</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: justify">
Data exploration process involves the visualization of the data instead of traditional data management systems to comprehend the features and contents of a dataset. These attributes include the size of the data, its completeness and accuracy, and any potential relationships between the variables in the dataset.

In this project, we explored many visualizations. We employed maps, bar charts, scatter plots and histograms to help us understand the nature of the dataset. This process enables us to extract some features and ideas and potential correlations that exist in the columns and rows of the data. Below are the variants explorations carried out and the results of these explorations.
    </div>
""", unsafe_allow_html=True)
    
    #Checking the Distribution of the amount of HBCUs across the nation in 2018.
    st.subheader("A map of number of HBCUs by City in US")
    hbcu3 = hbcus.groupby(['City', 'Long', 'Lat'])['Name'].count().reset_index()
    st.markdown("""
    <div style="text-align: justify">
    Figure 1 show the map of the HBCUs in the data. We note from the map that the location of the HBCUs in this data are in the Northeast and Southeast of the country. One key importance from this observation is that after building our model, whether we can deploy the model to explain similar situation in the other regions of the United States. 
    </div>
""", unsafe_allow_html=True)
    
    fig = go.Figure(data=go.Scattergeo(
        lon=hbcu3['Long'],
        lat=hbcu3['Lat'],
        text=hbcu3['City'],
        mode='markers',
        marker=dict(color=hbcu3['Name'])
    ))
    fig.update_layout(title='Figure 1: Number of HBCUs By City', geo_scope='usa')
    
    # Display the map in Streamlit
    st.plotly_chart(fig)
    # Plotting a bar graph of the number of HBCUs in each state
    st.subheader("Plotting a bar graph of the number of HBCUs in each state")
    st.markdown("""
    <div style="text-align: justify">
    Figure 2 show the number of HBCUs in the States that are represented in ths data. From the Figure 2, we note that Alabama state has the highest number of HBCUs in this dataset, followed by North Carolina, Texas, and South Carolina
    </div>
""", unsafe_allow_html=True)
    hbcu_state_count = hbcus.groupby('State')['Name'].count().reset_index()
    fig2 = px.bar(hbcu_state_count, x='State', y='Name', text='Name', 
                  title="Figure 2: Number of HBCUs by State")
    fig2.update_traces(texttemplate='%{text}', textposition='outside', cliponaxis=False)
    
    # Display the bar graph in Streamlit
    st.plotly_chart(fig2)




# Acceptance rate by State and School
    st.subheader("Acceptance rate by State and School")
    hbcus_2=hbcus
    ppt2 = hbcus_2.groupby('State')['acceptance_rate'].transform("max") == hbcus_2['acceptance_rate']
    hrt1 = hbcus_2[ppt2][['State', 'Name', 'acceptance_rate']]
    st.write(hrt1)
    # Display the result in Streamlit
    st.write("As noted, HBCUs in Alabama have the highest acceptance rate. But delving into each respective HBCU in each state, many of them have a higher acceptance rate.")

    # Acceptance rate by Type of HBCU
    st.subheader("Acceptance rate by Type of HBCU")
    st.markdown("""
    <div style="text-align: justify">
    As noted, the acceptance rate in private HBCUs is approximately 3.5 percentage points higher than public HBCUs. The next question I want to ask is whether acceptance rate determines enrollment. That is, do the HBCUs with higher/lower acceptance rate experience higher/lower enrollment?
    </div>
""", unsafe_allow_html=True)
    mean_acceptance_rate = hbcus_2.groupby('Type')['acceptance_rate'].mean().reset_index()

    # Display the mean acceptance rates per type
    st.write(mean_acceptance_rate)
    
    # Plotting a pie chart
    st.subheader("Plotting a Pie Chart of Acceptance rate by Type of HBCU")
    st.markdown("""
    <div style="text-align: justify">
    Figure 3 shows the pie chart of the acceptance rate between public and private HBCUs. The important information here is that the acceptance rate of the private HBCUs are larger than the public HBCUs. We also note that the higher 100 percentage acceptance rate clustered at 100 can distort this observation
    </div>
""", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    ax.pie(mean_acceptance_rate['acceptance_rate'], labels=mean_acceptance_rate['Type'], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title("Figure 3: Acceptance rate by Type of HBCU")
    # Display the pie chart using Streamlit
    st.pyplot(fig)

    # Scatter Plots
    st.subheader("Scatter Plots of Acceptance rate and Enrollment")
    st.markdown("""
     <div style="text-align: justify">
Figure 4 shows that there is a negative relation between acceptance rate and enrollment. However, one key observation is that from zero percent to about 90 percent, there is nicely scattered data point. But since acceptance rate is bounded between zero and 100 percent, we see that many HBCUs have 100 percent acceptance rate. This clusting of data point at 100 percent may potentially be associated with the negative relationship observing between school acceptance rate and enrollment. Thus, we can engineer a new feature from this observation for further analysis.
   </div>
""", unsafe_allow_html=True)
    fig2x = px.scatter(hbcus_2, x='acceptance_rate', y='Enrollment', trendline="ols", title="Figure 4: Scatter plot with trend line")
    st.plotly_chart(fig2x)
    # Interpretation

   
    
    # Correlation analysis
    st.markdown("""
    <div style="text-align: justify">
    This is quite interesting to see a negative correlation between enrollment and acceptance rate. I will investigate further. But for now, let's go back a little to check which HBCUs have higher enrollment.")
    </div>
""", unsafe_allow_html=True)
    st.subheader("Correlation analysis")
    corrb = hbcus_2['acceptance_rate'].corr(hbcus_2['Enrollment'])
    st.write(f"The correlation coefficient is: {corrb:.2f}")
    
    
#Now, let plot acceptance and enrollment by state and type of HBCU and compare
# Enrollment and acceptance rate of HBCU by State and Type
    st.subheader("Enrollment and acceptance rate of HBCU by State and Type")
    st.markdown("""
     <div style="text-align: justify">
    We plot enrollment by type of the HBCU (public or private) by state. It looks like there are more enrollent in Public HBCUs than private HBCUs with only a exception in South Carolina and DC, where private enrollment are higher than public enrollment. We can also see that the bar charts are stacked by the number of schools/colleges in each state. Is where a way we can show this?
   </div>
""", unsafe_allow_html=True)
    fig5x=px.bar(hbcus_2, x='State', y='Enrollment', color='Type', title='Figure 5: Enrollment of HBCUS by State and Type')
    st.plotly_chart(fig5x)
    
    st.markdown("""
    <div style="text-align: justify">
We note that in general, acceptance rate in private HBCU appear to be higher than public HBCUs. With exception of Alabama public HBCUs, the acceptance rate in the remaining HBCUs are comparatively smaller than private HBCUs. This is confirmed where the median private acceptance rate is approximately 65 % and that of the public is 60%. On the contrary that enrollment in the public HBCUs are comparatively higher than private HBCUs. This is true as the median average enrollment in public HBCUs is 2307 and that of the private HBCUs is about 900 which is a significant difference. Another important information worth mentioning is that some states have higher acceptance rate and enrollment than others. Some list include Alabama, North Carolina, Taxes, Georgia, Mississippi, South Carolina etc.
    </div>
""", unsafe_allow_html=True)

    fig6=px.bar(hbcus_2, x='State', y='acceptance_rate', color='Type', title='Figure 6: Acceptance of HBCUS by State and Type')
    st.plotly_chart(fig6)
 

# Call the function to run the Streamlit app
if __name__ == "__main__":
    app_page_4()
