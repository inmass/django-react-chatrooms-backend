FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN mkdir /api
WORKDIR /api
COPY requirements.txt /api/
RUN pip install -r requirements.txt
COPY . /api/