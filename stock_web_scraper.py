import requests
from bs4 import BeautifulSoup
from Models.financial import Financial
from FinancialStrategy import  FinancialStrategyFactory


def _get_next_financial_information(financial_section, financial_list):
    statement = financial_section.find_next_sibling("tr")
    if statement is None: # Nothing in statement then stop
        return financial_list

    # Get financial information from html content
    name = statement.contents[0].getText()
    yearOne = statement.contents[1].getText()
    yearTwo = statement.contents[2].getText()
    yearThree = statement.contents[3].getText()
    # Create financial object, storing information

    fs = FinancialStrategyFactory.create_strategy(name)
    yearOneNum = fs.format_financial_record(yearOne)
    yearTwoNum = fs.format_financial_record(yearTwo)
    yearThreeNum = fs.format_financial_record(yearThree)
    financial = Financial(name, yearOneNum, yearTwoNum, yearThreeNum)
    financial_list.append(financial)
    _get_next_financial_information(statement, financial_list)


def get_stock_financial_information(stock_exchange, ticker):
    stock_exchange_ticker = None
    if stock_exchange == 'New York Stock Exchange':
        stock_exchange_ticker = 'NYSE'
    elif stock_exchange == 'Nasdaq Stock Market':
        stock_exchange_ticker = 'NASDAQ'

    url = f'https://www.youinvest.co.uk/market-research/{stock_exchange_ticker}%3A{ticker}'
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    soup = BeautifulSoup(page.content, 'html.parser')
    res = soup.find_all("tr", {"class": "subHeader"})

    data = []
    for financialStatement in res:
        _get_next_financial_information(financialStatement, data)
    return data

