# blockmatics
This is a streamlit app hosted on an EC2 instance and **now deployed via Docker Container**. App utilizes the JSON RPC API to capture live blockchian data. 
This includes new blocks produced on the top chains by TVL. 

 
~~*The next iteration will be deploying this app via Docker*~~

**streamlit docs:**
https://docs.streamlit.io/
to run the code temporarily on the server run:
`python3 -m streamlit run nodestream.py`

**JSON RPC docs**
https://web3py.readthedocs.io/en/stable/web3.eth.html |
https://docs.alchemy.com/reference/chain-apis-overview

*Set up an EC2 instance(chainstream) with port mapping to: **8501***

**Edit inbound port rules on AWS:** Navigate to the instance>click on the `security` tab>click the security group>click on edit inbound rules. 

*Once completed run the following code to keep app running *(*see [video](https://www.youtube.com/watch?v=DflWqmppOAg&t=709s)*)**

The cmd to keep app running is:
`nohup python3 -m streamlit run nodestream.py`

Stop it from running by sending the kill cmd for its process ID:
`kill <PID>`
You can check the process ID of the streamlit process ID with one of the following commands:
`ps -ef | grep streamlit` 
`ps aux | grep streamlit`

You can use the following public facing link for williamplant.net `http://ec2-54-87-177-25.compute-1.amazonaws.com:8501/`
**Note:** *there is no ssl, i.e. https and the port number for streamlit has been appended to the end of the link.*

**Docker Repo** https://hub.docker.com/repository/docker/wtplant/blocktime/general
*Note: use the same EC2 instance, just need to kill the current streamlit process from running, see above*

Docker commands to build and run container:
`docker build -t <Build-Name> .` once the build it successful run `docker run -p 8501:8501 <Build-Name>`

To push to Docker hub the cammand is `docker push wtplant/<repo-name:build-name>`


**TO DO**
- [x] Move to lightsail and Dockerize deploy. EC2 instances seem to have a cost associated with each, even the free tier.
- [ ] Additionaly they have an option for deployment on K8s https://docs.streamlit.io/knowledge-base/tutorials/deploy/kubernetes
- [x] Set up EC2 free tier instance and test app
- [x] Move to a free EC2 instance
- [x] Add gas value
- [ ] Add pending tx for BNB and Matic Network




