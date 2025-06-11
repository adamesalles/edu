import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    mal = pd.read_csv("resources/2025/introcomp/11-06/myanimelist.csv")
    cr = pd.read_csv("resources/2025/introcomp/11-06/crunchyroll.csv")
    return cr, mal


@app.cell
def _(mal):
    mal
    return


@app.cell
def _(cr):
    cr
    return


@app.cell
def _(mal):
    mal_clean = mal.drop_duplicates(subset='title').copy()
    mal_clean['title'] = (
        mal_clean['title']
        .str.lower()
        .str.replace(r'[^a-z\s]', '', regex=True)
    )
    mal_clean
    return (mal_clean,)


@app.cell
def _(cr):
    cr_clean = (
        cr
        .rename(columns={
            'anime': 'title',
        }).copy()
    )

    cr_clean['title'] = (
        cr_clean['title']
        .str.lower()
        .str.replace(r'[^a-z\s]', '', regex=True)
    )

    cr_clean
    return (cr_clean,)


@app.cell
def _(cr_clean, mal_clean):
    mal_clean['source'] = 'MyAnimeList'
    cr_clean['source'] = 'Crunchyroll'
    return


@app.cell
def _(cr_clean, mal_clean, pd):
    mal_sel = mal_clean[['title', 'episodes', 'members', 'popularity', 'ranked', 'source']]
    cr_sel = cr_clean[['title', 'episodes', 'votes', 'rate', 'source']]

    merged = pd.concat([mal_sel, cr_sel], ignore_index=True)
    merged
    return cr_sel, mal_sel


@app.cell
def _(mal_sel):
    mal_sel.sort_values('members', ascending=False).head(10)[['title', 'members', 'ranked']]
    return


@app.cell
def _(mal_clean):
    mal_clean.sort_values('ranked', ascending=False).head(10)
    return


@app.cell
def _(mal_sel):
    mal_sel.sort_values('episodes', ascending=False).head(10)[['title', 'episodes']]
    return


@app.cell
def _(cr_sel):
    cr_sel.sort_values('episodes', ascending=False).head(10)[['title', 'episodes']]
    return


@app.cell
def _(mal_clean, pd):
    mal_clean['start_date'] = pd.to_datetime(
        mal_clean['aired'].str.split(' to ').str[0],
        format='%b %d, %Y',
        errors='coerce'
    )
    mal_clean['year'] = mal_clean['start_date'].dt.year
    return


@app.cell
def _(mal_clean):
    mal_clean
    return


@app.cell
def _(mal_clean):
    top3_per_year = (
        mal_clean[mal_clean['year'] > 1974]
        .sort_values(['year', 'popularity'])
        .groupby('year')
        .head(3)
        [['year', 'title', 'popularity', 'img_url']]
    )
    top3_per_year
    return


@app.cell
def _(mal_clean):
    top3_score_per_year = (
        mal_clean[mal_clean['year'] > 1974]
        .sort_values(['year', 'score'], ascending=[True, False])
        .groupby('year')
        .head(3)
        [['year', 'title', 'score', 'img_url']]
    )
    top3_score_per_year
    return


@app.cell
def _(mal_clean):
    mal_clean[mal_clean['year'] == 1997].sort_values('score', ascending=False)
    return


if __name__ == "__main__":
    app.run()
