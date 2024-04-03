# Importing necessary libraries
import streamlit as st  # A library to create web apps for machine learning and data science
import streamlit.components.v1 as components  # Importing components module for Streamlit
from web3 import Web3, HTTPProvider  # Importing Web3 to interact with Ethereum blockchain and HTTPProvider to connect to a specific Ethereum node
import requests  # A library to make HTTP requests
import http.client
import json  # A library to work with JSON data

# Creating four columns in the Streamlit web app
col1, col2, col3, col4 = st.columns(4,gap="medium")

with col1:
     st.image('/app/xblocks.png') #file path is for docker deploy, and does not run locally, remove /app/ to run locally
     st.markdown('**LIVE FROM THE BLOCKCHAIN**')
     
# Column 1: Displaying information about Ethereum blockchain
with col2:
     st.subheader('Ethereum', divider='rainbow')
     conn = http.client.HTTPSConnection("pro-api.coinmarketcap.com")

     headersList = {
     "X-CMC_PRO_API_KEY": "<PLACE HOLDER FOR API KEY>" 
     }

     payload = ""

     conn.request("GET", "/v2/cryptocurrency/quotes/latest?slug=ethereum", payload, headersList)
     response = conn.getresponse()
     data = response.read()

     # Parse the JSON response
     parsed_data = json.loads(data.decode("utf-8"))

     # Extract the price of Ethereum in USD
     eth_price = parsed_data['data']['1027']['quote']['USD']['price']

     # Assuming you're using Streamlit, to display the Ethereum price
     st.write(f"**Price:** ${eth_price:.2f}")
     try:
          w3 = Web3(HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/R7icSkXsQxK11r2UPZBCI0zvC0QOeDqW'))  # Connecting to Ethereum mainnet using Alchemy
     except:
          w3 = Web3(HTTPProvider('https://spring-fluent-frog.quiknode.pro/9dd4efa7281f4bfd7f7d5ed5548207526912a0e2/'))
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
     # CMC Price data 
     conn.request("GET", "/v2/cryptocurrency/quotes/latest?slug=bnb", payload, headersList)

     # Get the response from the server
     response = conn.getresponse()
     data = response.read()

     # Decode and parse the JSON response
     parsed_data = json.loads(data.decode("utf-8"))

     # Assuming the BNB data is directly accessible via its slug or ID. The ID for BNB might not be as straightforward as '1027' for Ethereum, so we use a dynamic approach.
     bnb_data = next(iter(parsed_data['data'].values()))

     # Extract the price of BNB in USD
     bnb_price = bnb_data['quote']['USD']['price']

     # Use Streamlit to display the BNB price
     st.write(f"**Price:** ${bnb_price:.2f}")
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
     conn.request("GET", "/v2/cryptocurrency/quotes/latest?slug=polygon", payload, headersList)

     # Get the response from the server
     response = conn.getresponse()
     data = response.read()

     # Decode and parse the JSON response
     parsed_data = json.loads(data.decode("utf-8"))

     # You need to know the ID for Polygon or access it dynamically. Here's a generic way:
     # Assuming 'polygon_id' is the variable holding Polygon's ID. It could also be extracted dynamically if needed.
     polygon_data = next(iter(parsed_data['data'].values()))

     # Extract the price of Polygon in USD
     polygon_price = polygon_data['quote']['USD']['price']

     # Use Streamlit to display the Polygon price
     st.write(f"**Price:** ${polygon_price:.2f}")   
     try:
          w5 = Web3(HTTPProvider('https://polygon-pokt.nodies.app'))  # Primary provider
     except: 
          w5 = Web3(HTTPProvider('https://polygon.llamarpc.com'))  # Backup provider
     #w5 = Web3(HTTPProvider('https://polygon.llamarpc.com'))  # Connecting to Polygon
     st.write("**chain ID:**", w5.eth.chain_id, 'hexidecimal: 0x89')  # Displaying Polygon chain ID
     st.write("**block height:**", w5.eth.block_number)  # Displaying the current block number of Polygon
     st.write("**current gas:**", w5.eth.gas_price, "wei")  # Displaying the current gas price of Polygon
     


