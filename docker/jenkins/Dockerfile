FROM ubuntu:14.04
MAINTAINER yohannesk <yohannesk@nestlabs.com>

RUN apt-get update && apt-get install -y wget apache2 openjdk-7-jdk
RUN apt-get install -y apt-transport-https
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
RUN sh -c 'echo deb https://apt.dockerproject.org/repo ubuntu-trusty main > /etc/apt/sources.list.d/docker.list'

RUN apt-get update -y
RUN apt-get install -y jenkins apt-transport-https ca-certificates apparmor docker-engine=1.10.1-0~trusty

ENV JENKINS_HOME /var/jenkins_home
ENV JENKINS_SLAVE_AGENT_PORT 50000

RUN mkdir -p /var/jenkins_home

ENV JENKINS_UC https://updates.jenkins-ci.org
RUN chown -R jenkins "$JENKINS_HOME"
VOLUME /var/jenkins_home

RUN usermod -g docker -G jenkins jenkins
RUN touch /var/run/docker.sock
RUN chown :docker /var/run/docker.sock

# for main web interface:
EXPOSE 8080

# will be used by attached slave agents:
EXPOSE 50000

USER jenkins

ENTRYPOINT ["java", "-jar", "/usr/share/jenkins/jenkins.war"]