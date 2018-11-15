#!/usr/local/bin/bash

zappa deploy

cd deployment
terraform init -backend-config="bucket=anchor-aid-terraform" -backend-config="region=us-east-1" -input=false
terraform apply -auto-approve
cd ..

zappa update