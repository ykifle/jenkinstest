node {
  stage "Checkout"
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  sh "git rev-parse HEAD > gitcommit"
  def GIT_COMMIT = readFile('gitcommit').trim()
  echo "At commit $GIT_COMMIT"

  stage "Build Base Image"
  def base = docker.build("gcr.io/dropcam-dev/jenkinstest-base:$GIT_COMMIT", 'docker/app')
  // docker.withRegistry('https://gcr.io/dropcam-dev', 'gcr:dropcam-dev') {
  //   def base = docker.build('jenkinstest-base', 'docker/app')
  //   base.tag(GIT_COMMIT)
  //   sh "docker images"
  // }
}