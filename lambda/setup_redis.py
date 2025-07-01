# setup_redis.py
import boto3
import botocore

REGION = "us-east-1"
CLUSTER_NAME = "my-redis-cluster"


def create_redis_cluster():
    client = boto3.client("elasticache", region_name=REGION)

    # Check if the cluster already exists
    try:
        response = client.describe_cache_clusters(CacheClusterId=CLUSTER_NAME)
        if response["CacheClusters"]:
            return f"✅ Redis cluster '{CLUSTER_NAME}' already exists. Skipping creation."
    except botocore.exceptions.ClientError as e:
        if e.response["Error"]["Code"] != "CacheClusterNotFound":
            return f"Error checking cluster: {e}"

    # Create the Redis cluster
    try:
        client.create_cache_cluster(
            CacheClusterId=CLUSTER_NAME,
            Engine="redis",
            CacheNodeType="cache.t2.micro",
            NumCacheNodes=1,
            AZMode="single-az",
            PreferredAvailabilityZone="us-east-1a"
        )
        return f"🚀 Creating Redis cluster: {CLUSTER_NAME}\n✅ Redis cluster '{CLUSTER_NAME}' creation command issued."
    except botocore.exceptions.ClientError as e:
        return f"Error creating cluster: {e}"
