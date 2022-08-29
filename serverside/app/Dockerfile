FROM python:3.10.6

COPY ./app /var/www/app

WORKDIR /var/www/app

ENV PIPENV_VENV_IN_PROJECT=0\
    LC_ALL=C.UTF-8\
    LANG=C.UTF-8\
    FLASK_APP=app\
    PORT=${PORT}\
    DEBUG=${DEBUG}\
    SERVICE_ACCOUNT_FILE=${SERVICE_ACCOUNT_FILE}\
    SHEET_URL=${SHEET_URL}\
    WORKSHEET_NAME=${WORKSHEET_NAME}


RUN pip install -U pip \
    pip install pipenv \
    pipenv update
RUN pipenv install --ignore-pipfile --skip-lock --system --deploy

CMD ["uwsgi","--ini","/var/www/app/uwsgi.ini"]
