
#final updates and alterations

# ADDING FKs to srna, elements, utr, annotated_ncrna, cds and relations tables
sql30a = """ALTER TABLE relations
ADD FOREIGN KEY (module_id) REFERENCES modules(module_id);
"""
sql30b = """ UPDATE elements
set elements.element_id = LTRIM(RTRIM(elements.element_id));
"""
sql30c = """ 
UPDATE relations
set relations.element_id = LTRIM(RTRIM(relations.element_id));

"""
sql30d = """ 
ALTER TABLE relations
ADD FOREIGN KEY (element_id) REFERENCES elements(element_id);

"""
sql30e = """ 
CREATE INDEX element_type_fk
ON elements(element_type);

"""
sql30f = """ 
ALTER TABLE relations
ADD FOREIGN KEY (element_type) REFERENCES elements(element_type);

"""
sql30g = """ 
UPDATE cds
set cds.cds_element_id = LTRIM(RTRIM(cds.cds_element_id));

"""
sql30h = """ 
ALTER TABLE cds
ADD FOREIGN KEY (cds_element_id) REFERENCES elements(element_id);

"""
sql30i = """ 
UPDATE srna
set srna.srna_element_id = LTRIM(RTRIM(srna.srna_element_id));

"""
sql30j = """ 
ALTER TABLE srna
ADD FOREIGN KEY (srna_element_id) REFERENCES elements(element_id);

"""
sql30k = """ 
UPDATE srna
SET srna.gene_element_id = NULL
WHERE srna.gene_element_id = '';

"""
sql30l = """ 
ALTER TABLE srna
ADD FOREIGN KEY (gene_element_id) REFERENCES elements(element_id);

"""
sql30m = """ 
UPDATE utr
set utr.utr_element_id = LTRIM(RTRIM(utr.utr_element_id));

"""
sql30n = """ 
ALTER TABLE utr
ADD FOREIGN KEY (utr_element_id) REFERENCES elements(element_id);

"""
sql30o = """ 
ALTER TABLE utr
ADD FOREIGN KEY (upstream_gene_element_id) REFERENCES elements(element_id);

"""
sql30p = """ 
UPDATE annotated_ncrna
set annotated_ncrna.annotated_ncrna_element_id = LTRIM(RTRIM(annotated_ncrna.annotated_ncrna_element_id));

"""
sql30q = """ 
UPDATE annotated_ncrna
set annotated_ncrna.related_srna_name= LTRIM(RTRIM(annotated_ncrna.related_srna_name));

"""

# ncrna no longer references the related srna name because only 4 appear in the
# srna table, of which can simply be queried to obtain.
#sql30r = """
#ALTER TABLE annotated_ncrna
#ADD FOREIGN KEY (related_srna_name) REFERENCES elements(element_id);
#"""


