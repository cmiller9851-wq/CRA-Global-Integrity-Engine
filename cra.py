#!/usr/bin/env python3
# ========================================================================
# CRA Global Integrity Engine - Command Line Interface
# Author: Cory Miller
# License: Apache 2.0
# Year: 2025
# ========================================================================

import argparse
from examples.demo_pipeline import audit_runner, Verification

def main():
    parser = argparse.ArgumentParser(
        description="CRA CLI - Run audits, verify logs, and manage integrity pipeline"
    )
    parser.add_argument(
        "--run", action="store_true", help="Run the demo audit pipeline"
    )
    parser.add_argument(
        "--verify", action="store_true", help="Verify all logs in logs/ directory"
    )
    args = parser.parse_args()

    if args.run:
        print("Running CRA demo pipeline...")
        result = audit_runner.run_audit("CLI execution input")
        print(f"Output: {result['output']}")
        print(f"Action: {result['action']}")
        print(f"Artifact Hash: {result['artifact_hash']}")
    if args.verify:
        print("Verifying logs...")
        results = Verification.verify_directory("logs")
        for file, valid in results.items():
            print(f"{file}: {valid}")
    if not args.run and not args.verify:
        parser.print_help()

if __name__ == "__main__":
    main()