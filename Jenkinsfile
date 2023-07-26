pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages {
        stage('Build') {
            steps {
                // sh 'pwd'
                // sh 'cd frontend && docker build -t israelma/red_project_front:v1 .'
                // sh 'cd ..'
                // sh 'cd server && docker build -t israelma/red_project_server:v1 .'
                // sh 'cd ..'
                sh 'docker images'
            }
        }
        stage('Run images') {
            steps {
                sh 'docker run -d -p3000:3000 israelma/red_project_front:v1'
                sh 'sleep 5'
                sh 'docker run -d -p3001:3001 israelma/red_project_server:v1'
                sh 'sleep 5'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest --junitxml=test-results.xml test/test.py'
            }
            
        }
        stage('Dockerhub login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push to DockerHub') {
            steps {
                 sh 'docker push israelma/red_project_front:v1'
                 sh 'docker push israelma/red_project_server:v1'
            }
        }
        stage('Remove images') {
            steps {
                sh 'docker kill $(docker ps -q)'
                sh 'echo docker rmi -f israelma/red_project_front:v1'
                sh 'echo docker rmi -f israelma/red_project_server:v1'
            }        
        }
    }
    post {
        always {
            sh 'docker logout'
        }   
    }  
}
