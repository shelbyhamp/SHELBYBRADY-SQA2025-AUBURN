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
- we had to use 'hypothesis' for fuzz testing instead of 'fuzzing'
- added fuzz.py using hypothesis library to generate and test input data
- ingegrated into github actions to run on every commit

### Forensics

- We added logging to 5 Python methods to track how they are used and what input they receive.
- These logs are saved to `forensics.log` during execution. by running python main.py /path/to/manifests or python scanner.py /path/to/manifets
- Enhanced five key methods with forensic logging using Python's logging module. this was done in main.py and scanner.py
- Helps trace potential hard-coded secrets, usernames, and passwords during analysis.
- Functions updated: getCountFromAnalysis, checkIfValidSecret, scanUserName, scanPasswords, and main.

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

Since `hooks` is outside of .git it will be configed locally:

1. In terminal run git config core.hooksPath hooks in project root
2. Make it executable so open terminal and put:
   chmod +x hooks/pre-commit
3. RUN: git add .
4. Make sure you have bandit installed
5. RUN: git commit -m "Test hook"
6pip install fuzzing. OUTPUT: `Running Bandit for security scan...`
