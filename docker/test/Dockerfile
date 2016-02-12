FROM jenkinstest-base
MAINTAINER yohannesk <yohannesk@nestlabs.com>

RUN pip install 'nose==1.3.0'

RUN mkdir /output

WORKDIR /build
ENTRYPOINT ["nosetests", "-s", "-v", "--with-xunit", "--xunit-file=/output/nosetests.xml"]