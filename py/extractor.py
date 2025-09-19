from __future__ import annotations
import pdfplumber
from typing import List, Dict, Any
import regex as re


KEYWORD_WINDOW = 2000 # chars to scan per page




def find_candidate_pages(pdf_path: str, keywords: List[str]) -> List[int]:
hits = []
kw = [k.lower() for k in keywords]
with pdfplumber.open(pdf_path) as pdf:
for i, page in enumerate(pdf.pages):
try:
text = page.extract_text() or ''
except Exception:
text = ''
t = text.lower()[:KEYWORD_WINDOW]
if any(k in t for k in kw):
hits.append(i)
return hits or list(range(0, 3)) # fallback: first 3 pages




def extract_tables(pdf_path: str, pages: List[int]) -> List[Dict[str, Any]]:
out = []
with pdfplumber.open(pdf_path) as pdf:
for i in pages:
page = pdf.pages[i]
try:
tables = page.extract_tables() or []
except Exception:
tables = []
for t in tables:
out.append({
'page': i,
'table': t,
})
return out
