from openpyxl import load_workbook

# load excel file
workbook = load_workbook(filename="csv/Email_sample.xlsx")

# open workbook
sheet = workbook.active

# modify the desired cell
sheet["A1"] = "Full Name"

# save the file
workbook.save(filename="csv/output.xlsx")