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
                withCredentials([usernamePassword(
                    credentialsId: 'jira-token',
                    usernameVariable: 'JIRA_USER',
                    passwordVariable: 'JIRA_TOKEN'
                )]) {

                    bat '''
                    curl -H "Content-Type: text/xml" ^
                         -u %JIRA_USER%:%JIRA_TOKEN% ^
                         --data @report.xml ^
                         "https://xray.cloud.getxray.app/api/v2/import/execution/junit?projectKey=XSP"
                    '''
                }
            }
        }
    }
}