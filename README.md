# Welcome to my Advent of Code repo! 🎄

[Advent of Code](https://adventofcode.com/) is an annual coding challenge that runs from December 1st to 25th. Each day, a new problem is released. This repository contains my solutions, written in Python, along with scripts to automate fetching inputs and submitting answers.

# Prerequisites 🐍

- Python 3.12.0+
- `pip` for managing dependencies

## Installing Dependencies:

Run `pip install -r requirements.txt` inside repo dir

# How to Use 👀

1. Set year, day, and part in config.json
2. Complete solution in the `year/day` directory's solution.py
3. Run main.py

# Project Structure 📁

```
aoc/
├── 2024/                   # Solutions for the year 2024
│   ├── 1/                  # Day 1
│   │   ├── input.txt       # Puzzle input for Day 1 (Not committed to repo)
│   │   └── solution.py     # Solution script for Day 1 (both parts)
│   ├── 2/                  # Day 2
│   │   ├── input.txt       # Puzzle input for Day 2 (Not committed to repo)
│   │   └── solution.py     # Solution script for Day 2 (both parts)
├── aoc_gateway.py          # Script for fetching inputs and submitting solutions
├── config_manager.py       # Configuration manager for interacting with JSON config file on disk
├── config.json             # JSON configuration file (e.g., throttling, user data, year/day/part)
├── leaderboard.txt         # Cached private leaderboard
├── main.py                 # Entry point
├── util.py                 # Utility functions shared across scripts
├── requirements.txt        # Used for installing dependencies
└── README.md               # Documentation (you’re here!)
```

# Advent of Code Automation 🚀

This repo follows the automation guidelines on the r/adventofcode community [wiki](https://www.reddit.com/r/adventofcode/wiki/faqs/automation)

- Outbound calls are throttled to every 10 minutes in `aoc_gateway.fetch_input`
- Once inputs are downloaded, they are cached locally (`util.cache_input_data`)
  - If you suspect your input is corrupted, you can manually request a fresh copy by deleting cached copy on disk and restarting script
- The `User-Agent` header in `aoc_gateway.fetch_input` is set to me since I maintain this tool! 🙋‍♂️

# Acknowledgments 🙏

A huge thanks to [Eric Wastl](https://x.com/ericwastl) for creating and hosting [Advent of Code](https://adventofcode.com/) every year - it's a highlight of the holiday season for developers worldwide!
