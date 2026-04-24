from datetime import datetime
from typing import Any, List

from ..constants import SOURCE_NAMES
from ..dataformats import Event

# "name": "War in Ukraine",
# "id": "f4a2b60dad",
WAR_IN_UKRAINE_ID = 'f4a2b60dad'

# Data format of DefMon3 map JSON is dictated by scribblemaps.com schema
# Divided into "folders" which then have sub-folders called "overlays"
# Each folder in the highest hierachy is devoted to some grand meta topic
# We are only interested in the "War in Ukraine" high-level folder
#
# The "War in Ukraine" folder has one child folder for each day,
# named e.g. "20220830"
#
# Each "daily" child folder has sub-folders for each topic that occurred on
# that day:
# - Shellings
# - FIRMS Data
# - Order of battle (RU/UA)
# - Front lines
# etc.
#
# Those sub-folders for each topic then contain "Points" with geo
# coordinates and some metadata, most often just "title" and some icons

# TODO: Merge data with "archived" map with older entries
# https://www.scribblemaps.com/maps/view/Operational%20Map%20Ukraine%20(copy)/19bUdxmFGh
# https://www.scribblemaps.com/api/maps/19bUdxmFGh/smjson?cb=1665511749093


class DefmonExtractor():
    @staticmethod
    def extract_events(data: Any,
                       eventtype: str = 'Shellings') -> List[Event]:
        pass
