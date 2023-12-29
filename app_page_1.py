import streamlit as st
import numpy as np
import pandas as pd

def app_page_1():

    # Title and Authors
    st.markdown("""
    <div style="text-align: justify">
        <h1 style="color: #008080;">A Demonstration of the Data Science Process using Historically Black Colleges and Universities (HBCUs) Data with Python and Streamlit App</h1>
    </div>
""", unsafe_allow_html=True)

    authors = "Authors: Chiehhsiung Chang, Kerneka Waldron, Naiya Jackson, Sally Amankwah, Jones A. Paintsil"
    st.markdown(f"<p>{authors}</p>", unsafe_allow_html=True)

# Introduction
    st.markdown("""
    <div style="text-align: justify">
        <h2 style='color: #800080;'>Introduction</h2>
        Data science is a multidisciplinary field that uses scientific methods, mathematical models, algorithms, and systems to explore patterns in data, both structured and unstructured, to provide helpful information for policymakers, business corporations, medicine, and almost all aspects of life. Data science processes start with data collection. There are seven data science processes. They are data collection, data cleaning, data exploration, data preparation, model training, model evaluation, and model deployment. In this exercise, we employed the 2018 HBCU dataset to show the various procedures involved in executing the data science processes.
    </div>
""", unsafe_allow_html=True)



    # Executive Summary
    st.markdown("<h2 style='color: #800080;'>EXECUTIVE SUMMARY</h2>", unsafe_allow_html=True)
    
    
    sub_style = "<strong style='color: #008080;'>{}</strong>"
    title = """
    {}
Determinants of Enrollment in Historically Black Colleges and Universities (HBCUs)
    """
    st.markdown(title.format(sub_style.format("Title")), unsafe_allow_html=True)

    objective = """
    {}
Examines the relationship between acceptance rate and Enrollment. 
Investigate whether the type of HBCUs impacts the acceptance rate and enrollment. 
Also, explore if significant relationships are prominent.
    """
    st.markdown(objective.format(sub_style.format("Objectives")), unsafe_allow_html=True)

    ds_source="""
    {}
A sub-sample of 2018 HBCUs dataframe with 100 observations.
"""
    st.markdown(ds_source.format(sub_style.format("Data Source")), unsafe_allow_html=True)

    # Main Findings
    st.markdown("<h3 style='color: #800080;'>Main Findings</h3>", unsafe_allow_html=True)
    
    findings_text = """
    <div style="text-align: justify">
    First, the model with Enrollment and acceptance rate (discrete variable) has an R square of about 6%, which is significant but negatively associated with Enrollment. The second model with Enrollment and acceptance rate (dummy variable) had an increase in R square (14%) and a positive association between Enrollment and acceptance. This shows an improvement in acceptance rate positively explaining enrollment in HBCUs. Then, we took the natural logarithm of the Enrollment to cater to extreme values and found that the linear regression of acceptance rate (discrete variable) and Enrollment changed from 6% to 11%, and that of acceptance rate (dummy variable, a feature engineered) on Enrollment is about 19%. After adding the type of HBCU into the model, we noted that the R square increased from 19% to about 50%. That acceptance rate and type of HBCU explain about 50% of variations in enrollment. We find that all else equal, if the HBCUs have an acceptance rate less than 90% (a feature engineered), enrollment increases about 80% when compared with HBCUs with an acceptance rate of 90 percent or greater, and the result is significant at a 1% alpha level. If the type of HBCU is public, Enrollment increases about 100% when compared with the private HBCUs. Although this analysis is interesting, we cannot assume causality as many factors that might affect enrollment HBCUs are not just acceptance rate and the Type.
    </div>
    """
    st.markdown(f"<p style='color: black;'>{findings_text}</p>", unsafe_allow_html=True)

    # Conclusion
    st.markdown("<h3 style='color: #800080;'>Conclusion</h3>", unsafe_allow_html=True)
    conclusion_text = """
    We can conclude that acceptance and Type of HBCU have a strong association with Enrollment in HBCUs in the US.
    """
    st.markdown(f"<p style='color: black;'>{conclusion_text}</p>", unsafe_allow_html=True)



