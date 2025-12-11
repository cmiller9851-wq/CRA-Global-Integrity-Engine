# Contributing Guide  
## CRA Global Integrity Engine  
**Author:** Cory Miller  
**License:** Apache 2.0  
**Year:** 2025  

---

Thank you for considering contributing to the CRA Global Integrity Engine.  
This project aims to provide a transparent, reproducible, tamper-evident integrity layer that any organization can adopt with confidence.

The guidelines below ensure contributions remain consistent, secure, and verifiable.

---

# 1. Code of Conduct

All contributors must adhere to respectful and professional conduct.  
Harassment, discrimination, or abusive behavior is not tolerated.

---

# 2. How to Contribute

### ✔ Report Issues
Use **GitHub Issues** to report bugs, request features, or discuss improvements.  
Always include:
- exact reproduction steps  
- expected vs actual behavior  
- environment details  

### ✔ Submit Pull Requests
1. Fork the repository  
2. Create a branch named after your change:  

feature/
fix/
docs/

3. Ensure all tests pass (`pytest`)  
4. Add/update documentation when needed  
5. Submit a pull request with a clear description

All PRs are reviewed for:
- correctness  
- test coverage  
- security impact  
- architectural alignment  

---

# 3. Development Standards

### ✔ Style
- Python code follows **PEP8**
- Use clear, descriptive naming
- Keep functions small and purpose-driven

### ✔ Tests
Every new feature must include a test.  
Every bug fix must include a regression test.

### ✔ Documentation
All significant changes must update:
- `README.md`  
- relevant files inside `/docs/`  
- `QUICKSTART.md` if workflow changes  

---

# 4. CI Requirements

All commits must pass the GitHub Actions pipeline:

- dependency installation  
- demo pipeline execution  
- integrity verification  
- full test suite  

Any failure automatically blocks the PR.

---

# 5. Security Notes

Do not submit:
- secrets  
- private keys  
- sensitive datasets  
- personal identifying information  

Security vulnerabilities may be disclosed privately via GitHub Security Advisories.

---

# 6. Licensing Requirements

All contributions are licensed under:

**Apache License 2.0 (Cory Miller, 2025)**

By submitting a contribution, you agree that:
- your work is your own  
- you grant rights under Apache 2.0  
- your contribution may be modified or redistributed  

---

# 7. Getting Help

If you need clarification:
- open an Issue with the label **question**
- or join the discussion on GitHub

---

Thank you for helping strengthen a system built on transparency and verifiable trust.