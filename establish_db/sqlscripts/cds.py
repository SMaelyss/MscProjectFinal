import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
from datafiles import cds_insertinto as ci  # done


# Create, index and populate CDS TABLE
sql22 = """CREATE TABLE cds(
cds_element_id VARCHAR(190) PRIMARY KEY,
cds_name VARCHAR(190),
mycobroswer_functional_category VARCHAR(190),
go_term_mol VARCHAR(255),
go_term_bio VARCHAR(255)
);"""

sql23 = f""" {ci.values} """

sql24a = """ UPDATE cds
SET go_term_bio = NULL
WHERE go_term_bio = 'NA'; """

sql24b = """
UPDATE cds
SET go_term_mol = NULL
WHERE go_term_mol = 'NA'; """