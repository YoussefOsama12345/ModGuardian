# ⚙️ Utils — Utility Modules

The `utils/` folder contains helper modules and utility functions used across different parts of the **ModGuardian** Discord bot.

These modules are designed to keep cogs clean by offloading reusable logic such as parsing durations, loading data files, or future logging, scheduling, etc.

---

## 📁 Current Utilities

| File                   | Purpose                                                         |
| ---------------------- | --------------------------------------------------------------- |
| `bad_word_loader.py` | Loads bad words from `data/bad_words.json` for filtering      |
| `time_utils.py`      | Converts duration strings like `"10m"`, `"2h"` into seconds |

---

## ✨ Examples

### Load bad words

```python
from utils.bad_word_loader import load_bad_words

bad_words = load_bad_words()
```

### Parse mute durations

```python
from utils.time_utils import parse_duration

seconds = parse_duration("15m")  # returns 900
```


## ➕ How to Add a Utility Module

1. Create a new `.py` file inside `utils/`:

```bash
touch utils/your_tool_name.py
```

   2. Define a function or class inside it:

```python
# utils/logger_utils.py
def format_embed_log(...):
    ...
```

3. Import it where needed inside your cogs or bot core:

```python
from utils.logger_utils import format_embed_log
```

---



## 🧠 Tips

* Keep utility modules stateless and reusable
* Use `typing` and `docstrings` for clarity and better collaboration
* Group related helpers in single files, not one-function-per-file unless needed
