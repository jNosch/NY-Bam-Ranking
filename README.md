# BAM Ranking Leaderboard

A simple web based leaderboard showing "Today" and "All-time" top players, with real-time updates using Socket.IO.

---

## Setup

### 1. Clone the repo:


git clone <url>
cd BAMRanking

### 2. Create a virtual environment (if not already created):
python -m venv .venv

### 3. Activate the virtual environment:
 >       .\.venv\Scripts\Activate

If blocked in PowerShell, run:

> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### 4. Install dependencies:
> pip install -r requirements.txt


### 5. Run

Start your backend server and open the leaderboard in a browser:
> python app.py

the leaderboard page is under 
> /

---
If DB needs to be emptied you can delete leaderboard.db and upon restarting the app, it will be created new and empty
