import sqlite3
import csv
from openpyxl import Workbook


DATABASE = "invoice.db"


def export_to_csv():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM invoices")

    records = cursor.fetchall()

    conn.close()

    with open("invoice_report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Invoice ID",
            "Invoice Number",
            "Vendor Name",
            "Customer Name",
            "Invoice Date",
            "Due Date",
            "Tax Amount",
            "Total Amount",
            "Currency",
            "Payment Status",
            "Processing Date",
            "Validation Status"
        ])

        writer.writerows(records)

    print("CSV export completed.")



def export_to_excel():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM invoices")

    records = cursor.fetchall()

    conn.close()


    workbook = Workbook()

    sheet = workbook.active
    sheet.title = "Invoices"


    headers = [
        "Invoice ID",
        "Invoice Number",
        "Vendor Name",
        "Customer Name",
        "Invoice Date",
        "Due Date",
        "Tax Amount",
        "Total Amount",
        "Currency",
        "Payment Status",
        "Processing Date",
        "Validation Status"
    ]


    sheet.append(headers)


    for record in records:
        sheet.append(record)


    workbook.save("invoice_report.xlsx")

    print("Excel export completed.")



if __name__ == "__main__":

    export_to_csv()
    export_to_excel()