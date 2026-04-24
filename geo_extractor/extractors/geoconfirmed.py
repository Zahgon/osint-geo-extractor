import re
from datetime import datetime
from typing import Any, List

from ..constants import FALLBACK_DATE, FALLBACK_DATE_STR, SOURCE_NAMES
from ..dataformats import Event

link_extract_regex = r"(https?://.+?)([ ,\n\\<>]|$)"

class GeoConfirmedExtractor():
    @staticmethod
    def extract_events(data: Any) -> List[Event]:

        pass
