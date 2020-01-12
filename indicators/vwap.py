# '''
#  Desc: Market volume weighted average price (VWAP) implementation using tulip
#
#  Copyright: (c) 2017-2020 Joshith Rayaroth Koderi
#  This file is part of Wolfinch.
# 
#  Wolfinch is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  Wolfinch is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with Wolfinch.  If not, see <https://www.gnu.org/licenses/>.
# '''

# from decimal import Decimal
from .indicator import Indicator

class VWAP (Indicator):
    '''
    volume weighted average price   (VWAP) market indicator implementation
    '''
    
    def __init__(self, name, period=12):
        self.name = name
        self.period = period
        
        #states
        self.cur_pv = 0
        self.cur_v = 0
                
    def calculate(self, candles):        
        candles_len = len(candles)
        if candles_len < self.period:
            old_pv = old_v = 0
        else:
            ohlc = candles[-self.period]['ohlc']
            old_pv = ohlc.volume*((ohlc.close + ohlc.high + ohlc.low)/3.0)
            old_v = ohlc.volume
        
        ohlc = candles[-1]['ohlc']
        v = ohlc.volume
        pv = v * ((ohlc.close + ohlc.high + ohlc.low)/3.0)
        
        self.cur_pv = self.cur_pv - old_pv + pv
        self.cur_v = self.cur_v - old_v + v
        #calculate vwap
        
#         log.info ("VWAP: %g"%cur_vwap)
        return float(self.cur_pv / self.cur_v)
        
