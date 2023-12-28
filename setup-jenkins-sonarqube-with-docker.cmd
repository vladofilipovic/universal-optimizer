REM 1. Setup Jenkins.

REM 1-1. Pull docker image for Jenikns:

docker pull jenkins/jenkins

REM 1-2. Start Jenkins Docker container from the downloaded image:

docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-vlado jenkins/jenkins:latest

REM 1-3. If everything is OK, Jenkins will listen on port 8080. 

REM 1-4. Unlock Jenkins.

REM 1-5. Install sugestted plug-ins.

REM 1-6. Create the first administrative user. Username will be 'Admin' and password will looks like 'Jenkins'.

REM 1-7. Install SonarQube Scanner Jenkins plugin (Manage Jenkins > Manage Plugins > Available).

REM 2. Setup SonarQube.

REM 2-1. Pull docker image for SonarQube:

docker pull sonarqube

REM 2-2. Start SonarQube Docker container from the downloaded image:

docker run -d --name sonarqube-vlado -p 9000:9000 sonarqube

REM 2-3. If everything is OK, SonarQube will listen on port 9000. 

REM 2-4. Login to SonarQube with the default user 'admin' and password 'admin'

REM 2-5. Set administrative password to be like 'SonarQube'

REM 3. Setup SonarQube Scanner (stand-alone tool that does the actual scanning of the source code and sends results to the SonarQube Server) on the same container as Jenkins.

REM 3-1. Access the Jenkins Docker container from a bash shell like this:

docker exec -it jenkins-vlado bash

REM 3-2. Within that shell, create `sonar-scanner` directory under `/var/jenkins_home` and make that current directory. 

REM 3-3. Download SonarQube Scanner onto the container from the sonar-scanner directory with wget:

wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492-linux.zip

REM 3-4. Unzip the Sonar Scanner binary:
unzip sonar-scanner-cli-3.3.0.1492-linux.zip

REM 3-5. Update Jenkins to point to sonar-scanner binary (Manage Jenkins > Global Tool Configuration > SonarQube Scanner); you will need to uncheck “Install automatically” so you can explicitly set SONAR_RUNNER_HOME to directory `/var/jenkins_home/sonar-scanner/sonar-scanner-3.3.0.1492-linux`

REM 4. Configuring Jenkins and SonarQube - it’s time to configure them to communicate with each other.

REM 4-1. Obtain host IP number e.g. `192.168.56.1`

REM 4-2. In SonarQube, add webhook to point to Jenkins (Administration > Configuration > Webhooks); URL will be in the format http://<host_ip>:8080/sonarqube-webhook  (http://192.168.56.1:8080/sonarqube-webhook)

REM 4-3. In SonarQube, generate an access token that will be used by Jenkins (My Account > Security > Tokens) 

REM 4-4. in Jenkins, add the SonarQube Server IP address and the access token (Manage Jenkins > Configure System > SonarQube Servers); URL will be in the format http://<host_ip>:9000   (http://192.168.56.1:9000)
 