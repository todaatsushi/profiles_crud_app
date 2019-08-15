FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /profiles
WORKDIR /profiles
COPY requirements.txt /profiles/
RUN pip install -r requirements.txt
COPY . /profiles/
