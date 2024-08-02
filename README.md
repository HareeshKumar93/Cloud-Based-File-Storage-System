# Cloud-Based File Storage System

## Project Description

This project implements a cloud-based file storage system using AWS S3 for scalable storage solutions. It provides a user-friendly interface for file uploads and downloads, with secure access control.

## Technologies

- **AWS S3**: For scalable file storage
- **Python**: Programming language used
- **Flask**: Web framework for Python
- **HTML/CSS**: For the user interface

## Key Features

- **File Uploads**: Allows users to upload files to AWS S3.
- **File Downloads**: Generates secure URLs for file access.
- **User Interface**: Simple HTML form for file uploads.

## Setup Instructions

### 1. Launch an EC2 Instance

1. Log in to AWS Management Console and launch an EC2 instance with Ubuntu Server.
2. Configure the security group to allow HTTP (port 80), HTTPS (port 443), and SSH (port 22).

### 2. Connect to Your EC2 Instance

```bash
ssh -i "your-key-pair.pem" ubuntu@your-ec2-public-dns
### 3.  Set up the Environment
     sudo apt update
     sudo apt upgrade
     sudo apt install python3 python3-pip
     pip install virtualenv
     mkdir myproject
     cd myproject
     virtualenv venv
     source venv/bin/activate
4. Install Dependencies
     pip install Flask boto3
5. Set Up the Flask Application
     5.1 Create the directory structure and files (app.py, templates/index.html).
      5.2 Configure AWS credentials with AWS CLI.
6.  Run the application
       python app.py
The application will be accessible via http://your-ec2-public-dns and the user can upload the files through the web interface an the same files can be accessed through the s3 buckets.
