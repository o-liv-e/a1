pipeline {
    agent any

    stages {
        // Stage 1: Checkout
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 2: Install Dependencies
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        // Stage 3: Run Unit Tests (verbose)
        stage('Run Unit Tests (verbose)') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}
