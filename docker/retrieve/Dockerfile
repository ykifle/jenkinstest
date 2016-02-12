FROM fedora:22
MAINTAINER yohannesk <yohannesk@nestlabs.com>

RUN dnf -y update && dnf install -y \
  git \
  && dnf clean all

RUN mkdir -p /root/.ssh
RUN echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

ENTRYPOINT eval `ssh-agent -s` && ssh-add && git clone git@github.com:ykifle/jenkinstest.git build