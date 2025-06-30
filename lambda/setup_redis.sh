#!/bin/bash

# Name of your Redis cluster
CLUSTER_NAME="my-redis-cluster"

# Check if the cluster already exists
EXISTING=$(aws elasticache describe-cache-clusters \
  --cache-cluster-id "$CLUSTER_NAME" \
  --region us-east-1 \
  --query "CacheClusters[*].CacheClusterId" \
  --output text 2>&1)

if [[ "$EXISTING" == *"$CLUSTER_NAME"* ]]; then
  echo "✅ Redis cluster '$CLUSTER_NAME' already exists. Skipping creation."
else
  echo "🚀 Creating Redis cluster: $CLUSTER_NAME"

  aws elasticache create-cache-cluster \
    --cache-cluster-id "$CLUSTER_NAME" \
    --engine redis \
    --cache-node-type cache.t2.micro \
    --num-cache-nodes 1 \
    --region us-east-1 \
    --availability-zone us-east-1a

  echo "✅ Redis cluster '$CLUSTER_NAME' creation command issued."
fi
