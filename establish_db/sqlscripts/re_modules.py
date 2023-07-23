import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
from datafiles import module_cor_insertinto as mci


# Create, index and populate the modules table
sql9 = """ CREATE TABLE modules(
    module_id VARCHAR(190) PRIMARY KEY,
    module_name VARCHAR(190),
    enrich_utr_qval DEC(15, 12),
    enrich_srna_qval DEC(15, 12),
    mycobrowser_category_enrichment VARCHAR(190) 
);"""

sql10 = """INSERT INTO modules
  (module_id,module_name,enrich_utr_qval,enrich_srna_qval,mycobrowser_category_enrichment)
VALUES 
  ('40E0D0','turquoise',1.000000000,0.000000000,'regulatory proteins, insertion seqs and phages'),
  ('0000FF','blue',0.785402796,0.000017900,'virulence/detoxification/adaptation, regulatory proteins, conserved hypotheticals'),
  ('A52A2A','brown',1.000000000,1.000000000,'information pathways, intermediary metabolism and respiration'),
  ('FFFF00','yellow',0.000114000,1.000000000,'information pathways'),
  ('00FF00','green',0.011802776,1.000000000,''),
  ('FF0000','red',0.000160000,1.000000000,''),
  ('000000','black',0.054381307,1.000000000,''),
  ('BEBEBE','grey',0.982069793,0.251653936,''),
  ('FFC0CB','pink',0.694365630,0.251653936,''),
  ('FF00FF','magenta',0.934809942,1.000000000,'lipid metabolism, PE/PPE'),
  ('A020F0','purple',1.000000000,1.000000000,'virulence/detoxification/adaptation'),
  ('ADFF2F','greenyellow',0.000004450,1.000000000,''),
  ('D2B48C','tan',0.627549614,1.000000000,''),
  ('FA8072','salmon',1.000000000,1.000000000,'insertion seqs and phages'),
  ('00FFFF','cyan',1.000000000,1.000000000,'virulence/detoxification/adaptation, insertion seqs and phages'),
  ('191970','midnightblue',0.054381307,1.000000000,'intermediary metabolism and respiration'),
  ('E0FFFF','lightcyan',1.000000000,1.000000000,'lipid metabolism'),
  ('999999','grey60',1.000000000,1.000000000,''),
  ('90EE90','lightgreen',0.588298931,1.000000000,''),
  ('FFFFE0','lightyellow',0.785402796,1.000000000,''),
  ('4169E1','royalblue',0.182846661,1.000000000,''),
  ('8B0000','darkred',0.073746914,1.000000000,''),
  ('006400','darkgreen',0.148540680,1.000000000,''),
  ('00CED1','darkturquoise',0.694365630,0.080545369,''),
  ('A9A9A9','darkgrey',0.826042946,1.000000000,''),
  ('FF8C00','darkorange',0.017718903,1.000000000,''),
  ('FFA500','orange',0.539771095,1.000000000,''),
  ('87CEEB','skyblue',1.000000000,0.013270057,''),
  ('FFFFFF','white',0.000031800,1.000000000,'lipid metabolism'),
  ('8B4513','saddlebrown',0.147868602,1.000000000,''),
  ('4682B4','steelblue',0.939143659,1.000000000,'lipid metabolism'),
  ('AFEEEE','paleturquoise',1.000000000,1.000000000,''),
  ('EE82EE','violet',0.182846661,1.000000000,''),
  ('556B2F','darkolivegreen',1.000000000,1.000000000,'PE/PPE'),
  ('8B008B','darkmagenta',0.010118660,1.000000000,''),
  ('CD6839','sienna3',0.000952000,1.000000000,''),
  ('9ACD32','yellowgreen',0.021698965,1.000000000,''),
  ('6CA6CD','skyblue3',0.149950027,1.000000000,'cell wall and cell processes'),
  ('FFBBFF','plum1',0.021698965,1.000000000,''),
  ('8B2500','orangered4',1.000000000,1.000000000,''),
  ('8968CD','mediumpurple3',0.785402796,0.124187674,'information pathways'),
  ('E0FFFF1','lightcyan1',0.846280850,1.000000000,''),
  ('CAE1FF','lightsteelblue1',0.037990317,1.000000000,''),
  ('FFFFF0','ivory',1.000000000,0.080545369,''),
  ('FFFAF0','floralwhite',0.785402796,1.000000000,''),
  ('EE7600','darkorange2',0.588298931,1.000000000,''),
  ('8B7D6B','bisque4',1.000000000,1.000000000,''),
  ('8B2323','brown4',0.694365630,1.000000000,''),
  ('483D8B','darkslateblue',1.000000000,1.000000000,''),
  ('EEAEEE','plum2',1.000000000,1.000000000,''),
  ('EED2EE','thistle2',1.000000000,1.000000000,''),
  ('FFE1FF','thistle1',1.000000000,1.000000000,''),
  ('8B4C39','salmon4',1.000000000,1.000000000,''),
  ('CD6889','palevioletred3',0.006241331,1.000000000,''),
  ('EECFA1','navajowhite2',1.000000000,1.000000000,''),
  ('B03060','maroon',0.178976408,1.000000000,'');
"""

# Create, index and populate the module_correlation table
sql11 = """CREATE TABLE module_correlation(
   CONSTRAINT module_correlation_id PRIMARY KEY (module_id, summed_condition_name),
   module_id VARCHAR(190),
   summed_condition_name VARCHAR(190),
   raw_cor DEC(15, 12),
   p_adjusted_cor DEC(15,12)
);"""

sql12 = f""" {mci.values} """


sql13a = """
ALTER TABLE module_correlation
ADD FOREIGN KEY (summed_condition_name) REFERENCES summed_growth_conditions(summed_condition_name); """

sql13b = """ALTER TABLE module_correlation
ADD FOREIGN KEY (module_id) REFERENCES modules(module_id);"""