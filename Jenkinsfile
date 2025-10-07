pipeline {
    agent any

    environment {
        // DockerHub credentials stored in Jenkins
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred')
        DOCKER_IMAGE = "mydocker691/banking-app"

        // Kubeconfig file stored in Jenkins as Secret File
        KUBECONFIG_FILE = credentials('kubeconfig')
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/gitproject96/mini-banking-app2.0.git', credentialsId: 'github-cred'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Use short git commit as tag
                    COMMIT = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    IMAGE_TAG = "${BUILD_NUMBER}-${COMMIT}"
                    sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                sh """
                echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                docker push ${DOCKER_IMAGE}:${IMAGE_TAG}
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    sh """
                    mkdir -p k8s/tmp
                    # Replace placeholder with the pushed Docker image
                    sed "s|IMAGE_PLACEHOLDER|${DOCKER_IMAGE}:${IMAGE_TAG}|g" k8s/deployment.yaml > k8s/tmp/deployment.yaml
                    # Apply deployment and service
                    kubectl --kubeconfig=$KUBECONFIG apply -f k8s/tmp/deployment.yaml
                    kubectl --kubeconfig=$KUBECONFIG apply -f k8s/service.yaml
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}

