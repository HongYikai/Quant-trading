# -*- coding: utf-8 -*-
""" HONG YIKAI  2017-12-17 """
import tushare as ts
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

'''
交易数据分类：
    今日：今日行情、今日分笔、实时五档
    历史：历史行情、历史分笔
    其它：大盘，大单，复权
'''
#今日行情（所有股票，实时变化，如果是节假日，即为上一交易日）
Get_today_all=ts.get_today_all()
#今日分笔（今日交易过的历史分笔，实时变化）
Get_today_ticks=ts.get_today_ticks('002776')
#实时五档（一次最好不要获取超过30个股票）
Get_realtime_quotes= ts.get_realtime_quotes('002776')

#历史行情（ktype=D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D）
Get_hist_data=ts.get_hist_data('002776',ktype='D',start='2017-12-01',end='2017-12-15')
#历史分笔
Get_tick_data= ts.get_tick_data('002776',date='2017-12-15')

#实时大盘指数行情
Get_index= ts.get_index('000001')
#大单交易数据（默认≥400手）
df = ts.get_sina_dd('002776', date='2017-12-25', vol=400)
#复权数据
Get_stock_basics=ts.get_stock_basics()


'''
投资参考数据:
    一级：业绩预告、分配预案、限售解禁
    二级：基金持股、融资融券
    其它：新股上市
'''
#业绩预告（2017年第4季度）
Forecast_data=ts.forecast_data(2017,4)
#分配预案(最近公布60条数据)
Profit_data=ts.profit_data(top=60)
#限售解禁(2017-12解禁股票)
Xsg_data=ts.xsg_data(year=2017,month=12)

#基金持股（2017年第4季度）
Fund_holdings=ts.fund_holdings(2017, 3)
#融资融券
Sh_margins=ts.sh_margins(start='2017-12-01', end='2017-12-15') #总的
Sh_margin_details=ts.sh_margin_details(start='2017-12-01', end='2017-12-15', symbol='601989')#指定股票
Sz_margins=ts.sz_margins(start='2017-12-01', end='2017-12-14') #总
Sz_margin_details=ts.sz_margin_details('2017-12-14') #个股列表

#新股上市
New_stocks=ts.new_stocks()


'''
数据储存：csv,mysql
'''
#csv
import os
filename = 'D:/VNPY/bigfile.csv'
for code in ['000875', '600848', '000981']:
    df = ts.get_hist_data(code)
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=None,columns=['open','high','low','close'])
    else:
        df.to_csv(filename,columns=['open','high','low','close'])

#mysql
df = ts.get_tick_data('002776', date='2017-12-15')
engine = create_engine('mysql+pymysql://root:hongyikai@127.0.0.1/quant?charset=utf8')
df.to_sql('tick_data',engine,if_exists='append')







