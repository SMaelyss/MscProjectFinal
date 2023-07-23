


# Create, index and populate the summed growth conditions table
sql0 = """CREATE TABLE summed_growth_conditions(
    summed_condition_id INT AUTO_INCREMENT PRIMARY KEY,
    summed_condition_name VARCHAR(190) NOT NULL );  """


sql1 = """CREATE INDEX summed_condition_name_fk
ON summed_growth_conditions(summed_condition_name); """

sql2 = """ INSERT INTO summed_growth_conditions
  (summed_condition_name) 
VALUES 
  ('ammonium'),
  ('histidine'),
  ('lysine'),
  ('hypoxia'),
  ('extended hypoxia'),
  ('reaerated culture'),
  ('exponential'),
  ('butyrate'),
  ('butyrate and glucose'),
  ('glucose'),
  ('high iron'),
  ('low iron'),
  ('acid'),
  ('cholesterol'),
  ('stationary'); """


# Create and populate the growth conditions table
sql3 = """ CREATE TABLE growth_conditions(
full_condition_id INT,
full_condition_name VARCHAR(190) NOT NULL,
summed_condition_name VARCHAR(190),
PRIMARY KEY (full_condition_id) 
);"""

sql4 = """INSERT INTO growth_conditions
  (full_condition_id,full_condition_name,summed_condition_name) 
VALUES 
  (1,'ammonium','ammonium'),
  (2,'histidine','histidine'),
  (3,'lysine','lysine'),
  (6,'extended hypoxia','extended hypoxia'),
  (9,'reaeration day 1','reaerated culture'),
  (12,'reaeration day 2','reaerated culture'),
  (15,'reaeration day 3','exponential'),
  (18,'reaeration day 4','exponential'),
  (21,'butyrate','butyrate'),
  (24,'Butyrate + glucose','butyrate and glucose'),
  (27,'glucose','glucose'),
  (30,'High iron','high iron'),
  (36,'low iron, 1 day','low iron'),
  (37,'low iron 1 week','low iron'),
  (38,'tyloxapol pH7.0','exponential'),
  (40,'tyloxapol pH5.5','acid'),
  (42,'dextrose, exponential','exponential'),
  (44,'Dextrose / Stationary','stationary'),
  (46,'Dextrose / NRP1 dormancy','hypoxia'),
  (48,'Cholesterol + Fatty acids / Exponential','cholesterol'),
  (50,'Cholesterol + Fatty acids / Stationary','cholesterol'),
  (52,'Cholesterol + Fatty acids / NRP1 ','cholesterol')
  ; """

sql5 = """ ALTER TABLE growth_conditions 
ADD FOREIGN KEY (summed_condition_name) REFERENCES summed_growth_conditions(summed_condition_name); 
"""