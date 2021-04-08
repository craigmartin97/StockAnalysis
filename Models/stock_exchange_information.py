class StockExchangeInformation:
    _ticker = ""
    _exchange = ""

    def __init__(self, ticker, exchange):
        self._ticker = ticker
        self._exchange = exchange

    def get_ticker_symbol(self):
        return self._ticker

    def get_stock_exchange(self):
        return self._exchange
