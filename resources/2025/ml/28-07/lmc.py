import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    from statsmodels.discrete.discrete_model import Logit
    from sklearn.linear_model import (
        LogisticRegression, SGDClassifier
    )
    from sklearn.metrics import (
        accuracy_score, roc_auc_score
    )
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import make_classification, load_breast_cancer, load_iris, load_wine

    import warnings
    warnings.filterwarnings('ignore')

    np.random.seed(42)
    return (
        LogisticRegression,
        Logit,
        accuracy_score,
        load_breast_cancer,
        mo,
        np,
        roc_auc_score,
        sm,
        train_test_split,
    )


@app.cell
def _(load_breast_cancer, train_test_split):
    cancer = load_breast_cancer()
    X, y = cancer.data, cancer.target

    feature_indices = [0, 1, 2, 3, 4]
    X_subset = X[:, feature_indices]
    feature_names = [cancer.feature_names[i] for i in feature_indices]

    X_train, X_test, y_train, y_test = train_test_split(X_subset, y, test_size=0.2, random_state=42)
    return X_test, X_train, y_test, y_train


@app.cell
def _(mo):
    mo.md(
        r"""
    $\text{logit}(Y_{train}) = X_{train}\beta$, encontro o $\hat{\beta}$

    $\text{logit}(Y_{pred}) = X_{test}\hat{\beta}$, espera-se que $Y_{pred} \approx Y_{test}$
    """
    )
    return


@app.cell
def _(LogisticRegression, X_test, X_train, y_train):
    # Scikit-learn
    sklearn_logit = LogisticRegression(random_state=42)
    sklearn_logit.fit(X_train, y_train)
    y_pred_sklearn = sklearn_logit.predict(X_test)
    y_prob_sklearn = sklearn_logit.predict_proba(X_test)[:, 1]
    return (y_prob_sklearn,)


@app.cell
def _(Logit, X_test, X_train, np, sm, y_train):
    # Statsmodels

    X_train_const = sm.add_constant(X_train)
    X_test_const = sm.add_constant(X_test)

    statsmodels_logit = Logit(y_train, X_train_const)
    result = statsmodels_logit.fit(disp=False)

    y_prob_statsmodels = result.predict(X_test_const)
    y_pred_statsmodels = (y_prob_statsmodels > 0.5).astype(np.int8)
    y_pred_statsmodels
    return X_train_const, result, y_prob_statsmodels


@app.cell
def _(X_train, X_train_const):
    X_train, X_train_const
    return


@app.cell
def _(result):
    result.summary2().tables[1]
    return


@app.cell
def _(np, y_prob_sklearn, y_prob_statsmodels):
    np.corrcoef(y_prob_sklearn, y_prob_statsmodels)[0,1]
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    $\text{existe minimo global} \to \text{cond. necessaria}$

    $\lnot(\text{existe minimo global} \to \text{cond. necessaria})$

    $\lnot\text{cond. necessaria} \to \lnot \text{existe minimo global}$
    """
    )
    return


@app.cell
def _(
    LogisticRegression,
    X_test,
    X_train,
    accuracy_score,
    roc_auc_score,
    y_test,
    y_train,
):
    solvers = ['liblinear', 'lbfgs', 'newton-cg', 'sag', 'saga']
    solver_resutls = {}

    for solver in solvers:
        lr = LogisticRegression(solver=solver, max_iter=1000, random_state=42)
        lr.fit(X_train, y_train)
        y_pred = lr.predict(X_test)
        solver_resutls[solver] = {
            'accuracy': accuracy_score(y_test, y_pred),
            'auc': roc_auc_score(y_test, lr.predict_log_proba(X_test)[:, 1]),
            'coef': lr.coef_[0]
        }
    return (solver_resutls,)


@app.cell
def _(solver_resutls):
    solver_resutls
    return


if __name__ == "__main__":
    app.run()
