#!/usr/local/bin/bash

cd deployment
terraform init
terraform apply -auto-approve
cd ..

zappa deploy dev
zappa update dev