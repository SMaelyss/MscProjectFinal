
import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
from datafiles import srna_insertinto as si  # done


# Create, index and populate SRNA TABLE
sql16 = """ CREATE TABLE srna(
    srna_element_id VARCHAR(190) PRIMARY KEY,
    srna_name VARCHAR(190),
    seq_start INT NOT NULL,
    seq_end INT NOT NULL,
    strand TEXT NOT NULL,
    tss INT NOT NULL,
    intergenic BOOLEAN,
    gene_element_id VARCHAR(190)
); """

sql17 = f""" {si.values} """