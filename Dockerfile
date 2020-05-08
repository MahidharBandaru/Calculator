FROM python:3.5 
MAINTAINER Mahidhar 
WORKDIR /calculator
ADD . /calculator
EXPOSE 5000
CMD ["python","calc.py"]

