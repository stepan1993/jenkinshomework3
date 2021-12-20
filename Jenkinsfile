pipeline {

	environment {
		imagename = 'homework4ci'
		Dockerhub = '9811a256-c0d9-448e-803c-cfc78eedf04b'
	}
	stages {
		stage('Checkout code from git') {
			steps {
			//git config
			git 'https://github.com/stepan1993/jenkinshomework3'
			}
		}
		stage('Build docker image'){
			steps {
				script
				{
					dockerImage = docker.build imagename
				}
			}
		}
		stage('Push image to Dockerhub repo'){
			steps {
				script	
				{
					docker.withRegistry( registry, Dockerhub) {
						dockerImage.push("$BUILD_NUMBER")
						dockerImage.push('latest')
					}
				}
			}
		}
	}	
	
}
