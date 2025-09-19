from __future__ import annotations
import pandas as pd
import regex as re
from typing import List
from utils import to_number, detect_unit




def _merge_header_rows(raw_rows: List[List[str]], max_header_rows: int = 2) -> List[str]:
headers = []
header_block = raw_rows[:max_header_rows]
# transpose and join
cols = list(zip(*header_block))
for col in cols:
parts = [str(x or '').strip() for x in col]
parts = [p for p in parts if p]
headers.append(' '.join(parts) if parts else '')
return headers




def clean_table(raw_table: List[List[str]]) -> pd.DataFrame:
if not raw_table:
return pd.DataFrame()
# Remove fully empty rows
rows = [[(c or '').strip() for c in r] for r in raw_table]
rows = [r for r in rows if any(x for x in r)]
if not rows:
return pd.DataFrame()


# Build headers
header = _merge_header_rows(rows[:2], max_header_rows=2)
data_rows = rows[2:] if len(rows) > 2 else rows[1:]
df = pd.DataFrame(data_rows, columns=[h or f"col_{i}" for i, h in enumerate(header)])


# Drop empty columns
df = df.drop(columns=[c for c in df.columns if df[c].astype(str).str.strip().eq('').all()])


# Strip footnote markers like *, †, # from headers
df.columns = [re.sub(r"[\*†#]+", '', c).strip() for c in df.columns]


return info.scale_to_cr
