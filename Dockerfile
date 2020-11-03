FROM python:3
ENV PATH /usr/bin:$PATH
ADD ./server.py /server.py
EXPOSE 8080
ENTRYPOINT [ "python", "server.py"]
