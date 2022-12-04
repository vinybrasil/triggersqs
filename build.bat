docker build -t triggersqs:latest -t %AWSACCOUNTID%.dkr.ecr.us-east-1.amazonaws.com/triggersqs:latest . -f Dockerfile
aws ecr create-repository --repository-name triggersqs
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 949250876409.dkr.ecr.us-east-1.amazonaws.com 
aws sqs create-queue --queue-name triggersqs_Queue
docker push %AWSACCOUNTID%.dkr.ecr.us-east-1.amazonaws.com/triggersqs:latest 