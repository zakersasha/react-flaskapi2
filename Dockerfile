FROM python:3.8
ADD . /react-flaskapi
WORKDIR /react-flaskapi
RUN pip install -r requirements.txt
CMD python app.py