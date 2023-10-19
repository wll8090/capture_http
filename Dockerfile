from python:3

WORKDIR /main

RUN python3 -m pip install --upgrade pip
RUN pip install flask
RUN pip install requests
RUN mkdir main

EXPOSE 5001/tcp

CMD ["python3","/main/capture.py"]