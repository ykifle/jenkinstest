node {
  echo 'hello from Pipeline4'
  sh 'env'
  sh 'echo `pwd`'
  sh 'echo `ls -la`'
  checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'website']], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'ab0c8b2e-2e4d-4399-ba68-2731b78889a2', url: 'git@github.com:ykifle/jenkinstest.git']]])
  dir('website/docker/app') {
    docker.build([image: 'gcr.io/dropcam-dev/jenkinstest-base'])
  }
  sh 'echo `pwd`'
  sh 'echo `ls -la`'
}