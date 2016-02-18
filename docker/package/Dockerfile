FROM gcr.io/dropcam-dev/jenkinstest-base
MAINTAINER yohannesk <yohannesk@nestlabs.com>

RUN dnf install -y docker-engine

RUN mkdir /package
COPY Packagefile /package/Dockerfile
COPY .packageignore /package/.dockerignore
WORKDIR /package

ENTRYPOINT cp -r /build/* /package && docker build -t $IMAGE_NAME .