# Main title style
    main_title_style = "<h2 style='color: #800080;'>{}</h2>"

# Subtitle style (bold)
    subtitle_style = "<strong style='color: #008080;'>{}</strong>"



# Data Science Processes content
    st.markdown(main_title_style.format("The Data Science Processes"), unsafe_allow_html=True)

    data_collection = """
    <div style="text-align: justify">
    {}
    The first step in the data science process is data collection. This involves gathering data from various sources, using libraries such as Pandas, Numpys or databases such as APIs, web scraping, or surveys. These libraries enable data scientists to import data from files (e.g., CSV, Excel), databases, or web APIs. Additionally, Python provides tools for web scraping, allowing data scientists to extract data from websites.
     </div>
"""
    st.markdown(data_collection.format(subtitle_style.format("Data Collection")), unsafe_allow_html=True)

    data_cleaning = """
    <div style="text-align: justify">
    {}
    Once the data is collected and imported, the next step is data cleaning. This is necessary because most of the data collected is raw, unstructured and unfiltered. Data cleaning is the process of addressing issues in the data such as missing values, duplicates and null values, outliers, inconsistencies, invalid entries, and improper formatting. This involves preprocessing the data to ensure that it's accurate, complete, and consistent. This includes tasks such as removing duplicates, filling in missing values, and standardizing the format. Python offers tools for data cleaning, including the Pandas library, which provides functions for handling missing data, removing duplicates, and transforming data into a suitable format.
    </div>
"""
    st.markdown(data_cleaning.format(subtitle_style.format("Data Cleaning")), unsafe_allow_html=True)

    data_exploration= """
    <div style="text-align: justify">
    {}
    Data Exploration The third step in the data science process is data exploration. This involves exploring the data to gain a better understanding of its characteristics, such as its distribution, correlation, and outliers. This involves gaining a deeper understanding of the dataset through descriptive statistics, data visualization, and exploratory data analysis (EDA). Python's libraries, such as Matplotlib, Seaborn, and Plotly, enable data scientists to create visualizations that reveal patterns, trends, and relationships within the data.
    </div>
"""
    st.markdown(data_exploration.format(subtitle_style.format("Data Exploration")), unsafe_allow_html=True)

    data_prep="""
    <div style="text-align: justify">
    {}
Data Preparation The fourth step in the data science process is data preparation. Data preparation involves selecting and transforming the features that will be used in the analysis. This includes tasks such as feature engineering, normalization, and dimensionality reduction.
</div>
"""
    st.markdown(data_prep.format(subtitle_style.format("Data Preparation")), unsafe_allow_html=True)

    model_train="""
    <div style="text-align: justify">
    {}
        Model Training The fifth step in the data science process is model training. This involves selecting the appropriate machine learning model and training it on the data.This process uses various algorithms and techniques, such as decision trees, logistic regression, and neural networks to develop a model that can accurately predict outcomes or classify data based on the input features. Model training is carried out using various machine learning algorithms implemented in libraries such as scikit-learn, XGBoost, and TensorFlow.
    </div>
"""
    st.markdown(model_train.format(subtitle_style.format("Model Training")), unsafe_allow_html=True)

    model_eval="""
    <div style="text-align: justify">
    {}
Model Evaluation The sixth step in the data science process is model evaluation. Model evaluation involves evaluating the performance of the model using various metrics and comparing it to other models. The model is evaluated using various metrics such as accuracy, precision, and recall determine its effectiveness. 
    </div>
"""
    st.markdown(model_eval.format(subtitle_style.format("Model Evaluation")), unsafe_allow_html=True)

    model_deployment = """
    <div style="text-align: justify">
    {}
    The final step in the data science process is model deployment. This involves deploying the model into a production environment, such as a web application or a database. Python frameworks like Flask or Django can be useful for building APIs, and libraries like TensorFlow Serving can facilitate model deployment.
    </div>
"""
    st.markdown(model_deployment.format(subtitle_style.format("Model Deployment")), unsafe_allow_html=True)


if __name__ == "__main__":
    app_page_1()
