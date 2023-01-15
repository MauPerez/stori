from datetime import datetime


class Transactions:
    def __init__(self, rows=[]) -> None:
        self.rows = rows
        self.total_balance = 0
        self.debit_amout = 0
        self.debit_amount_count = 0
        self.credit_amount = 0
        self.credit_amount_count = 0
        self.avg_credit = 0
        self.avg_debit = 0
        self.months = {}

    def get_monthly_transactions(self):
        if not self.rows:
            return
        for idx, row in enumerate(self.rows):
            date_time_obj = datetime.strptime(row.get("Date"), "%m/%d")
            month = str(date_time_obj.strftime("%B"))
            if month in self.months:
                self.months[month] += self.months.get(month, 1)
            else:
                self.months[month] = 1

    def get_total_balance(self):
        if not self.rows:
            return
        for idx, row in enumerate(self.rows):
            self.total_balance += float(row.get("Transaction", 0))

    def get_debit_balance(self):
        if not self.rows:
            return
        for idx, row in enumerate(self.rows):
            number = row.get("Transaction", 0)
            if number[0] == "-":
                self.debit_amout -= float(number[1:])
                self.debit_amount_count += 1

    def get_avg_debit_balance(self):
        self.get_debit_balance()
        if self.debit_amount_count == 0:
            return
        self.avg_debit = self.debit_amout / self.debit_amount_count

    def get_credit_balance(self):
        if not self.rows:
            return
        for idx, row in enumerate(self.rows):
            number = row.get("Transaction", 0)
            if number[0] == "+":
                self.credit_amount += float(number[1:])
                self.credit_amount_count += 1

    def get_avg_credit_balance(self):
        self.get_credit_balance()
        if self.credit_amount_count == 0:
            return
        self.avg_credit = self.credit_amount / self.credit_amount_count
