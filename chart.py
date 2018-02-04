## Prilepin's Chart

# Import our packages
from collections import OrderedDict
import webbrowser
import xlwt
import os
import sys

# Get our one rep max
try:
	one_rep_max = int(input("What is your 1RM for this movement? "))
except NameError:
	print "You have to enter a number..."
	sys.exit(0)

if one_rep_max < 0:
	print "You're not THAT weak..."
	sys.exit(0)

# Request desired chart format
chart_format = str(raw_input("Do you prefer html or excel? (html/excel) "))

if chart_format != "html" and chart_format != "excel":
	print "You have to enter 'html' or 'excel'..."

# Configure Prilepin's chart
percentages = ["55-65", "70-80", "80-90", "90+"]
chart = OrderedDict([
	(percentages[0], ["3-6", "24", "18-30"]),
	(percentages[1], ["3-6", "18", "12-24"]),
	(percentages[2], ["2-4", "15", "10-20"]),
	(percentages[3], ["1-2", "4", "10"])
])

# Set up percentages for calculating working weights
converted_percentages = []
for percentage in percentages:
	if len(percentage) == 5:
		converted_percentages.append(int(percentage[:2]))
		converted_percentages.append(int(percentage[-2:]))
	else:
		pass

# Find our working weights
working_weights = []
for percentage in converted_percentages:
	percentage_for_calculation = float(percentage) / 100
	working_weight = one_rep_max * percentage_for_calculation
	working_weights.append(str(int(working_weight)))

working_weights.append(working_weights[-1] + "+")

# Prepare working weights for the chart format
i = 0
while i < 3:
	working_weights[i] = working_weights[i] + "-" + working_weights[i + 1]
	working_weights.pop(i + 1)
	i = i + 1

# Create the html table to represent Prilepin's chart with our working weights
def create_html_table():
	table = ['<html><head><title>Prilepin\'s Chart</title></head><body><table border="1">']
	table.append(
		'<tr><td>Weight</td><td>Reps Per Set</td><td>Optimal Range</td><td>Total Range</td></tr>'
	)
	x = 0
	for row in chart:
		chart[row].insert(0, working_weights[x])
		x = x + 1
		table.append(
			r'<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>'.format(*chart[row])
		)
	table.append('</table></body></html>')

	# Create the html file
	html = open("chart.html", "w")
	html.write(''.join(table))

	# Open the html file
	webbrowser.open_new_tab("chart.html")

if chart_format == "html":
	create_html_table()

# Create the spreadsheet to represent Prilepin's chart with our working weights
def create_excel_spreadsheet():
	workbook = xlwt.Workbook()
	sheet = workbook.add_sheet("Prilepin's Chart")
	sheet.write(0, 0, "Weight")
	sheet.write(0, 1, "Reps Per Set")
	sheet.write(0, 2, "Optimal Range")
	sheet.write(0, 3, "Total Range")
	x = 0
	row_xl = 1
	for row in chart:
		chart[row].insert(0, working_weights[x])
		x = x + 1
		sheet.write(row_xl, 0, chart[row][0])	# Weight
		sheet.write(row_xl, 1, chart[row][1])	# Reps Per Set
		sheet.write(row_xl, 2, chart[row][2])	# Optimal Range
		sheet.write(row_xl, 3, chart[row][3])	# Total Range
		row_xl = row_xl + 1
	workbook.save("chart.xlsx")

	# Let user know that the spreadsheet was generated
	location = os.getcwd() + "/chart.xlsx"
	print "Your spreadsheet is saved at %s" % location

if chart_format == "excel":
	create_excel_spreadsheet()