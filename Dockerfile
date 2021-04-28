FROM node:16-buster-slim as web-build

ARG APP_HOME=/app/web
WORKDIR ${APP_HOME}

COPY ./web/package.json ${APP_HOME}
COPY ./web/yarn.lock ${APP_HOME}
RUN yarn install && yarn cache clean

COPY ./web ${APP_HOME}
RUN yarn build

FROM python:3.9-slim as python-build

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.6


RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN . /venv/bin/activate && poetry install --no-dev --no-root

FROM python:3.9-slim as python-run
ARG APP_HOME=/app
WORKDIR ${APP_HOME}

RUN addgroup --system django \
    && adduser --system --ingroup django django

COPY --from=python-build /venv  /venv
COPY --chown=django:django . ${APP_HOME}
COPY --from=web-build --chown=django:django ${APP_HOME}/web ${APP_HOME}/web

RUN chown -R django:django ${APP_HOME}
RUN . /venv/bin/activate

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

USER django

CMD ["./docker-entrypoint.sh"]
