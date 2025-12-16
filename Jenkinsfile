pipeline {
    agent { label 'docker' }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/pujaraamen2/jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-flask-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                // Remove old container if exists, ignore errors
                sh 'docker rm -f flask_app || true'

                // Run the container, ensure Flask app binds to all interfaces
                sh 'docker run -d --name flask_app -p 5000:5000 jenkins-flask-app'
            }
        }
    }
}
