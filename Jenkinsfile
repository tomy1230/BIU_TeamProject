pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'cd frontend && docker build -t front:v1 .'
                sh 'cd ..'
                sh 'cd server && docker build -t server:v1 .'
                sh 'cd ..'
                sh 'docker images'
            }
        }
        stage('Run images') {
            steps {
                sh 'docker run -d front:v1'
                sh 'sleep 10'
                sh 'docker run -d server:v1'
                sh 'sleep 10'
            }
        }
        stage('Test') {
            steps {
                sh 'cd test && pip3 install -r requirements.txt'
                sh 'python3 test.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Remove images') {
            steps {
                sh 'docker rmi -f front:v1'
                sh 'docker rmi -f server:v1'
            }
        }
    }
}