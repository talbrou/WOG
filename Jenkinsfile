pipeline {
    agent any

    environment {
        DOCKER_TOKEN = credentials('talbrou')
        DOCKER_USERNAME = 'talbrou'
        DOCKER_IMAGE = 'wog_score_flask:latest'
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
                    sh "docker-compose up --build"
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
                    sh "python e2e.py"
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
