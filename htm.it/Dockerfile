FROM htmengine:latest
RUN apt-get install -y nginx
ADD . /opt/numenta/htm.it
WORKDIR /opt/numenta/htm.it
RUN python setup.py develop --install-dir=/usr/local/lib/python2.7/site-packages --script-dir=/usr/local/bin
ENV APPLICATION_CONFIG_PATH=/opt/numenta/htm.it/conf \
    RABBITMQ_HOST=rabbit \
    RABBITMQ_USER=guest \
    RABBITMQ_PASSWD=guest \
    MYSQL_HOST=mysql \
    MYSQL_USER=root \
    MYSQL_PASSWD=htmit
RUN mkdir -p /opt/numenta/taurus/logs
EXPOSE 443 9001
CMD ./docker/taurus/run-taurus.sh
