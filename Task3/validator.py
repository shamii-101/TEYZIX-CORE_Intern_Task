import sqlite3


DATABASE = "invoice.db"


def check_duplicate_invoice(invoice_number):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT invoice_number FROM invoices
    WHERE invoice_number = ?
    """, (invoice_number,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return True
    return False



def validate_amount(amount):
    if amount < 0:
        return False
    return True



def validate_required_fields(fields):
    for field in fields:
        if field == "":
            return False
    return True