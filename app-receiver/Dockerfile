####################################################
## Multistage dockerfile to run the server (app-receiver)
####################################################
ARG APP_DIR="/usr/src/app-receiver/"

FROM python:3.7 as development_image

ARG APP_DIR

COPY ./receiver/ ${APP_DIR}/receiver
COPY ./tests/ ${APP_DIR}/tests/
COPY setup.py ${APP_DIR}/setup.py

COPY Pipfile ./
COPY Pipfile.lock ./

RUN mkdir -p /usr/src/app-receiver/output
RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy --ignore-pipfile --dev
RUN python -m pytest ${APP_DIR}



FROM python:3.7 as production_image

EXPOSE 8080

ARG APP_DIR
ENV DECRYPTION_KEY="/run/secrets/decryption_key"
ENV SERVER_IP="0.0.0.0"
ENV SERVER_PORT="8080"
ENV OUTPUT_DIR="/usr/src/app-receiver/output"

COPY --from=development_image ${APP_DIR} ${APP_DIR}
COPY --from=development_image Pipfile ./
COPY --from=development_image Pipfile.lock ./

RUN mkdir -p /usr/src/app-receiver/output
RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy --ignore-pipfile

WORKDIR ${APP_DIR}/receiver

ENTRYPOINT ["gunicorn", "server:app"]