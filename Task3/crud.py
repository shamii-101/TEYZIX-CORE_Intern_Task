import sqlite3
from logger import log_info, log_error




DATABASE = "invoice.db"


def add_invoice():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    try:
        invoice_number = input("Enter invoice number: ")
        vendor_name = input("Enter vendor name: ")
        customer_name = input("Enter customer name: ")
        invoice_date = input("Enter invoice date: ")
        due_date = input("Enter due date: ")
        tax_amount = float(input("Enter tax amount: "))
        total_amount = float(input("Enter total amount: "))
        currency = input("Enter currency: ")
        payment_status = input("Enter payment status: ")
        processing_date = input("Enter processing date: ")
        validation_status = "Valid"

        cursor.execute("""
        INSERT INTO invoices(
            invoice_number,
            vendor_name,
            customer_name,
            invoice_date,
            due_date,
            tax_amount,
            total_amount,
            currency,
            payment_status,
            processing_date,
            validation_status
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            invoice_number,
            vendor_name,
            customer_name,
            invoice_date,
            due_date,
            tax_amount,
            total_amount,
            currency,
            payment_status,
            processing_date,
            validation_status
        ))

        conn.commit()
        print("Invoice added successfully.")
        print("Invoice added successfully.")
        log_info(f"Invoice {invoice_number} added successfully")

    except sqlite3.IntegrityError:
        print("Invoice number already exists.")

    except Exception as e:
     print("Error:", e)
     log_error(str(e))

    finally:
        conn.close()



def show_invoices():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM invoices")

    records = cursor.fetchall()

    if records:
        for record in records:
            print(record)
    else:
        print("No invoices found.")

    conn.close()



def search_invoice():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    invoice_number = input("Enter invoice number to search: ")

    cursor.execute("""
    SELECT * FROM invoices
    WHERE invoice_number = ?
    """, (invoice_number,))

    record = cursor.fetchone()

    if record:
        print("Invoice Found:")
        print(record)
    else:
        print("Invoice not found.")

    conn.close()



def update_invoice():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    invoice_number = input("Enter invoice number: ")
    payment_status = input("Enter new payment status: ")

    cursor.execute("""
    UPDATE invoices
    SET payment_status = ?
    WHERE invoice_number = ?
    """,
    (payment_status, invoice_number))

    conn.commit()

    if cursor.rowcount:
        print("Invoice updated successfully.")
    else:
        print("Invoice not found.")

    conn.close()



def delete_invoice():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    invoice_number = input("Enter invoice number to delete: ")

    cursor.execute("""
    DELETE FROM invoices
    WHERE invoice_number = ?
    """,
    (invoice_number,))

    conn.commit()

    if cursor.rowcount:
        print("Invoice deleted successfully.")
    else:
        print("Invoice not found.")

    conn.close()