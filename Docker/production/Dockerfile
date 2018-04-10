FROM python:3.6.5-slim-stretch

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV pcloud_uname your_pcloud_email
ENV pcloud_password your_pcloud_password

CMD gunicorn -b 0.0.0.0:5000 main:app --log-file=-
