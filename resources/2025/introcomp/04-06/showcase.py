import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import sqlite3
    import marimo as mo
    import pandas as pd
    import seaborn as sns
    return mo, pd, sns, sqlite3


@app.cell
def _(sns):
    df_titanic = sns.load_dataset('titanic')
    df_titanic
    return (df_titanic,)


@app.cell
def _(df_titanic, sqlite3):
    conn = sqlite3.connect("test.sqlite")
    cursor = conn.cursor()
    df_titanic.to_sql("passengers", conn, index=False, if_exists='replace')
    return conn, cursor


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM passengers
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, pd):
    pd.read_sql_query("SELECT * FROM passengers", conn)
    return


@app.cell
def _(cursor):
    lines = cursor.execute("SELECT * FROM passengers").fetchall()
    for line in lines:
        print(line)
    return


@app.cell
def _(df_titanic):
    df_titanic.describe()
    return


@app.cell
def _(df_titanic):
    df_titanic.groupby(['class', 'sex'])["survived"].sum()
    return


@app.cell
def _(df_titanic, pd):
    df_info = pd.DataFrame({
        'class': ['First', 'Second', 'Third'],
        'description': ['Primeira Classe', 'Segunda Classe', 'Não tão rico']
    })
    df_merged = pd.merge(df_titanic, df_info, on='class', how='left')
    df_merged[df_merged["class"] == "Third"]
    return (df_merged,)


@app.cell
def _(df_merged):
    df_merged['is_minor'] = df_merged["age"] < 18
    df_merged
    return


@app.cell
def _(df_merged, sns):
    sns.countplot(df_merged, x="description", hue="sex")
    return


@app.cell
def _():
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT sex, survived, COUNT(*) as total FROM passengers
        GROUP BY sex, survived
        """,
        engine=conn
    )
    return


if __name__ == "__main__":
    app.run()
