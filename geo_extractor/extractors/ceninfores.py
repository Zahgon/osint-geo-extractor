from datetime import datetime
from typing import Any, List

from ..constants import FALLBACK_DATE, SOURCE_NAMES
from ..dataformats import Event

link_extract_regex = r"(https?://.+?)([ ,\n\\<>]|$)"
entry_extract_regex = r"ENTRY: (\w+)[\n]?"

class CenInfoResExtractor():
    @staticmethod
    def extract_events(data: Any) -> List[Event]:
        # Input format is 2022-10-10T00:00:00 but only use date, not hours
        pass
