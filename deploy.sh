#!/bin/bash
set -e

VPS_HOST="172.245.152.30"
VPS_USER="root"
BLOG_DIR="/var/www/blog"

echo "🔨 Building Hugo site..."
hugo --minify

echo "📁 Ensuring remote directory exists..."
ssh -o StrictHostKeyChecking=no ${VPS_USER}@${VPS_HOST} "mkdir -p ${BLOG_DIR}"

echo "🚀 Deploying to VPS via rsync..."
rsync -avz --delete -e "ssh -o StrictHostKeyChecking=no" public/ ${VPS_USER}@${VPS_HOST}:${BLOG_DIR}/

echo "🔄 Reloading nginx..."
ssh -o StrictHostKeyChecking=no ${VPS_USER}@${VPS_HOST} "sudo systemctl reload nginx"

echo "✅ Deploy complete!"
