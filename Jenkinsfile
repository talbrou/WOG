pipeline {
    agent any

    environment {
        DOCKER_TOKEN = credentials('talbrou')
        DOCKER_USERNAME = 'talbrou'
        DOCKER_IMAGE_TAG = 'v1.1.3'
        DOCKER_IMAGE = 'wog_score_flask:${DOCKER_IMAGE_TAG}'
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    git 'https://github.com/talbrou/WOG.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker-compose build"
                }
            }
        }

        stage('Run Docker') {
            steps {
                script {
                    sh "docker-compose up -d"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh "python3 e2e.py"
                }
            }
        }

        stage('Tag Docker Image && Push to Docker hub') {
            steps {
                script {
                    sh '''
                        docker image tag ${DOCKER_IMAGE} ${DOCKER_USERNAME}/${DOCKER_IMAGE}
                        docker login -u talbrou -p ${DOCKER_TOKEN}
                        talbrou/docker push ${DOCKER_USERNAME}/${DOCKER_IMAGE}
                    '''
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
            sh 'docker system prune -f'
        }
    }
}
