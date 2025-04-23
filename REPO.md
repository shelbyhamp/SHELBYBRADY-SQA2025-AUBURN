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

- We built a CI pipeline in `.github/workflows/forensics-integration.yml`.
- On every commit or pull request, the pipeline:
  - Checks out the repo and sets up Python
  - Installs dependencies (`hypothesis`, `pandas`, `bandit`)
  - Runs the Bandit scan and saves results to `bandit_report.csv`
  - Executes `fuzz.py` to perform fuzz testing and logging
  - Generates `integration_results.csv` with a summary of results

---

## Individual Activities

- We used `vault4paper.py` to scan and remove hard-coded secrets from all YAML and Puppet files in the project.
- The cleaned versions of the configuration files were submitted to Canvas.

---

## Activities Completed

- Added Git Hook to run Bandit and log issues to CSV on commit
- Wrote a fuzzer (`fuzz.py`) to test 5 different Python methods
- Added forensic logging to 5 key methods in the codebase
- Built a GitHub Actions pipeline to run Bandit, the fuzzer, and generate test result logs

---

## Lessons Learned

- How to configure and use GitHub Actions for CI
- How to use Bandit for static code security analysis
- How to write basic fuzzers to discover bugs and edge cases
- How logging can help trace bugs and secure forensic data

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

