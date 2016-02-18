node {
  stage "Checkout"
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm relativeTargetDir:'build'
  sh "git rev-parse HEAD > gitcommit"
  def GIT_COMMIT = readFile('gitcommit').trim()
  sh "rm gitcommit"
  echo "At commit $GIT_COMMIT"

  stage "Build Base Image"
  def baseImage = docker.build("gcr.io/dropcam-dev/jenkinstest-base:$GIT_COMMIT", 'docker/app')
  // docker.withRegistry('https://gcr.io/dropcam-dev', 'gcr:dropcam-dev') {
  //   def base = docker.build('jenkinstest-base', 'docker/app')
  //   base.tag(GIT_COMMIT)
  //   sh "docker images"
  // }
  stage "Run Tests"
  def testImage = docker.build("gcr.io/dropcam-dev/jenkinstest-test:$GIT_COMMIT", 'docker/test')
  // testImage.run("--rm -v ${env.WORKSPACE}/build:/build ")
  // docker run --rm --volumes-from jenkinstest_develop_hash_data -v `pwd`:/output jenkinstest-test
}