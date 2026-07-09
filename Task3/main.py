from database import create_database

from crud import (
    add_invoice,
    show_invoices,
    search_invoice,
    update_invoice,
    delete_invoice
)

from exporter import (
    export_to_csv,
    export_to_excel
)

from reports import (
    invoice_summary,
    payment_report,
    vendor_report
)

from pdf_processor import extract_pdf_text



def main_menu():

    create_database()

    while True:

        print("\n===== Smart Invoice Processing System =====")
        print("1. Add Invoice")
        print("2. Show All Invoices")
        print("3. Search Invoice")
        print("4. Update Invoice")
        print("5. Delete Invoice")
        print("6. Export CSV")
        print("7. Export Excel")
        print("8. Generate Reports")
        print("9. Process PDF")
        print("10. Exit")


        choice = input("Enter your choice: ")


        if choice == "1":
            add_invoice()


        elif choice == "2":
            show_invoices()


        elif choice == "3":
            search_invoice()


        elif choice == "4":
            update_invoice()


        elif choice == "5":
            delete_invoice()


        elif choice == "6":
            export_to_csv()


        elif choice == "7":
            export_to_excel()


        elif choice == "8":

            invoice_summary()
            payment_report()
            vendor_report()


        elif choice == "9":

            path = input("Enter PDF path: ")
            extract_pdf_text(path)


        elif choice == "10":

            print("Exiting system...")
            break


        else:
            print("Invalid choice")



if __name__ == "__main__":
    main_menu()