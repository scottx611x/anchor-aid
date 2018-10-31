#!/usr/local/bin/bash

cd terraform
terraform init
terraform apply -auto-approve
cd ..

cd flask_app
zappa deploy dev
zappa update dev
cd ..