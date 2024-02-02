
from openpyxl import load_workbook

import GetPricesWassermans
from Util import Util

milkPrice = Util.getPriceFromWassermans("milk")

breadPrice = Util.getPriceFromWassermans("bread")

lifePrice = Util.getPriceFromWassermans("life")



# Load the existing workbook
workbook = load_workbook('priceCheckerWorkBook.xlsx')

# Select the active sheet
worksheet = workbook.active

# Update cell values
worksheet['A2'] = "milk"
worksheet['B2'] = milkPrice

worksheet['A3'] = "bread"
worksheet['B3'] = breadPrice

worksheet['A4'] = "life"
worksheet['B4'] = lifePrice

# Save the workbook
workbook.save('priceCheckerWorkBook.xlsx')

print("data saved")





