import csv
from datetime import datetime
import typing

from budget.expense import Expense


class WellsFargoCsvParser():
    def parse(self, statement_file: str) -> typing.List[Expense]:
        expenses = []
        with open(statement_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                desc = row[4]
                cost = float(row[1])
                exp_date = datetime.strptime(row[0], '%m/%d/%Y')
                if cost < 0:
                    cost = cost * -1
                    expenses.append(Expense(desc, cost, exp_date, 'Wells Fargo'))

        return expenses
