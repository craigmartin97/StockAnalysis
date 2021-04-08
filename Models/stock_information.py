class StockInformation:
    _data = []
    _ticker = None
    _stock_exchange = None

    def __init__(self, ticker, stock_exchange, data):
        self._ticker = ticker
        self._stock_exchange = stock_exchange
        self._data = data

    def get_data(self):
        return self._data

    def get_ticker(self):
        return self._ticker

    def get_stock_exchange(self):
        return self._stock_exchange


