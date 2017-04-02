#-*-coding:utf-8-*-
import tushare as ts

def main():
    print ts.get_hist_data('600848')
    print ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')
    print ts.get_h_data('002337')  # 前复权
    print ts.get_h_data('002337', autype='hfq')  # 后复权
    print ts.get_h_data('002337', autype=None)  # 不复权
    print ts.get_h_data('002337', start='2015-01-01', end='2015-03-16')  # 两个日期之间的前复权数据


if __name__ == '__main__':
    main()