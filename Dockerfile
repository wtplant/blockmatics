FROM python:3.10.12
WORKDIR /blockmatics
COPY . /app
RUN pip3 install -r /app/requirements.txt
EXPOSE 8501
EXPOSE 80
CMD ["streamlit", "run",  "/app/nodestream.py"]
