#! /usr/bin/env python
#
# OldMonk Auto trading Bot
# Desc: Global Market Strategy Configuration. 
# ref. implementation.
# All the globally available market strategies are instantiated and configured here.
# If a market specific strategy list is required, a similar config may be made specific to the market
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from trend_rsi import TREND_RSI

init_done = False
market_strategies = []
def Configure ():
    global init_done, market_strategies
    if init_done:
        return market_strategies
    #### Configure the Strategies below ######
    trend_rsi = TREND_RSI ('trend_rsi')
    market_strategies = [
        trend_rsi
        ]
    
    #### Configure the Strategies - end ######
    init_done = True
    return market_strategies

######### ******** MAIN ****** #########
if __name__ == '__main__':
    print ("Market Strategy Test")
    Configure()
    
#EOF