FROM python:3 as tests
WORKDIR /home
COPY testFif.py ./
CMD python testFif.py

FROM tests as main-part
ENV options ""

WORKDIR /home

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY FiF.py ./
COPY main.py ./

CMD python ./main.py ${options} /mounted
