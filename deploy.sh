#!/usr/local/bin/bash

zappa deploy production

cd deployment
terraform init
terraform apply -auto-approve
cd ..

zappa update production