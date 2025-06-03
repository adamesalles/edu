import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell
def _():
    import sqlite3
    import marimo as mo
    import pandas as pd
    import os
    return mo, os, pd, sqlite3


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Tutorial de Pandas e SQLite

        Bem-vindo a este tutorial interativo em Python usando o **marimo** — um ambiente moderno de notebooks.

        Neste notebook, você aprenderá a:
        - Criar e consultar um banco de dados SQLite com `sqlite3`
        - Carregar, explorar e manipular dados usando `pandas`
        - Utilizar as células do `marimo` para tornar a experiência interativa

    ---

        ⚠️ **Nota**: O Marimo é semelhante ao Jupyter Notebook, outra ferramenta popular. Mas o `marimo` oferece melhor estrutura, reatividade e controle de versão.
    """
    )
    return


@app.cell
def cell3(os, sqlite3):
    os.remove("tutorial.sqlite")
    conn = sqlite3.connect("tutorial.sqlite") #:memory:
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    """)
    cursor.executemany("""
    INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
    """, [
        ("Eduardo", 22, "F-"),
        ("Marcos", 23, "A+"),
        ("João", 23, "C+"),
        ("Yuri", 23, "B-")
    ])
    conn.commit()
    return (conn,)


@app.cell
def cell4(conn, pd):
    df_students = pd.read_sql_query("SELECT * FROM students", conn)
    df_students
    return (df_students,)


@app.cell
def cell6(df_students):
    summary = df_students.describe()
    summary.T
    return


@app.cell
def _(df_students):
    grouped = df_students.groupby("grade").size()
    grouped
    return


@app.cell(hide_code=True)
def cell8(mo):
    mo.md(
        r"""
    ## Salvando e Carregando DataFrames com SQLite

    Você pode usar `pandas.to_sql()` para salvar um DataFrame no SQLite:

    ```python
    df_students.to_sql("students_backup", conn, index=False, if_exists="replace")
    ```

    E depois carregar com:

    ```python
    df_loaded = pd.read_sql("SELECT * FROM students_backup", conn)
    ```
    """
    )
    return


@app.cell
def _(conn, df_students):
    df_students.to_sql("students_backup", conn, index=False, if_exists="replace")
    return


@app.cell
def _(conn, pd):
    df_loaded = pd.read_sql("SELECT * FROM students_backup", conn)
    df_loaded
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT name FROM students_backup
        """,
        engine=conn
    )
    return


if __name__ == "__main__":
    app.run()
