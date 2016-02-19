node {
  stage "Checkout"
  echo "Checkout ${env.BRANCH_NAME}"
  checkout scm
  sh "git rev-parse HEAD > gitcommit"
  def GIT_COMMIT = readFile('gitcommit').trim()
  sh "rm gitcommit"
  echo "At commit $GIT_COMMIT"

  stage "Pull Base Image"
  sh 'docker login -e 1234@5678.com -u _json_key -p "$(cat /etc/test-jenkins.json)" https://gcr.io'
  def baseImage = docker.image('gcr.io/dropcam-dev/jenkinstest-base:1.0')
  baseImage.pull()
  //docker.withRegistry('https://gcr.io', 'gcr:dropcam-dev') {
  //  baseImage.pull()
  //}
  //def baseImage = docker.build("gcr.io/dropcam-dev/jenkinstest-base:$GIT_COMMIT", 'docker/app')
  // Tag with latest so building other images will work
  //baseImage.tag('latest')
  // docker.withRegistry('https://gcr.io/dropcam-dev', 'gcr:dropcam-dev') {
  //   def base = docker.build('jenkinstest-base', 'docker/app')
  //   base.tag(GIT_COMMIT)
  //   sh "docker images"
  // }

  stage "Run Tests"
  def testImage = docker.build("gcr.io/dropcam-dev/jenkinstest-test:$GIT_COMMIT", 'docker/test')
  def testContainer = testImage.run("-v ${env.WORKSPACE}:/build gcr.io/dropcam-dev/jenkinstest-test:$GIT_COMMIT")
}