import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import time
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.datasets import make_regression, load_diabetes
    from sklearn.linear_model import (
        LinearRegression, Ridge, Lasso, BayesianRidge
    )
    from sklearn.preprocessing import PolynomialFeatures, StandardScaler
    from sklearn.metrics import mean_squared_error, r2_score
    return (
        BayesianRidge,
        LinearRegression,
        PolynomialFeatures,
        load_diabetes,
        mean_squared_error,
        mo,
        np,
        plt,
        r2_score,
        train_test_split,
    )


@app.cell
def _(np):
    np.random.seed(42)
    return


@app.cell
def _(load_diabetes, train_test_split):
    diabetes = load_diabetes()
    X, y = diabetes.data, diabetes.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_test, X_train, y_test, y_train


@app.cell
def _(
    LinearRegression,
    X_test,
    X_train,
    mean_squared_error,
    np,
    r2_score,
    y_test,
    y_train,
):
    ols = LinearRegression()
    ols.fit(X_train, y_train)

    y_pred_ols = ols.predict(X_test)
    print(f"Coefficients: {ols.coef_}")
    print(f"Intercept: {ols.intercept_:.2f}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_ols))}")
    print(f"R2: {r2_score(y_test, y_pred_ols)}")
    return (ols,)


@app.cell
def _(X_train, np):
    X_one = np.concat([np.ones((len(X_train), 1)), X_train], axis=1)
    return (X_one,)


@app.cell
def _(X_one, np, y_train):
    betas = np.linalg.solve(X_one.T @ X_one, X_one.T @ y_train)
    betas
    return


@app.cell
def _(X_train, ols, plt, y_train):

    plt.hist(y_train - ols.predict(X_train))
    return


@app.cell
def _(X_test, ols, plt, y_test):
    plt.hist(y_test - ols.predict(X_test))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    $$ y = X\beta + \varepsilon,\, \varepsilon \sim \mathcal{N}(0, \sigma^2)  $$

    então, 

    $$ y - X\beta = \varepsilon \sim \mathcal{N}(0, \sigma^2) $$

    $$ E[y] = X\beta $$
    """
    )
    return


@app.cell
def _(np):
    X_poly = np.random.uniform(-2, 2, 300).reshape(-1, 1)
    y_poly = 0.5 * X_poly.ravel()**3 + 0.3 * X_poly.ravel()**2 - 0.2 * X_poly.ravel() + 0.1 * np.random.normal(0, 0.5, 300)
    return X_poly, y_poly


@app.cell
def _(PolynomialFeatures, X_poly, train_test_split, y_poly):
    X_poly_train, X_poly_test, y_poly_train, y_poly_test = train_test_split(X_poly, y_poly, test_size=0.2, random_state=42)
    poly_features = PolynomialFeatures(degree=3, include_bias=False)
    X_poly_transformed = poly_features.fit_transform(X_poly_train)
    X_poly_transformed_test = poly_features.fit_transform(X_poly_test)
    return (
        X_poly_transformed,
        X_poly_transformed_test,
        poly_features,
        y_poly_train,
    )


@app.cell
def _(
    LinearRegression,
    X_poly_transformed,
    X_poly_transformed_test,
    y_poly_train,
):
    poly_reg = LinearRegression()
    poly_reg.fit(X_poly_transformed, y_poly_train)
    y_poly_predict = poly_reg.predict(X_poly_transformed_test)
    return (poly_reg,)


@app.cell
def _(X_poly, np, plt, poly_features, poly_reg, y_poly):
    new_test = poly_features.fit_transform(np.linspace(-5, 5, 100).reshape(-1,1))
    new_predict = poly_reg.predict(new_test)
    plt.plot(new_test[:, 0], new_predict, 'ro') 
    plt.plot(X_poly, y_poly, 'bo') 
    return


@app.cell
def _(BayesianRidge, np):
    X_bayes = np.random.uniform(-2, 2, 300).reshape(-1, 1)
    y_bayes = - 0.2 * X_bayes.ravel() + 10 + 0.1 * np.random.normal(0, 0.5, 300)

    X_test_bayes = np.linspace(-2, 2, 300).reshape(-1,1)

    bayes_simple = BayesianRidge()
    bayes_simple.fit(X_bayes, y_bayes)

    y_plot_mean, y_plot_std = bayes_simple.predict(X_test_bayes, return_std=True)
    return X_bayes, X_test_bayes, y_bayes, y_plot_mean, y_plot_std


@app.cell
def _(X_bayes, X_test_bayes, plt, y_bayes, y_plot_mean, y_plot_std):
    plt.fill_between(X_test_bayes.ravel(), y_plot_mean - 2*y_plot_std, y_plot_mean + 2*y_plot_std, alpha=0.3)
    plt.plot(X_bayes, y_bayes, 'ro')
    plt.plot(X_test_bayes, y_plot_mean)
    return


if __name__ == "__main__":
    app.run()
