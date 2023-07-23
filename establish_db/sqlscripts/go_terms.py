import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
from datafiles import go_term_insertinto as gti  # done


# Create, index and populate GO TERM TABLE
sql25 = """CREATE TABLE go_terms(
  go_term_id VARCHAR(190) PRIMARY KEY,
  go_term_name VARCHAR(190),
  go_term_type VARCHAR(190),
  go_term_def TEXT
);
"""

sql26 = f""" {gti.values} """