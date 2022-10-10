import argparse
import configparser
import os

import budget.report
import budget.parse as ps
from budget.expense import Report


def main():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'config.ini')
    config = configparser.ConfigParser()
    config.read(config_path)

    parser = argparse.ArgumentParser(description=config.get('cli',
                                                            'description'))
    parser.add_argument('statements', type=str, help="""Wells Fargo \
                        statement to perform \
                        anaylsis on.""", nargs='+')
    args = parser.parse_args()
    statement_paths = args.statements
    parser = ps.WellsFargoCsvParser()
    expenses = []
    for statement_path in statement_paths:
        expenses += parser.parse(statement_path)

    report = Report()
    for exp in expenses:
        report.add_expense(exp)

    budget.report.report_to_excel(report, 'report')


if __name__ == '__main__':
    main()
