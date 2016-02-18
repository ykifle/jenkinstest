node {
  stage "Checkout"
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  sh "git rev-parse HEAD>result"
  def GIT_COMMIT = readFile(result).trim()
  echo 'At commit $GIT_COMMIT'
  stage "Build Base Image"
}