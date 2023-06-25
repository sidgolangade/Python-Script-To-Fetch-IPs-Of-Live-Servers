## Autoscaling Group IP Fetcher
This Python script allows you to fetch the IP addresses of live servers in an Autoscaling Group in AWS. It also provides the option to retrieve the IP address of a specific EC2 instance within the Autoscaling Group.

### Prerequisites
- Python 3.x installed
- Boto3 library installed (pip install boto3)
- EC2 Instance (or Instances)
- Attach IAM Roles (`AmazonEC2FullAccess` & `AutoScalingFullAccess`) to the EC2 Instance (or Instances)
- AWS credentials configured with appropriate permissions to access EC2 and Autoscaling resources
- AWS Auto Scaling Group already configured (Launch Template, etc)

### Usage
This script will retrieve the IP addresses of all live servers in the specified autoscaling group and display them.
If you provide an EC2 instance ID, it will fetch the IP address of that specific instance.

