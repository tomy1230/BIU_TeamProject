pipeline {
    agent any
    environment{
        DOCKERHUB_REPO = "israelma/red_project" 
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages {
        stage('Build') {
            steps {
                sh 'pwd'
                sh 'cd /var/lib/jenkins/workspace/project_pipeline/frontend && docker build -t $(DOCKERHUB_REPO)front$(BUILD_NUMBER) .'
                sh 'cd ..'
                sh 'cd server && docker build -t $(DOCKERHUB_REPO)server$(BUILD_NUMBER) .'
                sh 'cd ..'
                sh 'docker images'
            }
        }
        stage('Run images') {
            steps {
                sh 'docker run -d -p3000:3000 front:v1'
                sh 'sleep 2'
                sh 'docker run -d -p3001:3001 server:v1'
                sh 'sleep 5'
            }
        }
        stage('Test') {
            steps {
                //sh 'pwd'
                sh 'python3 -m pytest --junitxml=test-results.xml test/test.py'
            }
            
        }
        // stage('Publish test results') {
        //     steps {
        //         junit 'test-results.xml'
        //     }
        // }
        stage('Dockerhub login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
        stage('Deploy') {
            steps {
                 sh 'docker push $(DOCKERHUB_REPO)front$(BUILD_NUMBER)'
                 sh 'docker push $(DOCKERHUB_REPO)server$(BUILD_NUMBER)'
            }
        }
        stage('Remove images') {
            steps {
                sh 'docker kill $(docker ps -q)'
                sh 'echo docker rmi -f front:v1'
                sh 'echo docker rmi -f server:v1'
            }
            
        }
        post {
          always {
                sh 'docker logout'
    }
}