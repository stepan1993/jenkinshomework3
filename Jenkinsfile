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
	}	
	
}
