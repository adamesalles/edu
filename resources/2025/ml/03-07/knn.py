import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay
    from sklearn.datasets import make_classification, make_blobs
    import seaborn as sns
    return (
        ConfusionMatrixDisplay,
        KNeighborsClassifier,
        accuracy_score,
        confusion_matrix,
        make_blobs,
        np,
        plt,
        train_test_split,
    )


@app.cell
def _(np):
    SEED = 40
    np.random.seed(SEED)
    return (SEED,)


@app.cell
def _(SEED, make_blobs):
    X, y = make_blobs(n_samples=1200, n_features=2, centers=2, cluster_std=5, random_state=SEED)
    return X, y


@app.cell
def _(X, plt, y):
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
    return


@app.cell
def _(SEED, X, train_test_split, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)
    return X_test, X_train, y_test, y_train


@app.cell
def _(X_test, X_train, np, plt, y_train):
    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', edgecolor='k', s=50)
    plt.scatter(X_test[:, 0], X_test[:, 1], c=np.ones(360)*4, cmap='Reds', edgecolor='k', s=50)
    return


@app.cell
def _(KNeighborsClassifier, X_train, y_train):
    k_num = 11
    knn_classifier = KNeighborsClassifier(n_neighbors=k_num)
    knn_classifier.fit(X_train, y_train)
    ...
    return (knn_classifier,)


@app.cell
def _(X_test, knn_classifier):
    y_pred_sklearn = knn_classifier.predict(X_test)
    return (y_pred_sklearn,)


@app.cell
def _(accuracy_score, y_pred_sklearn, y_test):
    accuracy_sklearn = accuracy_score(y_test, y_pred_sklearn)
    accuracy_sklearn
    return


@app.cell
def _(
    ConfusionMatrixDisplay,
    confusion_matrix,
    knn_classifier,
    plt,
    y_pred_sklearn,
    y_test,
):
    cm = confusion_matrix(y_test, y_pred_sklearn, labels=knn_classifier.classes_, normalize='true')
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=knn_classifier.classes_)
    disp.plot()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
