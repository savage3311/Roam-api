FROM python:3.10.8
WORKDIR /app
RUN pip install flask
RUN pip install flask-smorest
RUN pip install python-dotenv
RUN pip install sqlalchemy
RUN pip install flask-sqlalchemy
RUN pip install requests
RUN pip install datetime
RUN pip install hmac
RUN pip install gunicorn
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:create_app()"]




