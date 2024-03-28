import openpyxl


def excel_reader():
    sku_data = []
    book = openpyxl.open("data.xlsx", read_only=True)
    sheet = book.active
    for row in range(1, sheet.max_row):
        sku = sheet[row][0].value
        sku_data.append(sku)

    return sku_data
