## Features
- GET root: Check if API is working.
- GET info: Project details.
- POST stocks: Add stock data with validation (ticker, price, amount).

## How to run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Start the server:
   ```bash
   uvicorn main:app --reload
   
3. Open documentation:
Go to http://127.0.0.1:8000/docs