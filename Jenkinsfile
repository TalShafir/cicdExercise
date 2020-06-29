pipeline {
    agent {
        docker
        {
            image 'python:rc-alpine3.12'
            args '-u root:root'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python -m pip install --user --upgrade pip'
                sh 'python -m pip install --user pylint'
                sh 'pylint ./*.py'
                sh 'python -m unittest discover .'
            }
        }
    }
}