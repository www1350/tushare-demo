#-*-coding:utf-8-*-
import tushare as ts

def main():
    print ts.get_hist_data('600848') #一次性获取全部日k线数据
    print ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')
    print ts.get_hist_data('600848', ktype='W')  # 获取周k线数据
    print ts.get_hist_data('600848', ktype='M')  # 获取月k线数据
    print ts.get_hist_data('600848', ktype='5')  # 获取5分钟k线数据
    print ts.get_hist_data('600848', ktype='15')  # 获取15分钟k线数据
    print ts.get_hist_data('600848', ktype='30')  # 获取30分钟k线数据
    print ts.get_hist_data('600848', ktype='60')  # 获取60分钟k线数据
    print ts.get_hist_data('sh')  # 获取上证指数k线数据，其它参数与个股一致，下同
    print ts.get_hist_data('sz')  # 获取深圳成指k线数据
    print ts.get_hist_data('hs300')  # 获取沪深300指数k线数据
    print ts.get_hist_data('sz50')  # 获取上证50指数k线数据
    print ts.get_hist_data('zxb')  # 获取中小板指数k线数据
    print ts.get_hist_data('cyb')  # 获取创业板指数k线数据
    print ts.get_h_data('002337')  # 前复权
    print ts.get_h_data('002337', autype='hfq')  # 后复权
    print ts.get_h_data('002337', autype=None)  # 不复权
    print ts.get_h_data('002337', start='2015-01-01', end='2015-03-16')  # 两个日期之间的前复权数据



if __name__ == '__main__':
    main()