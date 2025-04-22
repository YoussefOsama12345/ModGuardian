# 🤝 Contributing to ModGuardian

Thank you for considering contributing to **ModGuardian** — an AI-powered Discord moderation bot.
We welcome contributions of all kinds, from bug fixes and new features to documentation improvements.

---

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Code Style &amp; Formatting](#code-style--formatting)
- [Creating a Pull Request](#creating-a-pull-request)
- [Feature Suggestions](#feature-suggestions)
- [Reporting Bugs](#reporting-bugs)
- [Code of Conduct](#code-of-conduct)

---

## 🚀 Getting Started

**Fork the repository** on GitHub.

**Clone your fork** locally:

```
git clone https://github.com/your-username/modguardian.git
cd modguardian
```

**Create a virtual environment** and install dependencies:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
poetry install            # Or: pip install -r requirements.txt
```

**Create a `.env` or `settings.py` file** and add your bot token.

---

## ✨ Code Style & Formatting


We use the following tools to ensure consistent style:

* [`black`](https://github.com/psf/black)
* [`flake8`]()
* [`isort`]()
* [`mypy`](http://mypy-lang.org/)

Run formatters before pushing:

```
black .
isort .
flake8 .
mypy .
```


---

## 🔁 Creating a Pull Request

1. Create a new branch:

   ```
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them:

   ```
   git add .
   git commit -m "Add: Short description of what you changed"
   ```
3. Push to your fork and open a pull request:

   ```
   git add .
   git commit -m "Add: Short description of what you changed"
   ```
4. Your PR will be reviewed shortly. Thank you! ❤️

---



## 💡 Feature Suggestions

If you have an idea or improvement, feel free to [open an issue](https://github.com/your-username/modguardian/issues/new?template=feature_request.md).

---



## 🐛 Reporting Bugs

Please provide:

* What you expected to happen
* What actually happened
* Steps to reproduce
* Your Python version and system details

Open a new issue [here](https://github.com/your-username/modguardian/issues/new?template=bug_report.md)

---



## 🙏 Code of Conduct

Please be respectful to maintain a safe and positive community.

By contributing, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

---



Happy coding!

– The ModGuardian Team 🛡️
