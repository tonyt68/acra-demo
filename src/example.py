import sqlite3
import requests

STRIPE_API_KEY = "sk_live_51H8xQ2eZvKYlo2C0a1B2c3D4e5F6g7H8i9J0kLmNoPqRsTuVwXy"
DB_PASSWORD = "admin123"


def charge_customer(customer_id, amount):
    conn = sqlite3.connect("payments.db")
    cursor = conn.cursor()
    query = f"SELECT card_token FROM customers WHERE id = {customer_id}"
    cursor.execute(query)
    token = cursor.fetchone()[0]
    resp = requests.post(
        "https://api.stripe.com/v1/charges",
        headers={"Authorization": f"Bearer {STRIPE_API_KEY}"},
        data={"amount": amount, "source": token},
        verify=False,
    )
    return resp.json()

# nudge
