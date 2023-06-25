import boto3

def get_ips_of_live_servers(autoscaling_group_name):
    ec2_client = boto3.client('ec2')
    autoscaling_client = boto3.client('autoscaling')

    # Retrieve information about the autoscaling group
    response = autoscaling_client.describe_auto_scaling_groups(AutoScalingGroupNames=[autoscaling_group_name])
    instances = response['AutoScalingGroups'][0]['Instances']

    # Get the instance IDs from the autoscaling group
    instance_ids = [instance['InstanceId'] for instance in instances]

    # Retrieve the public IP addresses of the instances
    response = ec2_client.describe_instances(InstanceIds=instance_ids)
    ips = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            if 'PublicIpAddress' in instance:
                ips.append(instance['PublicIpAddress'])

    return ips

def get_live_ip_of_instance(instance_id):
    ec2_client = boto3.client('ec2')

    # Retrieve information about the instance
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance = response['Reservations'][0]['Instances'][0]

    # Check if the instance has a public IP address
    if 'PublicIpAddress' in instance:
        return instance['PublicIpAddress']
    else:
        return None

# User input for autoscaling group name
autoscaling_group_name = input("Enter the autoscaling group name: ")
ips = get_ips_of_live_servers(autoscaling_group_name)
print("IP addresses of all live servers in the given autoscaling group:", ips)

# User input for EC2 instance ID
instance_id = input("To get the IP of a specific server, enter the EC2 instance ID: ")
live_ip = get_live_ip_of_instance(instance_id)

if live_ip:
    print("Live IP address of the given EC2 instance: ", live_ip)
else:
    print("The instance does not have a public IP address.")
