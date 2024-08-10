import streamlit as st

st.set_page_config(
    page_title="Churn App",
    page_icon="📊",
    layout="wide"
)
# Main Content
st.title("Customer Churn Prediction")
st.markdown("""
            This app uses machine learning model to predict whether a customer will churn or not
            """)


# Key Features
st.subheader("Key Features")
st.markdown("""
- Upload CSV data file of company
- Select the features for classification
- From the dropdown choose a machine learning model of your choice
- This app also provide a comprehensive report on the performance of the model
- Metrics like accuracy score, precision, recall and f1-score are included in the report 
- The app provides interactive charts for feature importance and churn probability
""")


# menu jjj
st.subheader("App Features")
st.markdown("""
1. **View Data**: Access proprietary data
            
2. **Dashboard**: Explore interactive visuals for insights
""")

# Machine Learning Integration
st.subheader("Machine Learning Integration")
st.markdown("""
3. **Model Selection**: Choice of machine learning model
   **Prediction**: Individual customer prediction
   **Seamless Integration**: Integrate predictions into your workflow
   **Insights and Visualization**: Interactive charts and graphs 
""")


# Contact and Github Repository
st.subheader("Ask for Help")
st.markdown("For collaboration contact me at [victor.duah@azubiafrica.org]")
st.markdown("[connect](https://github.com/Victor-Osei)")
st.button("Repository on Github")
