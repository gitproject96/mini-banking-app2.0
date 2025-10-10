pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git(
                    url: 'https://github.com/gitproject96/mini-banking-app2.0.git',
                    branch: 'main',
                    credentialsId: 'github-cred'
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def COMMIT = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    env.IMAGE_TAG = "mydocker691/banking-app:${BUILD_NUMBER}-${COMMIT}"

                    echo "Building Docker Image: ${env.IMAGE_TAG}"

                    sh """
                        docker build --build-arg APP_VERSION=${BUILD_NUMBER}-${COMMIT} -t ${env.IMAGE_TAG} .
                    """
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKERHUB_PSW', usernameVariable: 'DOCKERHUB_USER')]) {
                    sh """
                        echo $DOCKERHUB_PSW | docker login -u $DOCKERHUB_USER --password-stdin
                        docker push ${env.IMAGE_TAG}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    script {
                        echo "Deploying new version to Kubernetes..."

                        // Replace image placeholder with new image tag
                        sh """
                            sed -i '/image:/ s|IMAGE_PLACEHOLDER|${env.IMAGE_TAG}|' k8s/deployment.yaml
                        """

                        // Apply deployment & service
                        sh """
                            kubectl --kubeconfig=$KUBECONFIG apply -f k8s/deployment.yaml
                            kubectl --kubeconfig=$KUBECONFIG apply -f k8s/service.yaml
                        """

                        // Rollout restart and wait until available
                        sh """
                            kubectl --kubeconfig=$KUBECONFIG rollout restart deployment banking-app
                            kubectl --kubeconfig=$KUBECONFIG rollout status deployment banking-app
                        """

                        // Show running pods for verification
                        sh "kubectl --kubeconfig=$KUBECONFIG get pods -o wide"
                    }
                }
            }
        }

        stage('Expose Metrics for Prometheus') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG')]) {
                    script {
                        // Annotate deployment for Prometheus scraping
                        sh """
                            kubectl --kubeconfig=$KUBECONFIG annotate deployment banking-app prometheus.io/scrape=true --overwrite
                            kubectl --kubeconfig=$KUBECONFIG annotate deployment banking-app prometheus.io/path=/metrics --overwrite
                            kubectl --kubeconfig=$KUBECONFIG annotate deployment banking-app prometheus.io/port=5000 --overwrite
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully — Banking App deployed & monitored!"
        }
        failure {
            echo "❌ Pipeline failed — check logs for details."
        }
    }
}
