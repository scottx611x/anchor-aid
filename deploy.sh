#!/usr/local/bin/bash

cd deployment
terraform init
terraform apply -auto-approve
cd ..

zappa deploy production
zappa update production
zappa certify --yes