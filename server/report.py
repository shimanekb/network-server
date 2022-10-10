import xlsxwriter

from budget.expense import Report


def load_report(report_file: str) -> Report:
    return Report()


def report_to_excel(report: Report, report_name: str) -> None:
    workbook = xlsxwriter.Workbook(report_name + '.xlsx')
    _summary_sheet(workbook, report)
    _expense_sheet(workbook, report)

    workbook.close()
    return


def _summary_sheet(workbook: xlsxwriter.Workbook, report: Report) -> None:
    bold = workbook.add_format({'bold': True})
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Category', bold)
    worksheet.set_column('A:A', 30)
    worksheet.write('B1', 'Total', bold)
    worksheet.set_column('B:B', 20)
    worksheet.write('D1', 'Overall Total', bold)
    worksheet.set_column('D:D', 20)

    worksheet.write(1, 0, 'Uknown')
    worksheet.write(1, 1, report.total())
    worksheet.write(1, 3, report.total())


def _expense_sheet(workbook: xlsxwriter.Workbook, report: Report) -> None:
    bold = workbook.add_format({'bold': True})
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Date', bold)
    worksheet.set_column('A:A', 10)
    worksheet.write('B1', 'Account', bold)
    worksheet.set_column('B:B', 20)
    worksheet.write('C1', 'Category', bold)
    worksheet.set_column('C:C', 20)
    worksheet.write('D1', 'Description', bold)
    worksheet.set_column('D:D', 100)
    worksheet.write('E1', 'Cost', bold)
    worksheet.set_column('E:E', 10)
    index = 1
    for expense in report.expenses:
        worksheet.write(index, 0, expense.date.strftime('%m/%d/%Y'))
        worksheet.write(index, 1, expense.account)
        worksheet.write(index, 2, 'na')
        worksheet.write(index, 3, expense.description)
        worksheet.write(index, 4, expense.cost)
        index += 1
