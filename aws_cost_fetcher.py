import boto3
from datetime import datetime

def get_aws_cost():
    # Initialize the Cost Explorer client
    client = boto3.client('ce')

    # Define the time period (last 30 days)
    start_date = (datetime.now().replace(day=1)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')

    # Fetch costs from AWS Cost Explorer
    response = client.get_cost_and_usage(
        TimePeriod={'Start': start_date, 'End': end_date},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    # Process and return the result
    cost_data = []
    for result in response['ResultsByTime'][0]['Groups']:
        service = result['Keys'][0]
        cost = result['Metrics']['UnblendedCost']['Amount']
        cost_data.append({'service': service, 'cost': float(cost)})
        
    return cost_data