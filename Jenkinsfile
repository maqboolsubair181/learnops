pipeline {
    agent any

    environment {
        IMAGE_NAME = "maqboolsubair181/flask-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/maqboolsubair181/learnops'
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                 docker build \
                  -t $IMAGE_NAME:$IMAGE_TAG \
                  -f Flask_App/Dockerfile \
                  Flask_App
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('Deploy to App EC2') {
            steps {
                sshagent(credentials: ['app-ec2-key']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@65.1.24.183 "
                      docker pull $IMAGE_NAME:$IMAGE_TAG
                      docker stop flask || true
                      docker rm flask || true
                      docker run -d --name flask -p 5000:5000 $IMAGE_NAME:$IMAGE_TAG
                    "
                    '''
                }
            }
        }
    }
}
