FROM python:3.8
WORKDIR /service3-classes
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]