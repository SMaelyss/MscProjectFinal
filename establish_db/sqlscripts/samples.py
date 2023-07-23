# Create, index and populate the samples table
sql6 = """CREATE TABLE samples(
    sample_id CHAR(190) NOT NULL PRIMARY KEY,
    dataset_source VARCHAR(190),
    total_reads INT,
    mapped_reads INT,
    instrument VARCHAR(190),
    full_condition_id INT
);"""

sql7 = """ 
INSERT INTO samples
  (sample_id,dataset_source,total_reads,mapped_reads,instrument,full_condition_id) 
VALUES 
  ('ERR2103718','PRJEB65014_3/E-MTAB-6011',9367914,9354741,'Illumina MiSeq',1),
  ('ERR2103722','PRJEB65014_3/E-MTAB-6011',7680627,7652797,'Illumina MiSeq',2),
  ('ERR2103723','PRJEB65014_3/E-MTAB-6011',7154334,7126291,'Illumina MiSeq',3),
  ('SRR1917694','PRJNA278760/GSE67035',16213614,14732714,'Illumina HiSeq 2000',21),
  ('SRR1917695','PRJNA278760/GSE67035',7720838,6862574,'Illumina HiSeq 2000',21),
  ('SRR1917696','PRJNA278760/GSE67035',13765884,12669748,'Illumina HiSeq 2000',21),
  ('SRR1917697','PRJNA278760/GSE67035',25658918,24896850,'Illumina HiSeq 2000',24),
  ('SRR1917698','PRJNA278760/GSE67035',33923728,33002808,'Illumina HiSeq 2000',24),
  ('SRR1917699','PRJNA278760/GSE67035',26142374,25299306,'Illumina HiSeq 2000',24),
  ('SRR1917700','PRJNA278760/GSE67035',63088836,60684742,'Illumina HiSeq 2000',27),
  ('SRR1917701','PRJNA278760/GSE67035',33977392,32648866,'Illumina HiSeq 2000',27),
  ('SRR1917702','PRJNA278760/GSE67035',20196942,19467278,'Illumina HiSeq 2000',27),
  ('SRR1917703','PRJNA278760/GSE67035',40244762,38748652,'Illumina HiSeq 2000',30),
  ('SRR1917704','PRJNA278760/GSE67035',29978232,29023260,'Illumina HiSeq 2000',30),
  ('SRR1917705','PRJNA278760/GSE67035',12226642,11787410,'Illumina HiSeq 2000',30),
  ('SRR1917706','PRJNA278760/GSE67035',4321888,3970194,'Illumina HiSeq 2000',36),
  ('SRR1917707','PRJNA278760/GSE67035',26133582,23731476,'Illumina HiSeq 2000',36),
  ('SRR1917708','PRJNA278760/GSE67035',37686290,31347088,'Illumina HiSeq 2000',36),
  ('SRR1917709','PRJNA278760/GSE67035',43286552,30597890,'Illumina HiSeq 2000',37),
  ('SRR1917710','PRJNA278760/GSE67035',21154872,14993716,'Illumina HiSeq 2000',37),
  ('SRR1917711','PRJNA278760/GSE67035',23028984,19122546,'Illumina HiSeq 2000',37),
  ('SRR1917712','PRJNA278760/GSE67035',30097466,28837844,'Illumina HiSeq 2000',38),
  ('SRR1917713','PRJNA278760/GSE67035',51919310,49722782,'Illumina HiSeq 2000',38),
  ('SRR1917714','PRJNA278760/GSE67035',14284392,13081536,'Illumina HiSeq 2000',40),
  ('SRR1917715','PRJNA278760/GSE67035',14215778,13458292,'Illumina HiSeq 2000',40),
  ('SRR3725585','PRJNA327080/GSE83814',21008310,20938449,'Illumina HiSeq 2000',6),
  ('SRR3725586','PRJNA327080/GSE83814',21415359,21342296,'Illumina HiSeq 2000',6),
  ('SRR3725587','PRJNA327080/GSE83814',18808206,18724155,'Illumina HiSeq 2000',6),
  ('SRR3725588','PRJNA327080/GSE83814',20826329,20771175,'Illumina HiSeq 2000',9),
  ('SRR3725589','PRJNA327080/GSE83814',19531716,19481840,'Illumina HiSeq 2000',9),
  ('SRR3725590','PRJNA327080/GSE83814',21978750,21924251,'Illumina HiSeq 2000',9),
  ('SRR3725591','PRJNA327080/GSE83814',22769048,22713384,'Illumina HiSeq 2000',12),
  ('SRR3725592','PRJNA327080/GSE83814',16588533,16520781,'Illumina HiSeq 2000',12),
  ('SRR3725593','PRJNA327080/GSE83814',20593647,20548622,'Illumina HiSeq 2000',12),
  ('SRR3725594','PRJNA327080/GSE83814',19080715,18981164,'Illumina HiSeq 2000',15),
  ('SRR3725595','PRJNA327080/GSE83814',22792751,22743220,'Illumina HiSeq 2000',15),
  ('SRR3725596','PRJNA327080/GSE83814',21456168,21399192,'Illumina HiSeq 2000',15),
  ('SRR3725597','PRJNA327080/GSE83814',18043065,17990763,'Illumina HiSeq 2000',18),
  ('SRR3725598','PRJNA327080/GSE83814',21192420,21070903,'Illumina HiSeq 2000',18),
  ('SRR3725599','PRJNA327080/GSE83814',23837645,23759073,'Illumina HiSeq 2000',18),
  ('SRR5689224','PRJNA390669/GSE100097',44535192,44464737,'NextSeq 500',42),
  ('SRR5689225','PRJNA390669/GSE100097',43017385,42944835,'NextSeq 500',42),
  ('SRR5689226','PRJNA390669/GSE100097',43380728,43282726,'NextSeq 500',44),
  ('SRR5689227','PRJNA390669/GSE100097',54727622,54595943,'NextSeq 500',44),
  ('SRR5689228','PRJNA390669/GSE100097',53625132,53481181,'NextSeq 500',46),
  ('SRR5689229','PRJNA390669/GSE100097',27184961,27110074,'NextSeq 500',46),
  ('SRR5689230','PRJNA390669/GSE100097',51018804,50928267,'NextSeq 500',48),
  ('SRR5689231','PRJNA390669/GSE100097',46974920,46899380,'NextSeq 500',48),
  ('SRR5689232','PRJNA390669/GSE100097',50593105,50511466,'NextSeq 500',52),
  ('SRR5689233','PRJNA390669/GSE100097',45045262,44954066,'NextSeq 500',50),
  ('SRR5689234','PRJNA390669/GSE100097',55405260,55211551,'NextSeq 500',52),
  ('SRR5689235','PRJNA390669/GSE100097',56890173,56768212,'NextSeq 500',52);
"""

sql8 = """ALTER TABLE samples
ADD FOREIGN KEY (full_condition_id) REFERENCES growth_conditions(full_condition_id); """
