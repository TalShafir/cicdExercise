pipeline {
    agent { docker { image 'python:rc-alpine3.12' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m pip install --update pip; python -m pip install pylint'
            }
            steps {
                sh 'pylint ./*.py'
            }
            steps {
                sh 'python -m unittest discover .'
            }
        }
    }
}