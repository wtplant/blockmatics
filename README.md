# blockmatics
This is a streamlit app deployed on an EC2 instance. App utilizes the JSON RPC API to capture live blockchian data. 
This includes new blocks produced on the top chains by TVL. 

*The next iteration will be deploying this app via Docker*

**streamlit docs:**
https://docs.streamlit.io/
to run the code temporarily on the server run:
`python3 -m streamlit run nodestream.py`

**JSON RPC docs**
https://web3py.readthedocs.io/en/stable/web3.eth.html |
https://docs.alchemy.com/reference/chain-apis-overview

*Set up an EC2 instance(chainstream) with port mapping to: **8501***

*Once completed run the following code to keep app running **see [video](https://www.youtube.com/watch?v=DflWqmppOAg&t=709s)***


