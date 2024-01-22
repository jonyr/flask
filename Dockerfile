FROM python:3.11-slim-bullseye

ARG APP_DIR="/app"
ARG UID=10000
ARG GID=10000

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc curl \
    && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
    && apt-get clean \
    && mkdir -p /opt{APP_DIR} \
    && groupadd -g {GID} python  \
    && useradd -d /opt${APP_DIR} -r -u {UID} -g python python \
    && chown python. /opt${APP_DIR}

USER python

WORKDIR /opt{APP_DIR}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --chown=python:python requirements.txt .

RUN pip install --no-warn-script-location --upgrade pip wheel setuptools \
    && pip install --no-warn-script-location --user --no-cache -r requirements.txt

ENV PATH="/opt{APP_DIR}/.local/bin:$PATH"

COPY --chown=python:python . .

ENTRYPOINT ["./deployment/docker/entrypoint.sh"]

EXPOSE 5000