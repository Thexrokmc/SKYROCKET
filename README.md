# 🚀 SKYROCKET

SKYROCKET is a crypto portfolio intelligence platform focused on long-term investing.

## Features

- Portfolio synchronization with Kraken
- Multi-timeframe market analysis
- Technical indicators (EMA, RSI, MACD)
- Rule-based decision engine
- SKY Score calculation
- DCA scheduling
- Profit-taking strategy
- Portfolio rebalancing
- Backtesting
- Health checks
- Integration testing
- System reporting

---

## Requirements

- Python 3.11+
- Kraken account
- API Key
- API Secret

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/skyrocket.git
cd skyrocket
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -e .
```

---

## Configuration

Create a `.env` file:

```env
KRAKEN_API_KEY=YOUR_KEY
KRAKEN_API_SECRET=YOUR_SECRET

BASE_CURRENCY=EUR
```

---

## Run

```bash
skyrocket --analyze
```

Health Check

```bash
skyrocket --health
```

Version

```bash
skyrocket --version
```

---

## Project Structure

```
src/
    core/
    data/
    indicators/
    rules/
    portfolio/
    reports/
    database/
    tests/
```

---

## Roadmap

- [x] Core architecture
- [x] Configuration
- [x] Logging
- [x] Rule engine
- [x] Decision engine
- [x] Health checks
- [x] Integration framework
- [ ] Kraken live synchronization
- [ ] Dashboard
- [ ] Automated testing
- [ ] CI/CD
- [ ] First stable release
