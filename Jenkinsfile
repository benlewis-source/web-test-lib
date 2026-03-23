pipeline {
    agent { label 'linux' }

    stages {
        stage('Install') {
            steps {
                sh 'pip install -e .'
                sh 'playwright install firefox --with-deps'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --browser firefox --junit-xml=results.xml'
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}
