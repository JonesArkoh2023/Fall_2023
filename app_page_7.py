import pandas as pd
import streamlit as st

def app_page_7(): 
    st.markdown('<h1 style="color: #008080;">Model Evaluation and Development</h1>', unsafe_allow_html=True) 
    
# Subtitle style (bold)
    subtitle_style = "<strong style='color: #008080;'>{}</strong>"


    model_eval = """
    <div style="text-align: justify">
    {}
Model evaluation involves evaluating the performance of the model using various metrics and comparing it to other models. The model is evaluated using various metrics such as accuracy, precision, and recall to determine its effectiveness. In the model training, we use linear regression analysis to train the data for the relationship we are exploring. That is the association between acceptance rate in the HBCU, the type of HBCU and the level of enrollment in the HBCU.

We use the R square, the significance level and the size of the estimate as the parameter in checking the performance of the linear regression model (OLS). We achieved this by generating new features, the dummy of the acceptance rate and the natural logarithm of the enrollment variable. Now, as part of model evaluation, we can employ other estimation techniques to check the strength of this relationship among acceptance rate, the type of HBCU and the level of enrollment, particularly, since the linear regression assumes a linearity among the variables. Thus, we can employ model that can handle non-linearity and allow for other form of relationship to exist among the variables. We can use random forest algorithm or decision trees to train and evaluate the same data and compare it with the linear regression model.
     </div>
"""
    st.markdown(model_eval .format(subtitle_style.format("Model Evaluation")), unsafe_allow_html=True)
    
    
    
    
    model_dep = """
    <div style="text-align: justify">
    {} 
Model Develoment involves deploying the model into a production environment, such as a web application or a database. In this particular example of HBUC data, we can deploy this model to explain the relatioinship acceptance rate, type of HBCU and the level of enrollment in other regions of the united states as this data is particular based on Northeast and Southeast region of the country. In this model is able to predict a similar pattern that accetance rate below 90 percent and type of HBCU are crusial in determining the enrollment, then, this model is efficient in explaining the relationship.

The next phase will be left in the house of policy makers to adopt this model in first, encouraging the enrollment in HBCUs, bridging the gap between the public and private HBCUs to boost enrollment and similar measures that will aid the expansion of HBCUs in the United States.
     </div>
"""
    st.markdown(model_eval .format(subtitle_style.format("Model Evaluation")), unsafe_allow_html=True)
    
    

if __name__ == "__main__":
    app_page_6()