
from openpyxl import load_workbook

import GetPricesWassermans
from Util import Util

pricesList = []

urlList = ["https://wassermansupermarket.com/#!/hb/m/000000/r/11406/he/flushing/",
           "https://wassermansupermarket.com/#!/hb/m/000000/r/15346/he/flushing/",
           "https://wassermansupermarket.com/#!/hb/m/000000/r/22987/he/flushing/"]

pricesList = Util.getPriceFromWassermans(urlList)


Util.addListToPrices(pricesList, 2, 2)









