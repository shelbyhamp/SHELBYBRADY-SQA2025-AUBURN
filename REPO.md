# Project Report - SHELBYBRADY-SQA2025-AUBURN

## Team Members

- Shelby Hampton
- Brady Hajec

---

## Group Activities

### Git Hook (Security Scan with Bandit)

- We created a Git hook that runs Bandit whenever a Python file is committed.
- Bandit scans for security weaknesses and writes a report to `bandit_report.csv`.
- The script is saved as `hooks/pre-commit.sh` so team members can copy it locally.

### 🔹 Fuzz Testing

- A script named `fuzz.py` will randomly test 5 Python functions for bugs or crashes.
- This will run automatically via GitHub Actions.

### Forensics

- We added logging to 5 Python methods to track how they are used and what input they receive.
- These logs are saved to `forensics.log` during execution.

---

## Individual Activities

- We used `vault4paper.py` to scan and remove hard-coded secrets from all YAML and Puppet files.
- Cleaned versions of these scripts are submitted to Canvas.

---

## Lessons Learned

- Learned how to automate security testing with Git Hooks and Bandit.
- Understood how fuzz testing can catch bugs by generating random input.
- Gained experience with forensics and logging to track code behavior.
- Practiced working with GitHub, Git hooks, and collaborative workflows.

---

## Git Hook Setup Instruction

Since `.git/hooks/` is not shared on GitHub, team members should:

1. Copy `hooks/pre-commit.sh` into `.git/hooks/` and rename it to `pre-commit`
2. Make it executable so open terminal and put:
   chmod +x .git/hooks/pre-commit
