# ⚽ Arsenal FC Performance Visualization Tool

A Python tool that fetches and analyzes match data for Arsenal FC in the Premier League. It visualizes key performance metrics such as win/loss distributions, goals scored, and rolling form trends. This tool is perfect for Arsenal fans and analysts who want to visualize the team's performance over time.

---

## 🚀 Features

- 📊 Visualizes Arsenal FC's performance metrics:
  - Match result distribution (Wins, Draws, Losses)
  - Average goals scored and conceded at home vs. away
  - Rolling form trends (average points over the last 5 matches)
- 🔄 Fetches live match data from the [football-data.org](https://www.football-data.org) API
- 🧑‍💻 Generates insightful charts: line graphs, bar charts, and more
- 🗓️ Analyzes performance by season (customizable)

---

## 🔧 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/arsenal-performance-viz.git
   cd arsenal-performance-viz
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain an API key from [football-data.org](https://www.football-data.org)**
   - Register on the website and get your free API key.

5. **Set your API token in the `config.py` file**
   ```python
   API_TOKEN = 'your_api_token_here'
   ```

6. **Run the script**
   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```
arsenal-performance-viz/
├── main.py                 # Main script to fetch data and generate visualizations
├── config.py               # Configuration file to store API token and settings
├── data_processing.py      # Data processing functions for Arsenal match data
├── visualization.py        # Functions to generate visualizations (charts)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📷 Sample Output

- 📈 **Form Trend Chart**: A line chart showing Arsenal's rolling average points over the last 5 matches.
- ⚽ **Goals Home vs. Away**: A bar chart comparing Arsenal's average goals scored and conceded at home and away.
- 🏆 **Match Results Distribution**: A bar chart showing the distribution of wins, draws, and losses.

---

## 📌 TODOs

- [ ] Integrate more metrics like possession stats, shots on target, etc.
- [ ] Add support for other teams or leagues (e.g., Champions League, FA Cup).
- [ ] Build an interactive dashboard with Streamlit for real-time performance analysis.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo, suggest improvements, or submit pull requests.

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for more info.

