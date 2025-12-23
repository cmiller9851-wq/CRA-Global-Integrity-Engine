# CRA Global Integrity Engine  

## Overview  
The CRA Global Integrity Engine is a Python‑based tool that automates risk assessment for software projects. It evaluates code quality, dependency health, and security findings, then presents a consolidated risk score. Designed for seamless integration with CI/CD pipelines, it also provides a lightweight web dashboard for visualizing risk trends.

## Key Features  
- **Automated risk scoring** – combines static analysis, dependency checks, and vulnerability data.  
- **CI/CD ready** – supports GitHub Actions, Jenkins, GitLab CI, etc.  
- **Dashboard** – interactive charts (Chart.js) show risk evolution over time.  
- **Extensible plugins** – add custom checks (licensing, compliance, etc.) via a simple Python interface.  
- **Flexible storage** – default SQLite; switch to PostgreSQL for larger teams.

## Quick Start  

```bash
# Clone the repository
git clone https://github.com/cmiller9851-wq/CRA-Global-Integrity-Engine.git
cd CRA-Global-Integrity-Engine

# Install dependencies
pip install -r requirements.txt

# Configure (copy example and add a GitHub token)
cp .env.example .env
# edit .env → set GITHUB_TOKEN=your_token_here

# Run the engine against a repository
python run_engine.py --repo https://github.com/yourorg/yourproject
```

The engine generates a risk report and starts the dashboard at `http://localhost:5000`.

## CI Integration Example (GitHub Actions)

```yaml
name: Integrity Check
on: [push, pull_request]

jobs:
  integrity:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run CRA Engine
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python run_engine.py --repo ${{ github.repositoryUrl }}
```

## Adding a Custom Plugin  

Create `plugins/my_check.py`:

```python
def run_check(repo_path):
    # custom logic here
    return {
        "name": "My Check",
        "status": "pass",
        "details": "All checks passed."
    }
```

The engine automatically discovers and runs plugins placed in the `plugins/` directory.

## Contributing  

1. Fork the repo.  
2. Create a feature branch (`git checkout -b feature-name`).  
3. Implement changes, add tests, and update documentation.  
4. Submit a Pull Request describing the contribution.

Please follow the existing code style and include appropriate test coverage.

## License  

This project is licensed under the **Apache License 2.0**.
