#-*-coding:utf-8-*-
import tushare as ts

def main():
    df = ts.get_realtime_quotes('000581')  # Single stock symbol
    print df[['code', 'name', 'price', 'bid', 'ask', 'volume', 'amount', 'time']]
    print ts.get_realtime_quotes(['600848', '000980', '000981'])  # symbols from a list
    print ts.get_realtime_quotes(df['code'].tail(10))  # from a Series


if __name__ == '__main__':
    main()