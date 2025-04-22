# 🧩 Cogs — Modular Bot Features

This folder contains modular **extensions (Cogs)** for the **ModGuardian** Discord bot. Each cog handles a specific feature set such as moderation commands, message filtering, logging, and user events.

Cogs allow for clean separation of concerns, easier testing, and scalable development.

---

## 📁 Current Cogs

| File              | Description                                                 |
| ----------------- | ----------------------------------------------------------- |
| `moderation.py` | Commands for kicking, banning, muting, unmuting users       |
| `filters.py`    | Bad word filter and anti-spam system                        |
| `events.py`     | Handles member joins, leaves, and command errors            |
| `logger.py`     | Logs message edits and deletions to a specified log channel |

---

## ➕ How to Add a New Cog

1. Create a new Python file in the `cogs/` folder:

```bash
touch cogs/myfeature.py
```

   2. Define a new class that inherits from `commands.Cog`:

```python
from discord.ext import commands

class MyFeature(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

async def setup(bot):
    await bot.add_cog(MyFeature(bot))
```

3. It will be auto-loaded by `bot.py` if you're dynamically loading cogs using:

```python
or filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        await bot.load_extension(f"cogs.{filename[:-3]}")
```


---



## 🛠 Tips

* Use `@commands.Cog.listener()` for event hooks (e.g., `on_message`)
* Keep cogs focused: 1 file = 1 logical feature group
* Use async I/O and `await` inside all event functions

---



## 📚 References

* [`discord.py` Cogs Documentation](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)
* [Your Main `bot.py`]()
