import streamlit as st
import pandas as pd
import plotly.express as px
import requests

url = "https://backend-5glg.onrender.com/get_all"
response = requests.get(url)
data = response.json()

# Streamlit app
st.title("Admin Dashboard")

# Select user
user_id = st.selectbox("Select User", list(data.keys()))

# Display user information
st.subheader("User Information")
user_data = data[user_id]
st.write(f"Customer ID: {user_data['customer_id']}")
st.write(f"Customer Name: {user_data['customer_name']}")
st.write(f"Gender: {'Male' if user_data['gender'] == 'm' else 'Female'}")

# Display account information
st.subheader("Account Information")
account_data = user_data["account"]
for acc_number, acc_details in account_data.items():
    st.write(f"Account Number: {acc_number}")
    st.write(f"Balance: {acc_details['balance']}")
    st.write(f"Last Active Date: {acc_details['last_active_date']}")
    st.write(f"Open Date: {acc_details['open_date']}")

# Display transactions
st.subheader("Transactions Visualization")

# Prepare transaction data for plotting
transaction_data = acc_details["transaction"]
transaction_df = [
    {
        "Transaction Number": trans_number,
        "Amount": trans_details["amount"],
        "Description": trans_details["transaction_description"],
        "Timestamp": trans_details["transaction_timestamp"],
    }
    for trans_number, trans_details in transaction_data.items()
]
transaction_df = pd.DataFrame(transaction_df)

# Line chart for transactions
fig = px.line(
    transaction_df,
    x="Timestamp",
    y="Amount",
    labels={"Amount": "Transaction Amount"},
)
st.plotly_chart(fig)

# Display loan types
st.subheader("Loan Types Visualization")

# Prepare loan data for plotting
loan_data = user_data["loan"]
loan_df = [{"Loan Number": loan_number, "Loan Type": loan_details["loan_type"], "Loan Status": loan_details["loan_status"]} for loan_number, loan_details in loan_data.items()]
loan_df = pd.DataFrame(loan_df)

# Bar chart for loan types
fig = px.bar(loan_df, x="Loan Type", labels={"Loan Type": "Type", "count": "Number of Loans"})
st.plotly_chart(fig)
