import streamlit as st
import pandas as pd
import pyodbc


st.title("👁️Welcome to the Data page")
st.write("Here you can view the data. Add your data viewing functionality here.")

# Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=dap-projects-database.database.windows.net;'
    'DATABASE=dapDB;'
    'UID=LP2_project;'
    'PWD=Stat$AndD@t@Rul3;'
)

# Query the data
query = "SELECT * FROM dbo.LP2_Telco_churn_first_3000"
df = pd.read_sql(query, conn)

# Display data
st.write(df)

# Close the connection
conn.close()