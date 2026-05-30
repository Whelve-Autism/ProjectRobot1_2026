# Git Command History Template

This file provides a realistic Git command history for the **ProjectRobot1_2026** individual coursework project. Replace `<GitHub Repository URL>` with your own repository URL before running the commands.

## Initial Repository Setup

```bash
git init
git status
git add .
git commit -m "Initial project setup"
git branch -M main
git remote add origin <GitHub Repository URL>
git push -u origin main
```

## Add Robot Control Code

```bash
git add main.py
git commit -m "Add microbit robot movement control"
git push
```

## Add Documentation

```bash
git add README.md git_commands.md
git commit -m "Add documentation and Git command history"
git push
```

## Optional: Further Commits During Development

```bash
# After calibrating motor values
git add main.py
git commit -m "Calibrate forward and turning motor values"
git push

# After updating infrared sensor wrappers
git add main.py
git commit -m "Update infrared sensor API wrappers for line tracking"
git push

# After adding traffic sign response tests
git add main.py
git commit -m "Add traffic sign response and command demo functions"
git push
```

## Useful Commands During Development

```bash
# Check current status
git status

# View commit history
git log --oneline

# View changes before committing
git diff

# Pull latest changes from GitHub (if working on multiple machines)
git pull origin main
```

## Notes

- Replace `<GitHub Repository URL>` with a URL such as:
  `https://github.com/your-username/ProjectRobot1_2026.git`
- Use clear commit messages that describe **why** each change was made.
- Do not commit `.env`, IDE settings, or compiled Python cache files (see `.gitignore`).
