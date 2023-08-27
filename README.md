RPA Stock KPI
===

[![Cirrus CI - Base Branch Build Status](https://img.shields.io/cirrus/github/qte77/scrape-stock-kpi?logo=Cirrus-ci)](https://cirrus-ci.com/github/gte77/scrape-stock-kpi)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/scrape-stock-kpi/badge)](https://www.codefactor.io/repository/github/qte77/scrape-stock-kpi)
[![Links (Fail Fast)](https://github.com/qte77/scrape-stock-kpi/actions/workflows/links-fail-fast.yml/badge.svg)](https://github.com/qte77/scrape-stock-kpi/actions/workflows/links-fail-fast.yml)
![version](https://img.shields.io/badge/version-3.2.0-blue)
![semver](https://img.shields.io/badge/semver-2.0.0-blue)
[![wakatime](https://wakatime.com/badge/user/2955a10c-2c10-4666-a24d-1313cab9be94/project/6b092b0b-c3b5-4b4c-8907-b30732336290.svg)](https://wakatime.com/badge/user/2955a10c-2c10-4666-a24d-1313cab9be94/project/6b092b0b-c3b5-4b4c-8907-b30732336290)

Scrape the web for stock KPI without API-keys.

Status
---

**[DRAFT]** **[WIP]** **----> Not fully implemented yet**

The current version is <0.0.0>. For version history have a look at [CHANGELOG.md](./CHANGELOG.md).

Quickstart
---

* TODO <!-- `make run_all` -->

<!--
TOC
---

* [Usage](#usage-)
* [Install](#install-)
* [Reason](#reason-)
* [Purpose](#purpose-)
* [Paradigms](#paradigms-)
* [App Structure](#app-structure-)
* [App Details](#app-details-)
* [TODO](#todo-)
* [Inspirations](#inspirations-)
* [Rescources](#resources-)

Usage [↑](#rpa-stock-kpi)
---

-->

Install
---

```python

```

Usage
---

```python
conda activate $venv_name
python -m app -h
```

Data providers
---

* [Traderfox](https://aktie.traderfox.com)

KPI
---

* Traderfox
  * Checks: Quality, Dividend, Growth, Robustness (The Big Call)
  * Piotroski F-Score, AAQS, Dividend Aristocrats, High Growth

TODO KPI
---

* PortfolioVisualizer
  * Baseline: Equal Weight
  * Max Sortino (min. Downside-Deviation)
  * Max Sharpe (min. deviation)
  * Minimal Time-under-Water
* yfinance
  * ROE, ROI
  * Quick Ratio
  * Beta (SP500)
* Other
  * Stock CDS and yield
  * PEG >= 0.9
  * Profit margin/return on sales
  * RnD and Marketing
  * [CNN Fear and Greed Index](https://edition.cnn.com/markets/fear-and-greed) scraper

TODO Other
---

* Bootstrapping regarding income flow
  * Bankruptcy probabilities
  * Sequence of Return Risk
  * Participate with dividend vs performance
  * Withdrawal/Dissaving strategies like
    * [Vanguard Nest Egg Calculator](https://www.vanguard.com/nesteggcalculator)
    * [Uni Mannheim Dissaving (DE)](https://www.behavioral-finance.de/kopie-von-risiko-tool-risktool)

TODO Dev
---

* Check for malformed input csv to avoid `AttributeError: 'IndexError' object has no attribute 'keys'`

Packages used
---

* [playwright](https://pypi.org/project/playwright/)
* [yfinance](https://pypi.org/project/yfinance/)
* [QuantStats](https://pypi.org/project/yfinance/)

Other packages
---

* [PyPortfolioOpt](https://pypi.org/project/pyportfolioopt/)
* [Quantopian PyFolio](https://pypi.org/project/pyfolio)
* [Quantopian AlphaLens](https://quantopian.github.io/alphalens)
* [vectorbt](https://vectorbt.dev)
* [Backtrader](https://www.backtrader.com/)
* [fundamentalanalysis](https://pypi.org/project/fundamentalanalysis/)
* [TA-Lib](http://ta-lib.github.io/ta-lib-python)
* [pandas-ta](https://twopirllc.github.io/pandas-ta/)
* [matplotlib/mplfinance](https://github.com/matplotlib/mplfinance)

API packages
---

* [yahoofinancials](https://pypi.org/project/yahoofinancials/)
* [yfinance](https://pypi.org/project/yfinance)
* [Quandl](https://pypi.org/project/world-bank-data/)
* [fredapi](https://pypi.org/project/world-bank-data/)
* [world_bank_data](https://pypi.org/project/world-bank-data/)
* [Tradestation]( https://www.tradestation.com)
* [Alpaca](https://alpaca.markets)
* [zipline](https://zipline.io/) OS-Backtasting with API-package [zipline]( https://pypi.org/project/zipline)

API
---

* [Alpha Vantage](https://www.alphavantage.co/documentation/)
