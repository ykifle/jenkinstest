node {
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  withEnv(['GIT_COMMIT=`git rev-parse HEAD`']) {
    echo "At commit $GIT_COMMIT"
  }
}