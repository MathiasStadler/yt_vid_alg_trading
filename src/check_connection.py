# FROM HERE
# https://www.interactivebrokers.com/campus/ibkr-quant-news/interactive-brokers-python-api-native-a-step-by-step-guide/

from ibapi.client import EClient
from ibapi.wrapper import EWrapper  

class IBapi(EWrapper, EClient):
     def __init__(self):
         EClient.__init__(self, self) 

app = IBapi()
app.connect('127.0.0.1', 7496, 123)
app.run()

'''
#Uncomment this section if unable to connect
#and to prevent errors on a reconnect
import time
time.sleep(2)
app.disconnect()
'''

''''
TWS NOT Running sdhow this
 python3 src/check_connection.py 
ERROR -1 502 Couldn't connect to TWS. Confirm that "Enable ActiveX and Socket EClients" 
is enabled and connection port is the same as "Socket Port" on the 
TWS "Edit->Global Configuration...->API->Settings" menu. Live Trading ports: 
TWS: 7496; IB Gateway: 4001. Simulated Trading ports for new installations 
of version 954.1 or newer:  TWS: 7497; IB Gateway: 4002

'''

'''
INTO VENV =>  source .venv/bin/activate
LIST INSTALLED PACKAGE => pip3 freeze
DEKTIVATE VENV = deactivate
START PRG => python3 src/check_connection.py
'''

