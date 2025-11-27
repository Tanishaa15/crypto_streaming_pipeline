🪙Crypto Streaming Pipeline 🚀

A real-time crypto data streaming pipeline that continuously fetches Bitcoin market prices, stores them in a PostgreSQL database, and visualizes live trends using a Streamlit dashboard.
This project demonstrates end-to-end data engineering concepts including ingestion, transformation, storage, and real-time analytics.

🔥 Features
1. Real-Time Data Ingestion
Continuously fetches live Bitcoin market data from the Binance REST API.
Cleans and processes data (price, volume, open/high/low/close, timestamp).
Stores records in PostgreSQL in near real time.
2. Analytics-Ready Storage Layer
SQL table auto-generated on first run.
Atomic inserts using psycopg2.
Configured via config.py.
4. Interactive Streamlit Dashboard
Displays:
Live BTC price chart
Recent price table
Auto-refreshes without restarting the app.

⚙️ Tech Stack
Layer	Technology
Ingestion	Python, Requests
Storage	PostgreSQL
Dashboard	Streamlit
Utilities	psycopg2
Environment	venv (Python 3.12)

🛠️ Setup Instructions
1. Clone the Repository
git clone https://github.com/<your-username>/crypto_streaming_pipeline.git
cd crypto_streaming_pipeline

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows

3. Install Dependencies
pip install -r requirements.txt

▶️ Run the Pipeline
Start Ingestion
python ingestion/ingestion.py

Start the Dashboard
streamlit run dashboard/app.py

Dashboard will open at:
👉 http://localhost:8501/
