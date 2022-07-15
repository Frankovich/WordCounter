FROM python:3.9

ADD wordCounter.py .

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

CMD python3 ./wordCounter.py