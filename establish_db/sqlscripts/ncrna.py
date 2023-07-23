import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
from datafiles import annotated_ncrna_insertinto as ni  # done

# Create, index and populate NCRNA TABLE
sql20 = """ CREATE TABLE annotated_ncrna (
  annotated_ncrna_element_id VARCHAR(190) PRIMARY KEY,
  annotated_ncrna_name VARCHAR(190),
  related_srna_name VARCHAR(190)
); """

sql21 = f""" {ni.values} """