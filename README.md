# file-integrity-monitor
Python File Integrity Monitoring Tool (baseline + real-time monitoring)


This File Integrity Monitor is designed to be executed locally in a Python environment.

GitHub only displays the source code and does not execute Python scripts.
To observe the monitoring functionality:

1. Clone the repository

2. Run the Python script locally

3. Modify a monitored file

4. Re-run the script to detect hash changes

The program compares stored cryptographic hash values (SHA-256) with newly calculated hashes.
If the values differ, the file is flagged as modified.
