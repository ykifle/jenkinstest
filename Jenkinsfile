node {
  echo env.BRANCH_NAME
  checkout scm
  echo scm.metaClass.methods*.name.sort().unique()
  echo env.GIT_COMMIT
  sh 'env'
}