node {
  echo 'hello from Pipeline4'
  sh 'echo `pwd`'
  sh 'echo `ls -la`'
  checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'website']], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'e01fb2aa-ce9b-4a90-8e26-716ca86a0d66', refspec: '+refs/heads/master:refs/remotes/origin/master', url: 'git@github.com:ykifle/jenkinstest.git']]])
  sh 'echo `pwd`'
  sh 'echo `ls -la`'
}