# 🚀 Serverless REST API using AWS SAM

A serverless REST API built using **AWS Serverless Application Model (AWS SAM)** and **Python**. This project demonstrates how to build, test, and deploy scalable REST APIs on AWS using **AWS Lambda**, **Amazon API Gateway**, and **AWS CloudFormation**.

---

## 📌 Project Overview

This project implements a RESTful API following a serverless architecture. Instead of managing traditional servers, the application runs on AWS Lambda functions, while Amazon API Gateway exposes HTTP endpoints to clients.

The application is deployed using AWS SAM, which simplifies infrastructure management through Infrastructure as Code (IaC).

---

## ✨ Features

- RESTful API implementation
- Serverless architecture
- AWS Lambda functions
- Amazon API Gateway integration
- Infrastructure as Code using AWS SAM
- Local testing using SAM CLI
- Easy deployment to AWS
- Authentication token generation utility
- Modular project structure

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Framework:** AWS Serverless Application Model (SAM)
- **Cloud Platform:** Amazon Web Services (AWS)
- **Services Used:**
  - AWS Lambda
  - Amazon API Gateway
  - AWS CloudFormation
- AWS CLI
- SAM CLI
- Git & GitHub

---

## 📂 Project Structure

```
Serverless-REST-API/
│
├── src/
│   ├── auth/
│   ├── handlers/
│   ├── requirements.txt
│   └── ...
│
├── generate_token.py
├── requirements.txt
├── samconfig.toml
├── template.yaml
├── template.yaml.save
└── README.md
```

---

## ⚙️ Prerequisites

Before running this project, install the following:

- Python 3.x
- Git
- AWS CLI
- AWS SAM CLI
- Docker Desktop

Configure your AWS credentials:

```bash
aws configure
```

Enter:

- AWS Access Key ID
- AWS Secret Access Key
- Default Region
- Output Format

---

## 📥 Clone the Repository

```bash
git clone https://github.com/Ashithareddy26/Serverless-REST-API.git

cd Serverless-REST-API
```

---

## 📦 Install Dependencies

Install project dependencies:

```bash
pip install -r requirements.txt
```

If required:

```bash
pip install -r src/requirements.txt
```

---

## 🔨 Build the Application

```bash
sam build
```

---

## ▶️ Run the API Locally

```bash
sam local start-api
```

The API will be available at:

```
http://127.0.0.1:3000
```

---

## 🚀 Deploy to AWS

First deployment:

```bash
sam deploy --guided
```

Subsequent deployments:

```bash
sam deploy
```

---

## 🔐 Authentication

The project includes a helper script:

```
generate_token.py
```

This script generates authentication tokens for testing secured API endpoints.

---

## 📄 Configuration Files

### template.yaml

Defines:

- Lambda Functions
- API Gateway
- IAM Roles
- Runtime
- Environment Variables
- Event Triggers

### samconfig.toml

Stores deployment configuration including:

- Stack Name
- AWS Region
- S3 Bucket
- Deployment Parameters

---

## 🧪 Useful Commands

### Build

```bash
sam build
```

### Validate

```bash
sam validate
```

### Run Locally

```bash
sam local start-api
```

### Deploy

```bash
sam deploy
```

### Delete Stack

```bash
sam delete
```

---

## 📖 Learning Outcomes

This project demonstrates:

- Serverless Computing
- REST API Development
- AWS Lambda
- Amazon API Gateway
- Infrastructure as Code (IaC)
- AWS SAM Deployment
- CloudFormation Templates
- API Authentication

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 👩‍💻 Author

**Ashitha Reddy**

- GitHub: https://github.com/Ashithareddy26

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

---

## 📜 License

This project is created for educational and learning purposes.
