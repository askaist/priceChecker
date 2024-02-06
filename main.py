from Util import Util

wassermansUrlList = Util.saveUrlListFromExcel(2, 2)

wassermansPricesList = Util.getPriceFromWassermans(wassermansUrlList)

seasonsUrlList = Util.saveUrlListFromExcel(2, 3)

seasonsPricesList = Util.getPricesFromSeasons(seasonsUrlList)

Util.addListToPrices(wassermansPricesList, 2, 2)

Util.addListToPrices(seasonsPricesList, 2, 3)
