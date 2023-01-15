from email_handler import Email
from file_handler import FileHandler
from transactions import Transactions

if __name__ == "__main__":
    file_handler = FileHandler()
    file_handler.read("txns.csv")
    print(file_handler.rows)
    transactions = Transactions(file_handler.rows)
    transactions.get_total_balance()
    transactions.get_avg_credit_balance()
    transactions.get_avg_credit_balance()
    transactions.get_avg_debit_balance()
    transactions.get_monthly_transactions()
    print(transactions.total_balance)
    print(transactions.avg_credit)
    print(transactions.avg_debit)
    print(transactions.months)
    email = Email(
        transactions.total_balance,
        transactions.avg_credit,
        transactions.avg_debit,
        transactions.months,
    )
    email.create_email_file("result.csv", file_handler)
    email.send_email("result.csv")
