node {
  stage "Checkout"
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  sh "git rev-parse HEAD > gitcommit"
  def GIT_COMMIT = readFile(gitcommit).trim()
  echo 'At commit $GIT_COMMIT'
  stage "Build Base Image"
}