import streamlit as st 
import streamlit.components.v1 as components
from web3 import Web3, HTTPProvider
from jsonrpcclient import request, parse, Ok
import logging
import requests
from datetime import datetime 
import pytz

   
col1, col2, col3, col4 = st.columns(4)

with col1:
#Eth
     
     st.write("**Ethereum**-chain ID:",w3.eth.chain_id, '0x1')

     st.write('**QUICKNODE**-',"block height:",w3.eth.blockNumber)
     w31 = Web3(HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/R7icSkXsQxK11r2UPZBCI0zvC0QOeDqW'))
     st.write('**ALCHEMY**-',"block height:",w31.eth.blockNumber)

     st.write ("current gas:",w3.eth.gas_price)

     st.write("**Beacon Chain**")

     res = requests.get('<PLACEHOLDER>')
     
     st.write("headers",res)  

     res2 = requests.get('<PLACE HOLDER>')
     
     st.write("genesis",res2) 

          
with col2:
#BSC
     w4 = Web3(HTTPProvider('https://binance.llamarpc.com'))

     st.write('**BSC** -'"chain ID:",w4.eth.chain_id,'hexidecimal: 0x38')

     st.write("block height:",w4.eth.blockNumber)

     st.write ("current gas:",w4.eth.gas_price)
     

with col3:
#Matic
     w5 = Web3(HTTPProvider('https://polygon.llamarpc.com	'))

     st.write("**Matic** -""chain ID:",w5.eth.chain_id,'hexidecimal: 0x89')

     st.write("block height:",w5.eth.blockNumber)

     st.write ("current gas:",w5.eth.gas_price)
     

with col4:
#Solana
#need to change out endpoint
     st.write("**Solana**")  
   #got the below rpc from https://docs.solana.com/cluster/rpc-endpoints
     response = requests.post("https://api.mainnet-beta.solana.com", json=request("getBlockHeight"))
     parsed = parse(response.json())
     if isinstance(parsed, Ok):
          st.write("block height:",parsed.result)

with st.expander("Eth Pending tx"):  
          st.write('The latest block number is: ', str(w3.eth.blockNumber) + '\n') 

          # retrive pending transactions hash
          pending_tx_filter = w3.eth.filter('pending')
          pending_tx = pending_tx_filter.get_new_entries()     # this is a list object

          # loop through the list of transcations and displays the tx hash
          for hash in pending_tx:
               st.write('Hash of a Pending Transaction:' , w3.toHex(hash))

   









   








