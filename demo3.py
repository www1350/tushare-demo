#-*-coding:utf-8-*-
import tushare as ts

def main():
    df = ts.get_tick_data('600848',date='2014-01-09')
    print df.head(10)


if __name__ == '__main__':
    main()