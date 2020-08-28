FROM python:3.8

ADD pipeline/hello.py /

ADD pipeline/condaEnv.txt /

RUN pip install -r condaEnv.txt

EXPOSE 8000
CMD ["python", "hello.py"]