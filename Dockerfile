FROM python:3.8.0
LABEL maintainer="kenolusola@gmail.com"

# install environment dependencies
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        netcat \
    && apt-get -q clean

ENV INSTALL_PATH /dicegame

# set working directory
RUN mkdir -p ${INSTALL_PATH}
WORKDIR ${INSTALL_PATH}

# add requirements
COPY requirements.txt requirements.txt
# install requirements
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -c "python:config.gunicorn" "dicegame.app:create_app()"
