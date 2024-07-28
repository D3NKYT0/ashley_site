FROM python:3.10.7

RUN apt-get update; \
    apt-get upgrade -y; \
    pip install --upgrade pip; \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    apt-get clean -y && rm -rf /var/lib/apt/lists/*;

WORKDIR /site/

COPY ./requirements.txt /site/

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80/tcp

ENTRYPOINT [ "python", "main.py" ]
