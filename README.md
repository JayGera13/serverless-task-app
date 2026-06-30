# Serverless Task App

A full-stack serverless web application built on AWS that allows users to create and manage tasks.

## Live Demo
http://jay-task-app.s3-website.us-east-2.amazonaws.com

## Architecture
- **Frontend** — HTML/CSS/JavaScript hosted on Amazon S3
- **API** — Amazon API Gateway with REST endpoints
- **Backend** — AWS Lambda functions written in Python
- **Database** — Amazon DynamoDB (NoSQL)

## Features
- View all tasks
- Create new tasks
- Fully serverless — no servers to manage

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Retrieve all tasks |
| POST | /tasks | Create a new task |
| DELETE | /tasks/{taskID} | Delete a task by ID |

## AWS Services Used
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- AWS IAM

## Deployment
Functions are deployed via AWS CLI using zip packaging.