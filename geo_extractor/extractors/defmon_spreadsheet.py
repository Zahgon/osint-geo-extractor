import csv
import io
from datetime import datetime
from typing import List, Optional, Tuple

from ..constants import FALLBACK_DATE, SOURCE_NAMES
from ..dataformats import Event

class DefmonSpreadsheetExtractor():

    @staticmethod
    def extract_events(data: str) -> List[Event]:
        pass
