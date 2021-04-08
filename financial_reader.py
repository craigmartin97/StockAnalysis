import stock_web_scraper
import excel_data_reader
import excel_data_writer
from Models.stock_information import StockInformation


def read_finances():
    """
    Read all financial information for the s and p 500 stocks from
    the aj bell website
    """
    # Get all stock ticker symbols for the s & p 500
    path = 'E:\\Finances\\Portfolio.xlsx'
    sheet = 'S&P 500 Stock Analysis'
    stock_exchange_info = excel_data_reader.read_sp500_stock_exchange_information(path, sheet, 3, 4, 7)

    # Get all stock financial information
    results = []
    for stock in stock_exchange_info:
        ticker = stock.get_ticker_symbol()
        exchange = stock.get_stock_exchange()
        print(f'Getting stock info for: {ticker}')
        result = stock_web_scraper.get_stock_financial_information(exchange, ticker)
        stock_information = StockInformation(ticker, exchange, result)
        results.append(stock_information)

    print('Completed collecting stock information...')
    print('Preparing to write to excel sheet...')
    excel_data_writer.write_sp500_stock_information('E:\\Finances\\PortfolioFinancialInformation.xlsx',
                                                    'Financials', results)


