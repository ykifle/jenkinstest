node {
  stage "Checkout"
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  withEnv(["GIT_COMMIT=${sh 'git rev-parse HEAD'}"]) {
    sh 'echo "At commit $GIT_COMMIT"'
  }
  stage "Build Base Image"
}