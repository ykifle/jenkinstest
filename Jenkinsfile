node {
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  env.GIT_COMMIT = sh 'git rev-parse HEAD'
  withEnv(['GIT_COMMIT=`git rev-parse HEAD`']) {
    echo "At commit $GIT_COMMIT"
  }
}