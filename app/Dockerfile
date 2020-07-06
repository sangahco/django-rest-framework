FROM alpine:3.8

COPY . /opt/djangoapp
WORKDIR /opt/djangoapp

ENV PYTHON_ENV=/opt/python \
    APP_HOME=/opt/djangoapp \
    ALLOWED_HOSTS=0.0.0.0

ENV PATH=$PATH:$PYTHON_ENV/bin:$APP_HOME

RUN set -e && \
    apk add --no-cache \
        bash \
        python3 \
        #libldap \
        openldap-dev \
        py-pip && \
    pip install --upgrade pip && \
    pip install virtualenv

RUN set -e && \
    apk add --no-cache --virtual .build-deps \
        build-base \
        python3-dev && \
    virtualenv $PYTHON_ENV --python=python3 && \
    . $PYTHON_ENV/bin/activate && \
    pip install -r requirements.txt && \
    deactivate && \
    apk del .build-deps

EXPOSE 8091

VOLUME [ "$APP_HOME/data", "$APP_HOME/static" ]

RUN chmod +x $APP_HOME/django-auto.sh
#CMD [ "pwd-manager-auto.sh" ]
ENTRYPOINT ["bash", "django-auto.sh"]