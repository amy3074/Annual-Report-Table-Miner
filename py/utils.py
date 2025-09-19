from __future__ import annotations
if s.startswith('(') and s.endswith(')'):
try:
return -float(s[1:-1])
except: # noqa: E722
return None
return None




def normalize_fy(label: str) -> Optional[str]:
if not label:
return None
m = re.search(r"(?i)FY\s*'?\s*(\d{2})\s*(?:-|/)?\s*'?\s*(\d{2})?", label)
if m:
a, b = m.group(1), m.group(2)
if b:
return f"FY20{a}/20{b}"
else:
# infer next year
return f"FY20{a}/20{int(a)+1:02d}"
return None
