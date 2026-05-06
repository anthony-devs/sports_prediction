# Sports Prediction Engine ⚽📊
### Football Match Outcome Predictor — Python

A Python-based football match outcome predictor that combines historical EPL data with live API data to forecast match results. Built as a backend data science project to explore sports analytics and prediction modelling.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-API-000000?style=flat-square&logo=flask&logoColor=white)
![Data](https://img.shields.io/badge/Data-EPL_2022--23-38003C?style=flat-square)

---

## What It Does

Predicts football match outcomes by analysing historical English Premier League results combined with live fixture data from a sports API. The engine processes team form, head-to-head records, and historical patterns to generate match outcome probabilities.

---

## How It Works

1. **Historical data** — EPL 2022/23 season results loaded from `epl_results_2022-23.csv`
2. **Live data** — Current fixture and team data fetched from a sports API (configured in `api.txt`)
3. **Prediction logic** — `main.py` processes both datasets to generate win/draw/loss probabilities
4. **API layer** — `app.py` exposes predictions via a Flask REST endpoint
5. **Testing** — `test.py` and `test.json` for validating prediction outputs

---

## Project Structure

```
sports_prediction/
├── app.py                    # Flask API exposing prediction endpoint
├── main.py                   # Core prediction logic
├── test.py                   # Test suite
├── test.json                 # Sample test fixtures
├── epl_results_2022-23.csv   # Historical EPL season data
├── api.txt                   # API configuration
└── info.txt                  # Project notes
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| API Layer | Flask |
| Data | CSV (EPL historical), Live sports API |
| Analysis | Custom statistical modelling |

---

## Running Locally

```bash
git clone https://github.com/anthony-devs/sports_prediction
cd sports_prediction
pip install flask requests pandas
python app.py
```

Then call the prediction endpoint:
```bash
curl http://localhost:5000/predict?home=Arsenal&away=Chelsea
```

---

## Built By

**Anthony Ude** — Full-Stack Developer
[github.com/anthony-devs](https://github.com/anthony-devs) · [LinkedIn](https://linkedin.com/in/anthony-ude-882b45263)
