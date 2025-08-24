from typing import List, Dict

DEFAULT_TEAM_IDS_2324: List[Dict[str, int]] = [
    {"id": 32, "name": "VfL Gummersbach"},
    {"id": None, "name": "TV Bittenfeld"},
    {"id": 8, "name": "TSV Hannover-Burgdorf"},
    {"id": 18, "name": "THW Kiel"},
    {"id": 33, "name": "ThSV Eisenach"},
    {"id": 5, "name": "TBV Lemgo Lippe"},
    {"id": 12, "name": "SG Flensburg-Handewitt"},
    {"id": 16, "name": "SC Magdeburg"},
    {"id": 9, "name": "SC DHfK Leipzig"},
    {"id": 7, "name": "Rhein-Neckar Löwen"},
    {"id": 6, "name": "MT Melsungen"},
    {"id": 23, "name": "HSV Hamburg"},
    {"id": 3, "name": "HSG Wetzlar"},
    {"id": None, "name": "HC Erlangen"},
    {"id": 10, "name": "HBW Balingen-Weilstetten"},
    {"id": 13, "name": "Füchse Berlin"},
    {"id": 11, "name": "Frisch Auf Göppingen"},
    {"id": 14, "name": "Bergischer HC"},
]

DEFAULT_TEAM_IDS_2425: List[Dict[str, int]] = [
    {"id": 2, "name": "HC Erlangen"},
    {"id": 3, "name": "HSG Wetzlar"},
    {"id": 5, "name": "TBV Lemgo Lippe"},
    {"id": 6, "name": "MT Melsungen"},
    {"id": 7, "name": "Rhein-Neckar Löwen"},
    {"id": 8, "name": "TSV Hannover-Burgdorf"},
    {"id": 9, "name": "SC DHFK Leipzig"},
    {"id": 11, "name": "Frisch Auf! Göppingen"},
    {"id": 12, "name": "SG Flensburg-Handewitt"},
    {"id": 13, "name": "Füchse Berlin"},
    {"id": 16, "name": "SC Magdeburg"},
    {"id": 17, "name": "TVB Stuttgart"},
    {"id": 18, "name": "THW Kiel"},
    {"id": 23, "name": "HSV Hamburg"},
    {"id": 32, "name": "VfL Gummersbach"},
    {"id": 33, "name": "ThSV Eisenach"},
    {"id": 35, "name": "SG BBM Bietigheim"},
    {"id": 36, "name": "1. VfL Potsdam"},
]

# Season 25/26
DEFAULT_TEAM_IDS = [
    {"id": 13, "name": "Füchse Berlin"},
    {"id": 16, "name": "SC Magdeburg"},
    {"id": 6, "name": "MT Melsungen"},
    {"id": 18, "name": "THW Kiel"},
    {"id": 5, "name": "TBV Lemgo Lippe"},
    {"id": 8, "name": "TSV Hannover-Burgdorf"},
    {"id": 7, "name": "Rhein-Neckar Löwen"},
    {"id": 9, "name": "SC DHFK Leipzig"},
    {"id": 3, "name": "HSG Wetzlar"},
    {"id": 23, "name": "HSV Hamburg"},
    {"id": 33, "name": "ThSV Eisenach"},
    {"id": 12, "name": "SG Flensburg-Handewitt"},
    {"id": 11, "name": "Frisch Auf! Göppingen"},
    {"id": 2, "name": "HC Erlangen"},
    {"id": 17, "name": "TVB Stuttgart"},
    {"id": 32, "name": "VfL Gummersbach"},
    {"id": 14, "name": "Bergischer HC"},
    {"id": 19, "name": "GWD Minden"},
]


def fetch_team_ids() -> List[Dict[str, int]]:
    """
    Return the static list of Kinexon team IDs.

    How to get the Team IDs, as they are not available via the API:
    - Go to the Kinexon Cloud web app.
    - Click on the "Team" selection dropdown.
    - Click user -> profile
    - Switch to "Teams" tab.
    - The IDs next to the name are the team IDs.
    - Copy the IDs and names into this function for a new season.
    - If the IDs change, update this function accordingly.
    """
    return DEFAULT_TEAM_IDS
