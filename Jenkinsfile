pipeline {
    agent any
    environment {
        SERVER_IP = "1"
        TF_IN_AUTOMATION = 'true'
        TF_CLI_CONFIG_FILE = credentials('tfcloudcreds')
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        ACCESS_KEY = credentials('aws-access')
        SECRET_KEY = credentials('aws-sec')
    }
    stages {
        // Build images from docker files
        stage('build images on local'){
            steps{
                sh 'cd server && docker build -t galdevops/biu12_red_backend_local .'
                sh 'sleep 5'
                sh "cd frontend && docker build --build-arg server_ip=localhost -t galdevops/biu12_red_frontend_local ."
                sh 'sleep 5'
            }
        }
        // Run containers
        stage('Run images on local') {
            steps {
                sh 'docker run -d -p3001:3001 galdevops/biu12_red_backend_local:latest'
                sh 'sleep 5'
                sh 'docker run -d -p3000:3000 galdevops/biu12_red_frontend_local:latest'
                sh 'sleep 5'
            }
        }
        // Run tests -> Test connection
        stage('Test') {
            steps {
                sh 'python3 -m pytest --junitxml=test-results.xml test/test.py'
            }   
        }
        // Update success
        stage('Test alert'){
            steps{
                echo "Test completed successfully, images will be removed"
            }
        }
        // Remove images from local
        stage('Remove images') {
            steps {
                sh 'docker kill $(docker ps -q)'
                sh 'echo docker rmi -f galdevops/biu12_red_backend_local'
                sh 'echo docker rmi -f galdevops/biu12_red_frontend_local'
            }        
        }

        // Initiate TF - initializes a working directory containing TF configuration files
        stage('TF INIT'){
            steps{
                sh 'terraform init -no-color'
            }
        }
        // Terminates TF resources managed by TF project
        stage('TF DESTROY_1'){
            steps{
                sh "terraform destroy -no-color -auto-approve -var 'access_key=${env.ACCESS_KEY}' -var 'secret_key=${env.SECRET_KEY}'"
            }
        }
        // Creates an execution plan, to preview the infrastructure changes that TF plans to make to apply.
        stage('TF PLAN'){
            steps{
                sh "terraform plan -no-color -var 'access_key=${env.ACCESS_KEY}' -var 'secret_key=${env.SECRET_KEY}'"
            }
        }
        // Executes infrastructure changes to each TF resource
        stage('TF APPLY'){
            steps{
                sh "terraform apply -no-color -auto-approve -var 'access_key=${env.ACCESS_KEY}' -var 'secret_key=${env.SECRET_KEY}'"
            }
        }
        // Wait for AWS instance creation is done before continue to the following steps
        stage('EC2 Wait'){
            steps{
                sh "AWS_ACCESS_KEY_ID=${env.ACCESS_KEY} AWS_SECRET_ACCESS_KEY=${env.SECRET_KEY} aws ec2 wait instance-status-ok --region us-east-1"
            }
        }
    }
}