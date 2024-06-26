# 🌤️ Google Cloud Run Resume

This repository contains the code for: [gcp-resume.jeremeybingham.com](https://gcp-resume.jeremeybingham.com).

### Some other resume templates in progress, inspired by the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/):

📝 **S3 Static via Terraform** version: [resume.jeremeybingham.com](https://resume.jeremeybingham.com) 
repo/code: [gcp-resume](https://github.com/jeremeybingham/resume)

💽 **S3 Static with Github Actions CI/CD** version: [aws-s3-static.jeremeybingham.com](https://aws-s3-static.jeremeybingham.com) 
repo/code: [aws-s3-static](https://github.com/jeremeybingham/aws-s3-static)

## 🚀 Deployment & Features

- 📦 **Dockerized** and deployed to [Google Cloud Run](https://cloud.google.com/run).
- ⚖️ **GCP Load Balancer** handles routing, DNS, and SSL.
- 📫 Deployed via a **Cloud Build Trigger** when commits are made to the `main` branch of this repository.
- 🔁 Utilizes **GCP CI/CD pipeline** for build and logging/continuous integration.
- ⚗️ `Flask` app using 🦆 `DuckDB` for JSON-based storage suitable for cold starts
- 🌐 Primary domain `jeremeybingham.com` is hosted on **AWS Route 53**, but Google issues SSL certs and handles networking for the subdomain; this is easily done with an `A` record in the AWS Hosted Zone for the domain. Check out [AWS Route 53 Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) for more.

### TODO...
To deploy, set up a Cloud Build Pipeline...
