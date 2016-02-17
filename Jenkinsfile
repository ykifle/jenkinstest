node {
  echo 'hello from Pipeline4'
  sh 'env'
  sh 'echo `pwd`'
  sh 'echo `ls -la`'
  checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'website']], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'e01fb2aa-ce9b-4a90-8e26-716ca86a0d66', refspec: '+refs/heads/master:refs/remotes/origin/master', url: 'git@github.com:ykifle/jenkinstest.git']]])
  dir('website')
  sh 'echo `pwd`'
  sh 'echo `ls -la`'
  def base = docker.build([image: 'gcr.io/dropcam-dev/jenkinstest-base', dir: 'docker/app'])
}