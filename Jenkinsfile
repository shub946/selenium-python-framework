pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Upload Results to XRAY') {
    steps {

        withCredentials([usernamePassword(
            credentialsId: 'xray_apikeys',
            usernameVariable: 'XRAY_CLIENT_ID',
            passwordVariable: 'XRAY_CLIENT_SECRET'
        )]) {

            bat '''
            curl -H "Content-Type: application/json" ^
                 -X POST ^
                 --data "{\\"client_id\\": \\"%XRAY_CLIENT_ID%\\", \\"client_secret\\": \\"%XRAY_CLIENT_SECRET%\\"}" ^
                 https://xray.cloud.getxray.app/api/v2/authenticate > token.txt

            set /p XRAY_TOKEN=<token.txt

            curl -H "Content-Type: text/xml" ^
                 -H "Authorization: Bearer %XRAY_TOKEN%" ^
                 --data @report.xml ^
                 "https://xray.cloud.getxray.app/api/v2/import/execution/junit?projectKey=XSP"
            '''
        }
    }
}