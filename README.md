# Serverless FastAPI Platform on Google Cloud

A professional, end-to-end backend project demonstrating how to deploy a **FastAPI** application on **Google Cloud Run**, route traffic through an **Nginx reverse proxy** running on a **Compute Engine VM**, and automate application delivery using **GitHub Actions**.

This repository is intentionally accurate and reflects only what is actually implemented.

---

## Architecture

```
Client
  |
  | HTTP
  v
Nginx (Compute Engine VM)
  |
  | HTTPS (Google-managed TLS)
  v
FastAPI Application (Cloud Run)
```

### Architecture Notes

* The FastAPI application runs on **Cloud Run**, which provides autoscaling, load balancing, and managed HTTPS.
* **Nginx** is used as a reverse proxy to demonstrate VM-based infrastructure concepts.
* The Compute Engine VM is publicly accessible on port `80`.
* TLS termination is handled by Cloud Run.

---

## Tech Stack

### Backend

* FastAPI
* Python
* Uvicorn

### Cloud & Infrastructure

* Google Cloud Run
* Google Compute Engine (VM)
* Artifact Registry
* Terraform

### DevOps

* Docker
* GitHub Actions (CI/CD)
* Nginx

---

## What Is Automated

### Automated

* Docker image build
* Image push to Artifact Registry
* Cloud Run deployment via GitHub Actions
* VM and firewall provisioning using Terraform

### Manual (Intentional)

* Nginx installation and configuration on the VM

> Nginx was configured manually to ensure reliability and transparency during setup and debugging. The configuration is version-controlled in the repository for reference.

---

## CI/CD Pipeline

A GitHub Actions workflow is triggered on every push to the `main` branch.

Pipeline steps:

1. Checkout source code
2. Build Docker image
3. Push image to Artifact Registry
4. Deploy updated image to Cloud Run

This enables automated application deployment without manual intervention.

---

## Repository Structure

```
.
├── app/                    # FastAPI application
├── nginx/                  # Nginx configuration reference
├── terraform/              # Infrastructure as Code
├── .github/workflows/      # GitHub Actions CI/CD
├── Dockerfile
├── README.md
```

---

## Setup and Deployment (End-to-End)

### Prerequisites

* Google Cloud account with billing enabled
* Google Cloud SDK (`gcloud`) installed
* Terraform installed
* Docker installed
* GitHub account

---

### Step 1: Google Cloud Setup

1. Create a new Google Cloud project
2. Enable the following APIs:

   * Cloud Run
   * Artifact Registry
   * Compute Engine
3. Create a service account and grant required permissions
4. Download the service account JSON key

---

### Step 2: Artifact Registry

Create a Docker repository in Artifact Registry:

* Region: `us-central1`
* Format: Docker

This repository will store Docker images for the application.

---

### Step 3: Infrastructure Provisioning (Terraform)

1. Navigate to the `terraform/` directory
2. Initialize Terraform:

```bash
terraform init
```

3. Review the plan:

```bash
terraform plan
```

4. Apply the infrastructure:

```bash
terraform apply
```

This creates:

* A Compute Engine VM
* A firewall rule allowing inbound HTTP traffic on port `80`

---

### Step 4: Nginx Setup (Manual)

1. SSH into the VM:

```bash
gcloud compute ssh nginx-vm --zone us-central1-a
```

2. Install Nginx:

```bash
sudo apt update
sudo apt install -y nginx
```

3. Configure Nginx as a reverse proxy to Cloud Run

4. Restart Nginx:

```bash
sudo systemctl restart nginx
```

---

### Step 5: Application Deployment (CI/CD)

1. Push code to the `main` branch
2. GitHub Actions automatically:

   * Builds the Docker image
   * Pushes it to Artifact Registry
   * Deploys the application to Cloud Run

No manual deployment steps are required after this.

---

### Step 6: Access the Application

* VM endpoint:

  ```
  http://<VM_PUBLIC_IP>
  ```

* Cloud Run service URL:

  ```
  https://<cloud-run-service>.run.app
  ```

---

## Key Learnings

* Containerizing FastAPI applications
* Deploying serverless workloads using Cloud Run
* Using GitHub Actions for CI/CD
* Provisioning infrastructure with Terraform
* Configuring Nginx as a reverse proxy
* Understanding cloud infrastructure trade-offs

---

## Limitations and Trade-offs

* Single Nginx VM (no autoscaling)
* No custom domain or external HTTPS load balancer
* Some resources (IAM, Artifact Registry) created manually

These decisions were made intentionally to keep the project focused and practical.

---

## Future Improvements

* Automate Nginx configuration using configuration management tools
* Add HTTPS and custom domain using a managed load balancer
* Add monitoring and logging
* Create a fully serverless version without a VM

---

## Purpose

This project is designed for learning, portfolio demonstration, and interview discussion.
