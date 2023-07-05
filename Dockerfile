FROM python:3.10-slim
EXPOSE 8080
ADD ./requirements.txt /
RUN apt-get update
RUN apt-get install poppler-utils -y
RUN pip install -r /requirements.txt
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ARG PORT
ENV PORT=8080
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
CMD python services.py