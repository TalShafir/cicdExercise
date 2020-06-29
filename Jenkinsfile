pipeline {
    agent {
        docker
        {
            image 'python:3.8'
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