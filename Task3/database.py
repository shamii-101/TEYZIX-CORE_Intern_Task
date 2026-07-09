import sqlite3


def create_database():
    conn = sqlite3.connect("invoice.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invoices(
        invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
        invoice_number TEXT UNIQUE,
        vendor_name TEXT,
        customer_name TEXT,
        invoice_date TEXT,
        due_date TEXT,
        tax_amount REAL,
        total_amount REAL,
        currency TEXT,
        payment_status TEXT,
        processing_date TEXT,
        validation_status TEXT
    )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")