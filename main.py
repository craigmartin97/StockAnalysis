import yfinance as yf
import  pandas as pd
import get_tickers

writer = pd.ExcelWriter("E:\\Finances\\PortfolioFinancialInformation2.xlsx", engine='openpyxl')
tickers = get_tickers.get_s_and_p_500_tickers()

goodStocks = []

for ticker in tickers:
    print(f'{ticker}')

    tickerSymbol = yf.Ticker(ticker)

    # get stock info as data frame
    balanceSheetDataFrame = pd.DataFrame(tickerSymbol.balancesheet)
    financialDataFrame = pd.DataFrame(tickerSymbol.financials)

    # Calculate total equity
    allTotalEquity = []
    for col in balanceSheetDataFrame.columns:
        column = balanceSheetDataFrame.get(col)
        totalAssets = column["Total Assets"]
        totalLiabilities = column["Total Current Liabilities"]
        totalEquity = totalAssets - totalLiabilities
        allTotalEquity.append(totalEquity)

    stockData = []
    for i in range(len(financialDataFrame.columns)):
        column = financialDataFrame.get(financialDataFrame.columns[i])

        netIncome = column["Net Income"]
        operatingIncome = column["Operating Income"]
        revenue = column["Total Revenue"]
        grossProfit = column["Gross Profit"]
        costOfRevenue = column["Cost Of Revenue"]

        grossMargin = round((grossProfit/revenue) * 100, 2)
        netMargin = round((netIncome / revenue) * 100, 2)
        operatingMargin = round((operatingIncome / revenue) * 100, 2)
        roe = round((netIncome / totalEquity) * 100, 2)

    # Store total equity in balance sheet data frame
    balanceSheetDataFrame.loc["Total Equity"] = allTotalEquity

    balanceSheetDataFrame.to_excel(writer, sheet_name=ticker, startcol=0)
    financialDataFrame.to_excel(writer, sheet_name=ticker, startcol=8)



writer.save()
writer.close()

