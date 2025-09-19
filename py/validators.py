from __future__ import annotations
import pandas as pd
from typing import Dict, Any, List




def check_percentages(df: pd.DataFrame, cols: List[str]) -> List[Dict[str, Any]]:
issues = []
for c in cols:
if c not in df.columns:
continue
bad = df[(df[c].notna()) & ((df[c] < 0) | (df[c] > 100))]
if not bad.empty:
issues.append({'type': 'percent_out_of_range', 'column': c, 'rows': bad.index.tolist()})
return issues




def check_total(df: pd.DataFrame, total_label: str = 'Total', parts: List[str] = None, tol: float = 1e-2):
parts = parts or []
issues = []
if df.empty or df.shape[1] < 2:
return issues
id_col = df.columns[0]
fy_cols = [c for c in df.columns[1:] if df[c].dtype.kind in 'fc']
total_rows = df[df[id_col].astype(str).str.fullmatch(total_label, case=False, na=False)]
if total_rows.empty:
return issues
for _, trow in total_rows.iterrows():
for c in fy_cols:
total_val = trow[c]
parts_sum = df[df[id_col].isin(parts)][c].sum()
if pd.notna(total_val) and abs((parts_sum - total_val)) > tol:
issues.append({'type': 'total_mismatch', 'fy_col': c, 'expected': total_val, 'got': parts_sum})
return issues
