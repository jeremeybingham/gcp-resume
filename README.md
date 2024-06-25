# 🌤️ GCP Resume

A resume hosted on **Google Cloud** Check it out [here](https://gcp-resume.jeremeybingham.com).

## 🚀 Deployment & Features

- Deployed via a **Cloud Build Trigger** on changes to this repository.
- Utilizes **GCP CI/CD pipeline** and logging for continuous integration.
- A `Flask` app using `DuckDB` for simple "static" storage.
- Containerized with **Docker** and deployed to [Google Cloud Run](https://cloud.google.com/run) as a serverless application. Learn more about [integrating custom domains with Cloud Run](https://cloud.google.com/run/docs/integrate/custom-domain-load-balancer).
- **GCP Load Balancer** handles routing, DNS, and SSL. For more details, visit [GCP Load Balancing Console](https://console.cloud.google.com/net-services/loadbalancing).
- Main domain `jeremeybingham.com` hosted on **AWS Route 53**. For DNS setup, check out [AWS Route 53 Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html).

## 🔧 Technical Details

More details to come!
