FROM ubuntu:14.04
ENV LANG fr_FR.utf8
RUN mkdir geotrek geotrek/etc
WORKDIR geotrek
ADD install.sh ./
ADD conf/settings.ini.sample etc/settings.ini
RUN ./install.sh --noinput; cat install.log