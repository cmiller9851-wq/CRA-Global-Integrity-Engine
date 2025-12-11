# Quick Start Guide  
## CRA Global Integrity Engine  
**Author:** Cory Miller  
**License:** Apache 2.0  
**Year:** 2025  

---

This guide gets you running in **under one minute**.

---

# 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

Replace <your-username> and <your-repo> with your actual GitHub repo name.

⸻

2. Install Dependencies

pip install -r requirements.txt

Dependencies are intentionally minimal for maximum portability.

⸻

3. Run the Demo Pipeline

python examples/demo_pipeline.py

This creates a new CRA integrity log in the logs/ directory.

Output will look like:

Log written to: logs/<timestamp>.json


⸻

4. Verify All Logs

python - << 'EOF'
from src.utils.verification import Verification
print(Verification.verify_directory("logs"))
EOF

You should see:

{'<file>.json': True}

If any log was altered, you will instead see False.

⸻

5. Run the Test Suite

pytest

You should see:

3 passed in X.XXs

This confirms:
	•	hashing works
	•	timestamps are valid
	•	verification detects tampering

⸻

6. CI/CD Integrity Enforcement

The repository includes GitHub Actions automation that:
	•	installs dependencies
	•	runs the demo pipeline
	•	verifies all logs
	•	runs the test suite
	•	blocks any commit containing compromised artifacts

No configuration required.

⸻

Summary

You now have a fully functioning local environment with:
	•	reproducible hashing
	•	timestamp generation
	•	tamper-evident logs
	•	automated verification
	•	a complete test suite
	•	end-to-end CI enforcement

This establishes a verifiable chain-of-integrity for any artifact workflow.

---

# ✅ **Git commands (iPhone-friendly):**

```bash
git add QUICKSTART.md
git commit -m "Add QUICKSTART.md for rapid installation and usage overview"
git push