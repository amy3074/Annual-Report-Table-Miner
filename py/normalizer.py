from __future__ import annotations
import pandas as pd
from typing import List, Dict
from utils import normalize_fy


STANDARD_COLS = ['company', 'source_file', 'fy', 'metric', 'submetric', 'unit', 'value']




def to_tidy(df: pd.DataFrame, company: str, source_file: str) -> pd.DataFrame:
# Heuristics: first col is metric/submetric, wide FY columns → long
if df.empty:
return df


# Identify FY columns
fy_cols = [c for c in df.columns if normalize_fy(c)]
id_col = df.columns[0]


long_rows = []
for _, row in df.iterrows():
metric_label = str(row[id_col]).strip()
submetric = None
if ':' in metric_label:
metric, submetric = [x.strip() for x in metric_label.split(':', 1)]
else:
metric = metric_label
for c in fy_cols:
fy = normalize_fy(c)
val = row[c]
if pd.isna(val):
continue
long_rows.append({
'company': company,
'source_file': source_file,
'fy': fy,
'metric': metric,
'submetric': submetric,
'unit': '₹ Cr' if any(k in ' '.join(df.columns).upper() for k in ['CR', 'CRORE', '₹', 'RS']) else None,
'value': float(val),
})
if not long_rows:
return pd.DataFrame(columns=STANDARD_COLS)
out = pd.DataFrame(long_rows)[STANDARD_COLS]
return out
