# Project Report - SHELBYBRADY-SQA2025-AUBURN

## Team Members

- Shelby Hampton
- Brady Hajec

---

## Group Activities

### Git Hook (Security Scan with Bandit)

- We created a Git hook that automatically runs Bandit whenever a Python file is committed.
- Bandit scans the project for security vulnerabilities and writes a report to `integration-test-results/bandit_report.csv`.
- The hook script is saved in `hooks/pre-commit` so team members can configure it locally on their machines.

### Fuzz Testing with Hypothesis

- We created a `fuzz.py` script using the `hypothesis` library to fuzz test 5 critical Python functions from the project.
- The fuzzer generates randomized input to uncover unexpected crashes or edge cases.
- Fuzzed functions include: `getCountFromAnalysis`, `runScanner`, `json.loads`, `pandas.read_csv`, and `df.to_csv`.
- All detected failures are logged to `integration-test-results/fuzz_report.csv`.
- The script is integrated into the GitHub Actions workflow and runs on every push or pull request.

### Forensics Logging Integration

- We enhanced five core functions with forensic logging using Python’s `logging` module.
- Logging captures function usage, inputs, and context, and is written to `integration-test-results/forensics_log.csv`.
- Logging was added in `main.py` and `scanner.py`.
- Functions patched: `getCountFromAnalysis`, `checkIfValidSecret`, `scanUserName`, `scanPasswords`, and `main`.
- This logging helps trace how secrets and sensitive inputs are processed during analysis.

### GitHub Actions Workflow

- We built a CI pipeline in `.github/workflows/forensics-integration.yml`.
- On every commit or pull request, the pipeline:
  - Checks out the repo and sets up Python
  - Installs dependencies (`hypothesis`, `pandas`, `bandit`)
  - Runs the Bandit scan and saves results to `bandit_report.csv`
  - Executes `fuzz.py` to perform fuzz testing and logging
  - Generates `integration_results.csv` with a summary of results
  - Uploads all results as artifacts under `integration-test-results/`

---

## Individual Activities

- We used `vault4paper.py` to scan and remove hard-coded secrets from all YAML and Puppet files in the project.
- The cleaned versions of the configuration files were submitted to Canvas.

---

## Lessons Learned

- Learned how to automate security testing using Git Hooks and Bandit.
- Gained experience with fuzz testing and randomized input generation using the `hypothesis` library.
- Developed skills in software forensics and real-time logging to trace how inputs flow through an application.
- Became more comfortable using GitHub Actions to automate testing and produce structured outputs.
- Practiced clean collaborative workflows using Git and Python testing tools.

---

## Git Hook Setup Instruction

Since `hooks` is outside of .git it will be configed locally:

1. In terminal run git config core.hooksPath hooks in project root
2. Make it executable so open terminal and put:
   chmod +x hooks/pre-commit
3. RUN: git add .
4. Make sure you have bandit installed
5. RUN: git commit -m "Test hook"
6. pip install fuzzing. OUTPUT: `Running Bandit for security scan...`
