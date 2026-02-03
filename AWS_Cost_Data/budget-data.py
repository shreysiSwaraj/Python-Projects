import openpyxl

fileA = openpyxl.load_workbook("fileA.xlsx")
fileB = openpyxl.load_workbook("fileB.xlsx")    #downloaded one

sheet_a = fileA["Sheet1"]
sheet_b = fileB["Sheet1"]

service_list = {}

for service_row in range(2, sheet_b.max_row + 1):
    service_name = sheet_b.cell(service_row, 1).value
    cost = sheet_b.cell(service_row, 2).value
    service_list[service_name] = cost


for service_row in range(2, sheet_a.max_row + 1):
    service_name = sheet_a.cell(service_row, 1).value
    if service_name in service_list:
        sheet_a.cell(service_row, 2).value = service_list[service_name]


fileA.save("fileA.xlsx")