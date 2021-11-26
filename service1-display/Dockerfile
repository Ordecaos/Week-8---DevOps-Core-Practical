FROM python:3.8
COPY . .
RUN pip3 install flask
RUN pip3 install requests
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]