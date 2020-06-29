pipeline {
    agent { docker { image 'python:rc-alpine3.12' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install pylint'
                sh 'pylint ./*.py'
                sh 'python -m unittest discover .'
            }
        }
    }
}