#!/usr/local/bin/bash

zappa deploy

cd deployment
terraform init
terraform apply -auto-approve
cd ..

zappa update