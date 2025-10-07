pipeline {
  agent any

  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
    DOCKER_IMAGE = "mydocker691/banking-app"
    KUBECONFIG_CRED = 'kubeconfig'  // the ID (file credential) added in Jenkins
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          // Use BUILD_NUMBER or Git commit short SHA for tag
          COMMIT = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
          IMAGE_TAG = "${env.BUILD_NUMBER}-${COMMIT}"
          env.IMAGE_FULL = "${DOCKER_IMAGE}:${IMAGE_TAG}"
          sh "docker build -t ${env.IMAGE_FULL} ."
        }
      }
    }

    stage('Push to DockerHub') {
      steps {
        sh '''
          echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
          docker push ${IMAGE_FULL}
        '''
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        withCredentials([file(credentialsId: "${KUBECONFIG_CRED}", variable: 'KUBECONFIG_FILE')]) {
          sh '''
            # create a temp manifest with the image replaced
            mkdir -p k8s/tmp
            sed "s|IMAGE_PLACEHOLDER|${IMAGE_FULL}|g" k8s/deployment.yaml > k8s/tmp/deployment.yaml
            kubectl --kubeconfig=$KUBECONFIG_FILE apply -f k8s/tmp/deployment.yaml
            kubectl --kubeconfig=$KUBECONFIG_FILE apply -f k8s/service.yaml || true
            # optionally force a rolling update by setting image
            kubectl --kubeconfig=$KUBECONFIG_FILE set image deployment/banking-app banking-app=${IMAGE_FULL} --record || true
          '''
        }
      }
    }
  }

  post {
    failure {
      echo "Build or deployment failed!"
    }
    success {
      echo "Pipeline completed successfully. Image: ${env.IMAGE_FULL}"
    }
  }
}

