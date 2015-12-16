FROM htmengine:latest
ENV HTM_IT_HOME=/opt/numenta/numenta-apps/htm-it/
RUN apt-get update
RUN apt-get install -y nginx mysql-server rabbitmq-server language-pack-en

ADD . ${HTM_IT_HOME}
WORKDIR ${HTM_IT_HOME}

RUN cp docker/rabbitmqadmin /usr/local/bin

RUN python setup.py develop --install-dir=/usr/local/lib/python2.7/site-packages --script-dir=/usr/local/bin

ENV HTM_IT_LOG_DIR=${HTM_IT_HOME}/logs
RUN mkdir -p ${HTM_IT_LOG_DIR}

ENV RABBITMQ_HOST=rabbit \
    RABBITMQ_USER=guest \
    RABBITMQ_PASSWD=guest \
    MYSQL_HOST=mysql \
    MYSQL_USER=root
#    MYSQL_PASSWD=htmit

ENV APPLICATION_CONFIG_PATH=${HTM_IT_HOME}/conf

EXPOSE 443 9001

CMD docker/start-htm-it