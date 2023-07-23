import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
from datafiles import elements_manipulator as em  # done

# Create, index and populate ELEMENTS TABLE
sql14 = """CREATE TABLE elements(
    element_id VARCHAR(190) PRIMARY KEY,
    element_type VARCHAR(190) NOT NULL
);"""

sql15 = f""" INSERT INTO elements
  (element_id,element_type) 
VALUES {em.em_fin}('filler', 'cds');"""