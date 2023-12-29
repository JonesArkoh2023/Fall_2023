from app_page_1 import app_page_1
from app_page_2 import app_page_2
from app_page_3 import app_page_3
from app_page_4 import app_page_4
from app_page_5 import app_page_5
from app_page_6 import app_page_6
from app_page_7 import app_page_7
import streamlit as st

pages = {
    "Overview": app_page_1,
    "Data Collection": app_page_2,
    "Data Cleaning": app_page_3,
    "Data Exploration": app_page_4,
    "Data Preparation": app_page_5,
    "Model Training": app_page_6,
    "Model Evaluation and Development": app_page_7,
}

st.sidebar.title('Data Science Processes')
select_pages = st.sidebar.selectbox("Navigate the process", list(pages.keys()))

pages[select_pages]()