
from openpyxl import load_workbook

import GetPricesWassermans
from Util import Util

pricesList = []

milkPrice = Util.getPriceFromWassermans("milk")
pricesList.append(milkPrice)

breadPrice = Util.getPriceFromWassermans("bread")
pricesList.append(breadPrice)

lifePrice = Util.getPriceFromWassermans("life")
pricesList.append(lifePrice)


Util.addListToPrices(pricesList, 2, 2)









