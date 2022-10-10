from datetime import date
import typing


class Expense:
    def __init__(self, description: str, cost: float, exp_date: date = None,
                 account: str = 'na'):
        self.date = exp_date
        self.description = description
        self.cost = cost
        self.account = account

    def __str__(self):
        return '%s $%s' % (self.description, self.cost)

    def __eq__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented

        equal = self.cost == other.cost
        equal = equal and self.description == other.description
        equal = equal and self.date == other.date
        equal = equal and self.account == other.account

        return equal


class Report:
    def __init__(self, expenses: typing.List[Expense] = [],
                 ignore_exp: typing.List[str] = ['WELLS FARGO CASH WISE VISA SIGNATURE',
                                                 'WF Credit Card AUTO PAY',
                                                 'BARCLAYCARD US CREDITCARD']):
        self.expenses = expenses
        self.ignore_exp = ignore_exp

    def add_expense(self, expense: Expense) -> None:
        for exp in self.expenses:
            if exp == expense:
                return

        for ignore in self.ignore_exp:
            if ignore in expense.description:
                return

        self.expenses.append(expense)

    def total(self) -> float:
        costs = [expense.cost for expense in self.expenses]
        return sum(costs)
