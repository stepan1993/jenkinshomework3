pipeline {
	agent {
		label 'docker'
	    }
	environment {
		imagename = 'homework4ci'
		Dockerhub = '6772f8b9-5edc-4b40-ad8c-966a632ba272'
		registry = 'stepan93/jenkinshomework3'
	}
	stages {
		stage('Checkout code from git') {
			steps {
				git(
       url: 'https://github.com/stepan1993/jenkinshomework3.git',
       branch: "main"
    )
			}
		}
		stage('Build docker image'){
			steps {
				script
				{
					dockerImage = docker.build registry + ":$BUILD_NUMBER"
				}
			}
		}
		stage('Push image to Dockerhub repo'){
			steps {
				script	
				{
					docker.withRegistry( '', Dockerhub ) {
						dockerImage.push()
					}
				}
			}
		}
		stage('Deploy to Dev environment'){
			steps {
docker.withServer('', Dockerhub) {
        docker.image('$registry:$BUILD_NUMBER').withRun('-p 8081:80') {
            /* do things */
        }
    }
			
			}
		}
		stage('Go to prod'){
			steps {
				input "Go to prod"
			}
		}
		stage("Deploy to Prod environment"){
			agent { label 'docker' }
			steps }
			docker.withServer('', Dockerhub) {
        docker.image('mysql:5').withRun('-p 3306:3306') {
            /* do things */
        }}
    }

			
		
		}


			
	}	
	
}
