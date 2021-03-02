properties([
    buildDiscarder(logRotator(numToKeepStr: ‘10’)),
])
def label = “worker-${UUID.randomUUID().toString()}”
podTemplate(label: label, containers: [], volumes: [
  hostPathVolume(mountPath: ‘/var/run/docker.sock’, hostPath: ‘/var/run/docker.sock’)
]) { node (label) {
	    if (env.BRANCH_NAME == ‘deployment’ || env.BRANCH_NAME == ‘JenkinsSetup’) {
	        stage(‘Checkout’) {
	            checkout(
	                [
	                    $class                           : ‘GitSCM’,
	                    branches                         : [
	                        [name: env.BRANCH_NAME]
	                    ],
	                    doGenerateSubmoduleConfigurations: false,
	                    extensions                       : [],
	                    submoduleCfg                     : [],
	                    userRemoteConfigs                : [
	                        [
	                            credentialsId: ‘github’,
	                            url          : ‘https://github.com/SDU-eScience/Type3-Docs.git’
	                        ]
	                    ]
	                ]
	            )
	        }
	        def latestTag = sh(script: ‘git describe --abbrev=0 --tags’, returnStdout: true)
		    println(latestTag)
	        if (latestTag.startsWith(“doc-“)) {
		        def commitNumber = latestTag.split(“-”)[1]
		        println(commitNumber)
		        sendAlert(“deploy documentation. Image: dreg.cloud.sdu.dk/type3-docs/user-guide:$commitNumber”)	
	        }
	       
	    }
	}
}
def sendAlert(String alertMessage) {
    withCredentials(
        [string(credentialsId: “slackToken”, variable: “slackToken”)]
    ) {
        slackSend(channel: “docs”, message: alertMessage, tokenCredentialId: ‘slackToken’)
    }
}
