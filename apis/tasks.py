import pandas as pd
from basetables.models import Customer, Loan
import os
def ingest_data():
    try:
        customer_df = pd.read_excel("/app/customer_data.xlsx")
        loan_df = pd.read_excel("/app/loan_data.xlsx")
        print(f"✅ Read {len(customer_df)} customers, {len(loan_df)} loans.")

        for _, row in customer_df.iterrows():
            Customer.objects.get_or_create(
                customer_id=row['Customer ID'],
                defaults={
                    'first_name': row['First Name'],
                    'last_name': row['Last Name'],
                    'phone_number': str(row['Phone Number']),
                    'monthly_income': row['Monthly Salary'],
                    'approved_limit': row['Approved Limit'],
                    'age': row['Age'],
                }
            )

        for _, row in loan_df.iterrows():
            Loan.objects.get_or_create(
                loan_id=row['Loan ID'],
                defaults={
                    'customer_id_id': row['Customer ID'], 
                    'loan_amount': row['Loan Amount'],
                    'tenure': row['Tenure'],
                    'interest_rate': row['Interest Rate'],
                    'monthly_installment': row['Monthly payment'],
                    'emis_paid_on_time': row['EMIs paid on Time'],
                    'start_date': pd.to_datetime(row['Date of Approval']).date(),
                    'end_date': pd.to_datetime(row['End Date']).date(),
                }
            )

        print("✅ Ingestion completed successfully.")

    except Exception as e:
        print(f"❌ Ingestion failed: {e}")

from django.db import connection

def reset_sequences():
    with connection.cursor() as cursor:
        cursor.execute("SELECT setval(pg_get_serial_sequence('basetables_customer', 'customer_id'), MAX(customer_id)) FROM basetables_customer;")
        cursor.execute("SELECT setval(pg_get_serial_sequence('basetables_loan', 'loan_id'), MAX(loan_id)) FROM basetables_loan;")
