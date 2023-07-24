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
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}