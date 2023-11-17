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

**Edit inbound port rules on AWS:** Navigate to the instance>click on the `security` tab>click the security group>click on edit inbound rules. 

*Once completed run the following code to keep app running **see [video](https://www.youtube.com/watch?v=DflWqmppOAg&t=709s)***

The cmd to keep app running is:
`nohup python3 -m streamlit run nodestream.py`

Stop it from running by sending the kill cmd for its process ID:
`kill <PID>`
You can check the process ID of the streamlit process ID with one of the following commands:
`ps -ef | grep streamlit` 
`ps aux | grep streamlit`

You can use the following public facing link for williamplant.net `http://ec2-34-238-255-221.compute-1.amazonaws.com:8501/`
**Note:** *there is no ssl, i.e. https and the port number for streamlit has been appended to the end of the link.*

Switching to a less expensive EC2 @ `http://ec2-54-87-177-25.compute-1.amazonaws.com:8501/`

**TO DO**
- [x] Set up EC2 free tier instance and test app
- [ ] Move to a free EC2 instance
- [ ] Add gas value
- [ ] Add pending tx for BNB and Matic Network
- [ ] Dockerize deploy



