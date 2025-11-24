#!/bin/sh
set -e

# 先运行训练脚本
echo "Starting training with python train.py..."
python train.py

# 训练结束后启动 MLflow UI，绑定所有地址以便外部访问
echo "Starting MLflow UI on 0.0.0.0:5000..."
exec python -m mlflow ui --host 0.0.0.0 --port 5000
