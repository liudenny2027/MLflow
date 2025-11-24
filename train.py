# 最小可运行 MLflow 示例：训练一个线性回归并记录参数/指标/模型
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn


def main():
    data = load_diabetes()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    # 开始一个 MLflow 运行
    with mlflow.start_run() as run:
        # 简单参数（示例）
        model_type = "LinearRegression"
        mlflow.log_param("model_type", model_type)

        # 训练
        model = LinearRegression()
        model.fit(X_train, y_train)

        # 评估
        preds = model.predict(X_test)
        mse = mean_squared_error(y_test, preds)
        mlflow.log_metric("mse", mse)

        # 保存模型到 MLflow（artifact 路径为 "model"）
        mlflow.sklearn.log_model(model, artifact_path="model")

        print(f"Logged run {run.info.run_id} with mse={mse}")


if __name__ == "__main__":
    main()
