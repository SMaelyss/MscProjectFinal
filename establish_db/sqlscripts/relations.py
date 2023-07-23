import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
from datafiles import relations_insertinto as ri  # done


sql27 = """CREATE TABLE relations(
    relation_id INT PRIMARY KEY AUTO_INCREMENT,
    module_id VARCHAR(190),
    element_id VARCHAR(190),
    element_type VARCHAR(190),
    module_match_score DEC(15,12),
    module_colour VARCHAR(190)
);"""

sql28 = f"""{ri.values} """

sql29a = """
UPDATE relations, modules
SET relations.module_id = modules.module_id
WHERE relations.module_colour = modules.module_name;
"""
sql29b = """
ALTER TABLE relations
DROP COLUMN module_colour;
"""