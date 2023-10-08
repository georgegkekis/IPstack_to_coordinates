FROM python:3

LABEL maintainer="George Gkekis <georgegkekis@gmail.com>"
RUN pip install requests
RUN pip install pytest
WORKDIR /home/root/ipstack
COPY ipstack_to_coords.py .
VOLUME /home/root/ipstack

