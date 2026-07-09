import sqlite3


DATABASE = "invoice.db"


def invoice_summary():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute("SELECT COUNT(*) FROM invoices")

    total_invoices = cursor.fetchone()[0]


    cursor.execute("SELECT SUM(total_amount) FROM invoices")

    total_amount = cursor.fetchone()[0]


    if total_amount is None:
        total_amount = 0


    print("\n===== Invoice Summary =====")
    print("Total Invoices:", total_invoices)
    print("Total Amount:", total_amount)


    conn.close()



def payment_report():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute("""
    SELECT payment_status, COUNT(*)
    FROM invoices
    GROUP BY payment_status
    """)


    records = cursor.fetchall()


    print("\n===== Payment Report =====")

    for record in records:
        print(record)


    conn.close()



def vendor_report():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()


    cursor.execute("""
    SELECT vendor_name, COUNT(*), SUM(total_amount)
    FROM invoices
    GROUP BY vendor_name
    """)


    records = cursor.fetchall()


    print("\n===== Vendor Report =====")

    for record in records:
        print(record)


    conn.close()



if __name__ == "__main__":

    invoice_summary()
    payment_report()
    vendor_report()