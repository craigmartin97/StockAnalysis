from FinancialStrategy import EPSFinancialConverterStrategy
from FinancialStrategy import MillionFinancialConverterStrategy


def create_strategy(name):
    if name == 'Basic EPS':
        return EPSFinancialConverterStrategy
    else:
        return MillionFinancialConverterStrategy

