import streamlit as st 
st.set_page_config(
    page_title="Home Page",
    page_icon="🏡",
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
- Read data from SQL Server
- Select the features for classification
- This app also provide a comprehensive report on the performance of the model
- The app provides interactive charts for feature importance and churn probability
""")


# App features
st.subheader("App Features")
st.markdown("""
1. **Home page**
2. **View Data**           
3. **Dashboard**
4. **Prediction**
""")


# How to run the app
st.subheader("How to run Churn App")
st.code(""" 
        # activate virtual environment
        venv/Scripts/activate
        streamlit run app.py
        """, language= 'python')


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
st.markdown("For collaboration contact Team Fiji")
st.button("Repository on Github")
