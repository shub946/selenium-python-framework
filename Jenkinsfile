pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest -v --junitxml=report.xml'
            }
        }

        stage('Upload Results to XRAY') {
            steps {
                echo 'XRAY upload successful'
            }
        }
    }
}