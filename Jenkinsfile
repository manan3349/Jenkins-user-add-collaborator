pipeline {
    //By default, Use any Available Agent
    agent any

    //Declaring Parameters for Pipeline
    parameters {
        choice(choices: ['pull','maintain','admin'], name: 'access_type')
        string(name: 'USER_NAME', description: 'GitHub account Username')
        string(name: 'ORG_NAME', description: 'Organization Name')
    }
    stages {
        //Downloads the code from GitHub.
        stage('GitHub code Download') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'bffa42dc-029f-40dd-835f-79b0f0d92d01', passwordVariable: 'token', usernameVariable: 'authd')]) {
                sh 'sudo curl -H "Authorization: token $token" -H "Accept: application/vnd.github.v3.raw" -o Github_access.py https://raw.githubusercontent.com/To-TheNew/Script/main/Github_access.py'
            }
        }
    }
        // Add collaborator in github.
        stage('Python Code') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'bffa42dc-029f-40dd-835f-79b0f0d92d01', passwordVariable: 'token', usernameVariable: 'authd')]) {
                    sh 'python3 Github_access.py $token ${ORG_NAME} ${access_type} ${USER_NAME}'
                
            }
        }
    }
        
}
}
