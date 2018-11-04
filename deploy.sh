#!/usr/local/bin/bash

cd terraform
terraform init
terraform apply -auto-approve
cd ..

zappa deploy dev
zappa update dev