from tradingview_ta import TA_Handler, Interval


class CryptoCurrency:
    def __init__(self, StockA, StockB):
        self.sA = StockA
        self.sB = StockB

    def get_close_price(self, stock):
        return TA_Handler(
            symbol=stock,
            screener="crypto",
            exchange="binance",
            interval=Interval.INTERVAL_1_DAY,
        ).get_indicators()['close']

    def get_currency(self):
        sA_close = self.get_close_price(self.sA)
        sB_close = self.get_close_price(self.sB)

        text1 = f'1 {self.sA} = {sA_close / sB_close} {self.sB}'
        text2 = f'1 {self.sB} = {sB_close / sA_close} {self.sA}'

        print(text1)
        print(text2)

nesne = CryptoCurrency('BTCUSDT',"AVAXUSDT")
nesne.get_currency()
