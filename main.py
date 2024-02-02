from Util import Util

urlList = Util.saveUrlListFromExcel(2, 3)

pricesList = Util.getPriceFromWassermans(urlList)

Util.addListToPrices(pricesList, 2, 2)
