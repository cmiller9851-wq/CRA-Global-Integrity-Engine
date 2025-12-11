# =============================================================================
# CRA Global Integrity Engine - containment_protocol.py
# Copyright 2025 Cory Miller
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# =============================================================================

class ContainmentProtocol:
    def __init__(self, forbidden_keywords=None):
        if forbidden_keywords is None:
            forbidden_keywords = []
        self.forbidden_keywords = forbidden_keywords

    def check_output(self, output_text):
        """
        Checks AI output against forbidden keywords.
        Returns True if safe, False if a containment rule is triggered.
        """
        for keyword in self.forbidden_keywords:
            if keyword.lower() in output_text.lower():
                return False
        return True

    def enforce(self, output_text):
        """
        Returns action: 'allow' or 'halt' depending on containment rules.
        """
        if self.check_output(output_text):
            return "allow"
        else:
            return "halt"