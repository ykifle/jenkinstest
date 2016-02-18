node {
  stage "Checkout"
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  sh "echo 1234 > result.txt"
  def GIT_COMMIT = readFile(result.txt).trim()
  echo 'At commit $GIT_COMMIT'
  stage "Build Base Image"
}