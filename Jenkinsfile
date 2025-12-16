pipeline {
    agent { label 'docker' }

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker rm -f flask_app || true
                docker run -d --name flask_app -p 5000:5000 jenkins-flask-app
                '''
            }
        }
    }
}
