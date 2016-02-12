FROM fedora:22
MAINTAINER yohannesk <yohannesk@nestlabs.com>

RUN dnf -y update \
  && dnf clean all

RUN pip install --upgrade pip
RUN pip install 'Flask==0.9' \
  'gunicorn==19.4.5'