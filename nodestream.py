# Importing necessary libraries
import streamlit as st  # A library to create web apps for machine learning and data science
import streamlit.components.v1 as components  # Importing components module for Streamlit
from web3 import Web3, HTTPProvider  # Importing Web3 to interact with Ethereum blockchain and HTTPProvider to connect to a specific Ethereum node
import requests  # A library to make HTTP requests

# Creating four columns in the Streamlit web app
col1, col2, col3, col4 = st.columns(4,gap="medium")

with col1:
     st.image('/app/xblocks.png')
     st.markdown('**LIVE FROM THE BLOCKCHAIN**')
     
# Column 1: Displaying information about Ethereum blockchain
with col2:
     st.subheader('Ethereum', divider='rainbow')
     w3 = Web3(HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/R7icSkXsQxK11r2UPZBCI0zvC0QOeDqW'))  # Connecting to Ethereum mainnet using Alchemy
     st.write("**chain ID:**", w3.eth.chain_id, 'hexidecimal:0x1')  # Displaying Ethereum chain ID 
     st.write("**block height:**", w3.eth.block_number)  # Displaying the current block number of Ethereum blockchain

     st.write("**current gas:**", w3.eth.gas_price, "wei")  # Displaying the current gas price 

     # Create a filter to retrieve pending transactions
     pending_tx_filter = w3.eth.filter('pending')

# Retrieve the list of pending transaction hashes
     pending_tx_hashes = pending_tx_filter.get_new_entries()

# Loop through the list of transaction hashes and display them
     for tx_hash in pending_tx_hashes:
          st.write('**Pending Transaction:**', w3.to_hex(tx_hash))

     
     #st.write("**Beacon Chain**")  # Displaying title for Beacon Chain

     #res = requests.get('<https://eth-mainnet.g.alchemy.com/v2/R7icSkXsQxK11r2UPZBCI0zvC0QOeDqW>')  # Making a GET HTTP request to a specified URL
     #st.write("headers", res)  # Displaying the HTTP response

     #res2 = requests.get('https://eth-mainnet.g.alchemy.com/v2/R7icSkXsQxK11r2UPZBCI0zvC0QOeDqW')  # Making another GET HTTP request to a specified URL
     #st.write("genesis", res2)  # Displaying the HTTP response
     
     
# Column 2: Displaying information about Binance Smart Chain
with col3:
     st.subheader('BNB Chain', divider='orange')
     try:
          w4 = Web3(HTTPProvider('https://bsc-dataseed.bnbchain.org'))  # Primary provider
     except:
          w4 = Web3(HTTPProvider('https://endpoints.omniatech.io/v1/bsc/mainnet/public'))  # Backup provider

     #w4 = Web3(HTTPProvider('https://binance.llamarpc.com'))  # Connecting to Binance Smart Chain
     st.write('**chain ID:**', w4.eth.chain_id, 'hexidecimal: 0x38')  # Displaying BSC chain ID
     st.write("**block height:**", w4.eth.block_number)  # Displaying the current block number of BSC
     st.write("**current gas:**", w4.eth.gas_price, "wei")  # Displaying the current gas price of BSC
     #pending transaction
     # this method doesn't work for bsc -pending_tx_filter = w4.eth.filter('pending')

# Column 3: Displaying information about Polygon (Matic)
with col4:
     st.subheader('Polygon', divider='violet')
     try:
          w5 = Web3(HTTPProvider('https://polygon.llamarpc.com'))  # Primary provider
     except:
          w5 = Web3(HTTPProvider('https://endpoints.omniatech.io/v1/matic/mainnet/public'))  # Backup provider
     #w5 = Web3(HTTPProvider('https://polygon.llamarpc.com'))  # Connecting to Polygon
     st.write("**chain ID:**", w5.eth.chain_id, 'hexidecimal: 0x89')  # Displaying Polygon chain ID
     st.write("**block height:**", w5.eth.block_number)  # Displaying the current block number of Polygon
     st.write("**current gas:**", w5.eth.gas_price, "wei")  # Displaying the current gas price of Polygon
     #pnding tx
     
     #st.write("**Solana**")  # Displaying title for Solana

     # Making a POST HTTP request to Solana RPC endpoint
     #response = requests.post("https://api.mainnet-beta.solana.com", json=request("getBlockHeight"))  # Missing 'request' function, you might need to define or import it
     #parsed = parse(response.json())  # Parsing the JSON response
     #if isinstance(parsed, Ok):  # Checking if the parsed result is an instance of 'Ok'
          #st.write("block height:", parsed.result)  # Displaying the block height

# Creating an expander for Ethereum pending transactions
#with st.expander("Eth Pending tx"):  
          #st.write('The latest block number is: ', str(w3.eth.blockNumber) + '\n')  # Displaying the latest block number

          # Retrieving pending transactions hash
          #pending_tx_filter = w3.eth.filter('pending')
          #pending_tx = pending_tx_filter.get_new_entries()  # Getting new entries from the filter

          # Looping through the list of transactions and displaying the transaction hash
          #for hash in pending_tx:
               #st.write('Hash of a Pending Transaction:', w3.toHex(hash))  # Converting the hash to hexadecimal and displaying it


