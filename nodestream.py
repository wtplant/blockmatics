# Importing necessary libraries
import streamlit as st  # A library to create web apps for machine learning and data science
import streamlit.components.v1 as components  # Importing components module for Streamlit
from web3 import Web3, HTTPProvider  # Importing Web3 to interact with Ethereum blockchain and HTTPProvider to connect to a specific Ethereum node
import requests  # A library to make HTTP requests


# Creating four columns in the Streamlit web app
col1, col2, col3, col4 = st.columns(4)

# Column 1: Displaying information about Ethereum blockchain
with col1:
     # Ethereum
     #st.write("**Ethereum**-chain ID:", w3.eth.chain_id, '0x1')  # Displaying Ethereum chain ID (assumes that 'w3' is previously defined)

     w3 = Web3(HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/R7icSkXsQxK11r2UPZBCI0zvC0QOeDqW'))  # Connecting to Ethereum mainnet using Alchemy
     st.write('**ALCHEMY**-',"block height:", w3.eth.blockNumber)  # Displaying the current block number of Ethereum blockchain

     st.write("current gas:", w3.eth.gas_price)  # Displaying the current gas price (assumes that 'w3' is previously defined)

     st.write("**Beacon Chain**")  # Displaying title for Beacon Chain

     res = requests.get('<https://eth-mainnet.g.alchemy.com/v2/R7icSkXsQxK11r2UPZBCI0zvC0QOeDqW>')  # Making a GET HTTP request to a specified URL
     st.write("headers", res)  # Displaying the HTTP response

     res2 = requests.get('https://eth-mainnet.g.alchemy.com/v2/R7icSkXsQxK11r2UPZBCI0zvC0QOeDqW')  # Making another GET HTTP request to a specified URL
     st.write("genesis", res2)  # Displaying the HTTP response

# Column 2: Displaying information about Binance Smart Chain
with col2:
     # Binance Smart Chain (BSC)
     w4 = Web3(HTTPProvider('https://binance.llamarpc.com'))  # Connecting to Binance Smart Chain
     st.write('**BSC** - "chain ID:', w4.eth.chain_id, 'hexidecimal: 0x38')  # Displaying BSC chain ID
     st.write("block height:", w4.eth.blockNumber)  # Displaying the current block number of BSC
     st.write("current gas:", w4.eth.gas_price)  # Displaying the current gas price of BSC

# Column 3: Displaying information about Polygon (Matic)
with col3:
     # Polygon (Matic)
     w5 = Web3(HTTPProvider('https://polygon.llamarpc.com'))  # Connecting to Polygon
     st.write("**Matic** - " "chain ID:", w5.eth.chain_id, 'hexidecimal: 0x89')  # Displaying Polygon chain ID
     st.write("block height:", w5.eth.blockNumber)  # Displaying the current block number of Polygon
     st.write("current gas:", w5.eth.gas_price)  # Displaying the current gas price of Polygon

# Column 4: Displaying information about Solana
with col4:
     # Solana
     st.write("**Solana**")  # Displaying title for Solana

     # Making a POST HTTP request to Solana RPC endpoint
     response = requests.post("https://api.mainnet-beta.solana.com", json=request("getBlockHeight"))  # Missing 'request' function, you might need to define or import it
     parsed = parse(response.json())  # Parsing the JSON response
     if isinstance(parsed, Ok):  # Checking if the parsed result is an instance of 'Ok'
          st.write("block height:", parsed.result)  # Displaying the block height

# Creating an expander for Ethereum pending transactions
with st.expander("Eth Pending tx"):  
          st.write('The latest block number is: ', str(w3.eth.blockNumber) + '\n')  # Displaying the latest block number

          # Retrieving pending transactions hash
          pending_tx_filter = w3.eth.filter('pending')
          pending_tx = pending_tx_filter.get_new_entries()  # Getting new entries from the filter

          # Looping through the list of transactions and displaying the transaction hash
          for hash in pending_tx:
               st.write('Hash of a Pending Transaction:', w3.toHex(hash))  # Converting the hash to hexadecimal and displaying it


   









   








