FROM python:3

ENV options ""

WORKDIR /

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY FiF.py ./
COPY main.py ./

CMD python ./main.py ${options} /mounted