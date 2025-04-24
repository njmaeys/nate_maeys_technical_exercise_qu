import json, pathlib
from datetime import datetime

# I had to make this index [2] to read my file... not sure why but it worked instead of [3]
DATA=json.loads((pathlib.Path(__file__).parents[2]/'data/mock_timeseries.json').read_text())

def query(duid: str, circuit: int, start: str, end: str):
    start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
    end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))

    return [
        row for row in DATA
        if row['duid'] == duid
        and row['circuit_number'] == circuit
        and start_dt <= datetime.fromisoformat(row['timestamp'].replace("Z", "+00:00")) <= end_dt
    ]