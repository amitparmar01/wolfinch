'''
 Wolfinch Auto trading Bot
 Desc: NOOP Exchanges 
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
'''

from exchanges import Exchange

class Exchange(Exchange):
    def __init__ (self):
        ''' 
        Init for the exchange class
        '''
        self.name = "NOOP"
    
    def __str__ (self):
        return "{Message: noop exchange}"

    def market_init (self):
        pass
    def close (self):
        pass    
    
    def add_candle(self, market):
        pass
    
    def buy (self):
        pass
    def sell (self):
        pass
    def get_order (self):
        pass
    def cancel_order (self):
        pass
    def get_products (self):
        pass
    def get_accounts (self):
        pass     
    def get_historic_rates (self):
        pass        
    def get_product_order_book (self):
        pass
    
#EOF    
