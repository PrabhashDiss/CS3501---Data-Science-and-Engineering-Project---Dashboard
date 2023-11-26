import streamlit as st
import pandas as pd
import plotly.express as px

# Assuming your data is stored in a dictionary named 'data'
data = {
  "user234": {
    "account": {
      "1082310654": {
        "balance": 2304394,
        "last_active_date": "2022-02-01",
        "open_date": "2005-06-16",
        "transaction": {
          "3332": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "550000",
            "transaction_description": "paying car rent",
            "transaction_timestamp": "2022-02-24 17:53:43"
          },
          "3333": {
            "account_number_from": 3051271963,
            "account_number_to": 1082310654,
            "amount": "125000",
            "transaction_description": "grocery shopping",
            "transaction_timestamp": "2022-03-15 09:30:15"
          },
          "3334": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "75000",
            "transaction_description": "electricity bill",
            "transaction_timestamp": "2022-04-02 14:45:22"
          },
          "3335": {
            "account_number_from": 1082310654,
            "account_number_to": 3051271963,
            "amount": "200000",
            "transaction_description": "home rent",
            "transaction_timestamp": "2022-04-10 18:20:30"
          },
          "3336": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "300000",
            "transaction_description": "medical expenses",
            "transaction_timestamp": "2022-05-05 11:10:12"
          },
          "3337": {
            "account_number_from": 3051271963,
            "account_number_to": 1082310654,
            "amount": "50000",
            "transaction_description": "dining out",
            "transaction_timestamp": "2022-05-18 20:15:45"
          },
          "3338": {
            "account_number_from": 1082310654,
            "account_number_to": 3051271963,
            "amount": "80000",
            "transaction_description": "clothing shopping",
            "transaction_timestamp": "2022-06-02 09:55:27"
          },
          "3339": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "100000",
            "transaction_description": "travel expenses",
            "transaction_timestamp": "2022-06-20 16:30:18"
          },
          "3340": {
            "account_number_from": 1082310654,
            "account_number_to": 2051271952,
            "amount": "120000",
            "transaction_description": "home improvement",
            "transaction_timestamp": "2022-07-08 13:40:55"
          },
          "3341": {
            "account_number_from": 3051271963,
            "account_number_to": 1082310654,
            "amount": "25000",
            "transaction_description": "entertainment",
            "transaction_timestamp": "2022-07-25 21:05:10"
          }
        }
      }
    },
    "customer_id": "a234",
    "customer_name": "Angelica Jefferson",
    "gender": "f",
    "loan": {
      "101": {
        "loan_status": 0,
        "loan_type": "personal loan"
      },
      "111": {
        "loan_status": 0,
        "loan_type": "home"
      },
      "289": {
        "loan_status": 0,
        "loan_type": "home"
      },
      "349": {
        "loan_status": 0,
        "loan_type": "home"
      },
      "540": {
        "loan_status": 0,
        "loan_type": "personal loan"
      },
      "834": {
        "loan_status": 0,
        "loan_type": "personal loan"
      },
      "901": {
        "loan_status": 0,
        "loan_type": "education"
      },
      "102": {
        "loan_status": 0,
        "loan_type": "car loan"
      },
      "451": {
        "loan_status": 0,
        "loan_type": "personal loan"
      },
      "632": {
        "loan_status": 0,
        "loan_type": "education"
      }
    },
    "password": "$2b$12$qVlefJ2kQHWo./fARSr8kuwjgkJT2y2yy8svNRLtTTM77Gxqlz74y"
  },
  "user235": {
    "account": {
      "2051271952": {
        "balance": 1748967,
        "last_active_date": "2022-03-05",
        "open_date": "2010-11-22",
        "transaction": {
          "3334": {
            "account_number_from": 1082310654,
            "account_number_to": 2051271952,
            "amount": "32000",
            "transaction_description": "reimbursement",
            "transaction_timestamp": "2022-03-18 14:12:29"
          },
          "3335": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "50000",
            "transaction_description": "utility bills",
            "transaction_timestamp": "2022-04-05 12:30:45"
          },
          "3336": {
            "account_number_from": 1082310654,
            "account_number_to": 2051271952,
            "amount": "75000",
            "transaction_description": "grocery shopping",
            "transaction_timestamp": "2022-04-15 17:45:22"
          },
          "3337": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "100000",
            "transaction_description": "medical expenses",
            "transaction_timestamp": "2022-05-02 09:10:30"
          },
          "3338": {
            "account_number_from": 1082310654,
            "account_number_to": 2051271952,
            "amount": "150000",
            "transaction_description": "home rent",
            "transaction_timestamp": "2022-05-20 14:20:12"
          },
          "3339": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "200000",
            "transaction_description": "travel expenses",
            "transaction_timestamp": "2022-06-10 18:55:45"
          },
          "3340": {
            "account_number_from": 1082310654,
            "account_number_to": 2051271952,
            "amount": "250000",
            "transaction_description": "car loan repayment",
            "transaction_timestamp": "2022-06-28 11:30:27"
          },
          "3341": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "300000",
            "transaction_description": "home improvement",
            "transaction_timestamp": "2022-07-15 20:15:18"
          },
          "3342": {
            "account_number_from": 1082310654,
            "account_number_to": 2051271952,
            "amount": "350000",
            "transaction_description": "personal loan repayment",
            "transaction_timestamp": "2022-08-02 16:40:55"
          },
          "3343": {
            "account_number_from": 2051271952,
            "account_number_to": 1082310654,
            "amount": "400000",
            "transaction_description": "education expenses",
            "transaction_timestamp": "2022-08-20 21:05:10"
          },
          "3344": {
            "account_number_from": 1082310654,
            "account_number_to": 2051271952,
            "amount": "450000",
            "transaction_description": "dining out",
            "transaction_timestamp": "2022-09-05 09:25:36"
          }
        }
      }
    },
    "customer_id": "b235",
    "customer_name": "John Doe",
    "gender": "m",
    "loan": {
      "202": {
        "loan_status": 0,
        "loan_type": "home loan"
      },
      "303": {
        "loan_status": 0,
        "loan_type": "car loan"
      },
      "404": {
        "loan_status": 0,
        "loan_type": "education"
      },
      "505": {
        "loan_status": 0,
        "loan_type": "personal loan"
      },
      "606": {
        "loan_status": 0,
        "loan_type": "home loan"
      },
      "707": {
        "loan_status": 0,
        "loan_type": "car loan"
      },
      "808": {
        "loan_status": 0,
        "loan_type": "education"
      },
      "909": {
        "loan_status": 0,
        "loan_type": "personal loan"
      },
      "1010": {
        "loan_status": 0,
        "loan_type": "home loan"
      },
      "1111": {
        "loan_status": 0,
        "loan_type": "car loan"
      }
    },
    "password": "$2b$12$suBvfq6iGhiekHuwQPx7f.txEDbTgttJ6bmutALC4hrtbeaXEB0l."
  }
}

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
