node {
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  withEnv(['GIT_COMMIT=`git rev-parse HEAD`']) {
    sh 'echo "At commit $GIT_COMMIT"'
  }
}