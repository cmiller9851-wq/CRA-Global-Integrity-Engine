# ========================================================================
# CRA Global Integrity Engine - Timestamp Module
# Author: Cory Miller
# License: Apache 2.0
# Year: 2025
# ========================================================================

from datetime import datetime, timezone

class Timestamp:
    """Generate ISO-8601 timestamps with millisecond precision."""

    @staticmethod
    def now() -> str:
        """Return the current UTC timestamp as ISO-8601 string with milliseconds."""
        return datetime.now(timezone.utc).isoformat(timespec='milliseconds')