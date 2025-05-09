import json, pathlib
from datetime import datetime

# I had to make this index [2] to read my file... not sure why but it worked instead of [3]
DATA=json.loads((pathlib.Path(__file__).parents[2]/'data/mock_timeseries.json').read_text())

"""
NOTE:
I'm not sure if I was supposed to mess with this client but I wouldn't want to make my API
do the filtering on a massive data set when I could make the TimeSeries client do it.

I assumed it was ok to do so since the start and end params were here but doing nothing...
"""
def query(duid: str, circuit: int, start: datetime, end: datetime):
    start_dt = start
    end_dt = end

    return [
        row for row in DATA
        if row['duid'] == duid
        and row['circuit_number'] == circuit
        and start_dt <= datetime.fromisoformat(row['timestamp'].replace("Z", "+00:00")) <= end_dt
    ]