import sqlite3
import requests

# A02 - hardcoded credentials committed to source
STRIPE_API_KEY = "sk-live-DEMO-51H8xQ2eZv-KYlo2C0a1B2c3D4e5-NOT-REAL"
DB_PASSWORD = "admin123"


def charge_customer(customer_id, amount):
    # A03 - SQL injection: user input interpolated into the query
    conn = sqlite3.connect("payments.db")
    cursor = conn.cursor()
    query = f"SELECT card_token FROM customers WHERE id = {customer_id}"
    cursor.execute(query)
    token = cursor.fetchone()[0]
    # A02 - secret in header + TLS verification disabled
    resp = requests.post(
        "https://api.stripe.com/v1/charges",
        headers={"Authorization": f"Bearer {STRIPE_API_KEY}"},
        data={"amount": amount, "source": token},
        verify=False,
    )
    return resp.json()
