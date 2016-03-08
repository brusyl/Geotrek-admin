FROM ubuntu:14.04
ENV LANG fr_FR.utf8
RUN mkdir geotrek geotrek/etc
WORKDIR geotrek
ADD install.sh docker-install.sh docker-cmd.sh ./
ADD conf/settings.ini.sample etc/settings.ini
RUN ./docker-install.sh
VOLUME /var/lib/postgresql/9.3/main /geotrek/var/media
ENTRYPOINT ["/geotrek/docker-cmd.sh"]
