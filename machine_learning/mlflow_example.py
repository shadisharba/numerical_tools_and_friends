"""
MLflow is a platform to manage Machine Learning (ML) Lifecycle, which includes ETL, feature engineering, training, scoring, and monitoring model. MLflow can be integrated within the ML Lifecycle at any stage, depending on what users want to track.
Do note that there is a concept of experiment ID and experiment name, run ID and run name which cannot be mixed up!
"""

import mlflow

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123
)

EXPERIMENT_NAME = "mlflow-demo"
EXPERIMENT_ID = mlflow.create_experiment(EXPERIMENT_NAME)

for idx, depth in enumerate([1, 2, 5, 10, 20]):
    clf = DecisionTreeClassifier(max_depth=depth)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Start MLflow
    RUN_NAME = f"run_{idx}"
    with mlflow.start_run(experiment_id=EXPERIMENT_ID, run_name=RUN_NAME) as run:
        # Retrieve run id
        RUN_ID = run.info.run_id

        # Track parameters
        mlflow.log_param("depth", depth)

        # Track metrics
        mlflow.log_metric("accuracy", accuracy)

        # Track model
        mlflow.sklearn.log_model(clf, "classifier")
