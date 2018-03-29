FROM python:3

COPY phantomjs /bin/

WORKDIR /app

COPY requirements.txt ./
COPY requirements-test.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-test.txt

COPY . .

CMD shovel test.run_acceptance
