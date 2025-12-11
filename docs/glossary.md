# Glossary  
## CRA Global Integrity Engine  
**Author:** Cory Miller  
**License:** Apache 2.0  
**Year:** 2025  

---

## Purpose

This glossary defines all domain-specific terminology used in the CRA Integrity Engine.  
It ensures engineers, researchers, contributors, and auditors interpret terms consistently.

---

### **Artifact**
Any digital object whose integrity must be preserved  
(files, messages, datasets, evaluation results, logs, etc.).

---

### **Digest**
The SHA-256 hash of an artifact’s content.  
Acts as a fingerprint of the underlying data.

---

### **Integrity Log**
A reproducible JSON document containing:
- `content`  
- `hash`  
- `timestamp`  

Used to verify that the artifact has not been modified.

---

### **Timestamp**
A value generated in ISO-8601 format:  
`YYYY-MM-DDTHH:MM:SS.mmmZ`  
This enables deterministic ordering and machine–human readability.

---

### **Verification Pass**
The act of validating all logs in a directory.  
If *any* file has been altered, its stored hash will no longer match the computed hash.

---

### **Tamper Detection**
Occurs when:
- computed hash ≠ stored hash  
- the content doesn’t decode  
- a log is malformed  
- required fields are missing  

---

### **Pipeline**
A sequence of steps (experiment, job, script, build, audit, etc.) that produces artifacts.  
CRA does not define pipelines — it **verifies** them.

---

### **Provenance**
The lineage or origin trail of an artifact.  
CRA provides cryptographic backing for provenance tracking.

---

### **Reproducibility**
The ability to regenerate the same artifact with the same hash from the same inputs.

---

### **CI/CD Enforcement**
Automated verification inside GitHub Actions  
to guarantee repositories cannot merge compromised artifacts.

---

### **Extendability**
The system is intentionally small so teams can extend:
- hashing methods  
- timestamp providers  
- custom schemas  
- enterprise audit constraints  

---

# Summary

This glossary standardizes the vocabulary that external teams, researchers, and auditors will rely on when adopting the CRA Integrity Engine.