pipeline {
    agent { docker { image 'python:3.8' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m pip install pylint'
                sh 'pylint ./*.py'
                sh 'python -m unittest discover .'
            }
        }
    }
}