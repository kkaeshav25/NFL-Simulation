import streamlit as st
import pandas as pd
import plotly.express as px
import io
import contextlib
from scoring import scoring as simulate_game
import team_data


def get_team_list():
    try:
        return sorted(list(team_data.teams.keys()))
    except Exception:
        # fallback list if module shape changes
        return ["ARI","ATL","BAL","BUF","CAR","CHI","CIN","CLE","DAL","DEN","DET","GB","HOU","IND","JAX","KC","LV","LAC","LAR","MIA","MIN","NE","NO","NYG","NYJ","PHI","PIT","SF","SEA","TB","TEN","WAS"]


st.set_page_config(page_title="NFL Simulator", layout="wide")

st.title("NFL Simulation — Streamlit Prototype")

with st.sidebar:
    st.header("Simulation Settings")
    teams = get_team_list()
    home = st.selectbox("Home team", teams, index=teams.index("GB") if "GB" in teams else 0)
    away = st.selectbox("Away team", teams, index=teams.index("DAL") if "DAL" in teams else 1)
    if home == away:
        st.warning("Home and away are the same — pick different teams to simulate a game")
    num_sims = st.number_input("Number of simulations", min_value=1, max_value=10000, value=1, step=1)
    seed = st.number_input("Random seed (0 = random)", min_value=0, value=0, step=1)
    verbose = st.checkbox("Show play-by-play for single run", value=True)
    run_btn = st.button("Run simulation")


def run_single(home, away, seed, verbose):
    buf = io.StringIO()
    result = None
    with contextlib.redirect_stdout(buf):
        result = simulate_game(home, away)
    logs = buf.getvalue().splitlines()
    # scoring.scoring prints play-by-play and returns a dict
    return result, logs


def run_batch(home, away, num_sims, seed):
    winners = {home: 0, away: 0, "Tie": 0}
    home_scores = []
    away_scores = []
    for i in range(num_sims):
        res, _ = run_single(home, away, seed if seed != 0 else None, verbose=False)
        if res is None:
            continue
        winner = res.get("winner")
        winners[winner] = winners.get(winner, 0) + 1
        home_scores.append(res.get("home_score", 0))
        away_scores.append(res.get("away_score", 0))

    df_summary = pd.DataFrame([
        {"team": home, "wins": winners.get(home, 0), "avg_score": sum(home_scores) / len(home_scores) if home_scores else 0},
        {"team": away, "wins": winners.get(away, 0), "avg_score": sum(away_scores) / len(away_scores) if away_scores else 0},
        {"team": "Tie", "wins": winners.get("Tie", 0), "avg_score": None}
    ])
    return df_summary, home_scores, away_scores


if run_btn:
    if num_sims == 1:
        with st.spinner("Running single simulation..."):
            result, logs = run_single(home, away, seed, verbose)

        st.subheader("Result")
        if result is None:
            st.error("Simulation returned no result")
        else:
            st.metric("Home Score", result.get("home_score", "—"), delta=None)
            st.metric("Away Score", result.get("away_score", "—"), delta=None)
            st.write("Winner:", result.get("winner"))

        if verbose and logs:
            st.subheader("Play-by-play")
            st.code("\n".join(logs), language="text")
            st.download_button("Download log", data="\n".join(logs), file_name=f"{home}_vs_{away}_log.txt")

    else:
        with st.spinner(f"Running {num_sims} simulations... (this may take a while) "):
            df_summary, home_scores, away_scores = run_batch(home, away, int(num_sims), seed)

        st.subheader("Batch summary")
        st.dataframe(df_summary)

        if home_scores and away_scores:
            df_scores = pd.DataFrame({"home": home_scores, "away": away_scores})
            diff = df_scores["home"] - df_scores["away"]
            fig = px.histogram(diff, nbins=40, title="Distribution of score differential (home - away)")
            st.plotly_chart(fig, use_container_width=True)

        st.info("Tip: reduce number of sims while iterating. For large batches consider running the simulation as a background job")

else:
    st.write("Set parameters in the sidebar and click Run simulation")
