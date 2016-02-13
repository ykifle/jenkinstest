FROM jenkinstest-base
MAINTAINER yohannesk <yohannesk@nestlabs.com>

RUN mkdir website
COPY . /website
WORKDIR /website

ENTRYPOINT ["gunicorn", "-b", ":5000", "app:app"]