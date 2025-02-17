FROM python:3.10-slim



COPY . /app
RUN apt update && \
apt upgrade -y && \
DEBIAN_FRONTEND=noninteractive apt install libkrb5-dev krb5-user gcc -y &&\
apt clean all &&\
python3 -m venv /env &&\
pip3 install --upgrade pip &&\
pip3 install -r /app/requirements.txt

EXPOSE 8080
WORKDIR /app
CMD [ "gunicorn", "--config", "web_config.py", "app:app" ]