pipeline {
    agent any
    stages{
        stage('Run Tests') {
            steps{
                sh "bash test.sh"
            }
        }
        stage ('Build and Push Images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"          
            }
        }
        stage ("Manage Configuration & Deploy") {
            steps{
                sh "scp docker-compose.yaml dnd-char-gen-manager:/home/jenkins/docker-compose.yaml"
                sh "ansible-playbook -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
    }
}