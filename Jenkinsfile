pipeline {
    agent any

    environment {
        DOCKER_TOKEN = credentials('talbrou')
        DOCKER_USERNAME = 'talbrou'
        DOCKER_IMAGE_TAG = 'v1.1.6'
        DOCKER_IMAGE_NAME = 'wog_score_flask'
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

        stage('Make sure no containers are running') {
            steps {
                script {
                    sh 'docker system prune -f'
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
                        docker image tag ${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG} ${DOCKER_USERNAME}/${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}
                        docker login -u talbrou -p ${DOCKER_TOKEN}
                        talbrou/docker push ${DOCKER_USERNAME}/${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}
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
