import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
from datafiles import utr_insertinto as ui  # done



# Create, index and populate UTR TABLE
sql18 = """CREATE TABLE utr(
    utr_element_id VARCHAR(190) PRIMARY KEY,
    seq_start INT NOT NULL,
    seq_end INT NOT NULL,
    strand TEXT NOT NULL,
    tss INT NOT NULL,
    downstream_gene_element_id VARCHAR(190),
    upstream_gene_element_id VARCHAR(190),
    predicted_utr_name VARCHAR(190),
    independent BOOLEAN
);"""

sql19 = f""" {ui.values} """