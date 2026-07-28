pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Stop Old App') {
            steps {
                sh 'pkill -f app.py || true'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 app.py > app.log 2>&1 &'
            }
        }
    }
}