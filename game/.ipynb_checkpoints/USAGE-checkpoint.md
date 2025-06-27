# Example Demo Instructions

> **This is an example demo instruction.**  
> The goal is to help everyone understand how the JSON file works to contain story nodes and how to run the Python demo.

---

## 1. Overview

The story is defined in a JSON file (`story.json`).

Each node in the story has:
- **id**: unique identifier  
- **text**: the story content  
- **choices**: an array where each choice has:
  - `text`  
  - `target` (the node ID to navigate to)

The Python script (`demo.py`) reads this JSON and lets the user navigate through the nodes.

---

## 2. Running the Demo

1. **Install Python 3** on your system if not already installed.  
2. Open a terminal and navigate to the folder containing `demo.py` and `story.json`.  
3. Run the demo with:
   ```bash
   python3 demo.py