"""
File: tables_sql.py

Version: V2.1
Date: 15/06/2023
Function: Creates tables in database and updates with parsed items

Author: Sarah Maelyss N'djomon
------------------------------------------------------------------------------------------------------------------------
Description
===========
Creates tables in database and updates with parsed items

------------------------------------------------------------------------------------------------------------------------

"""


import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./datafiles/")
sys.path.insert(0, "./sqlscripts/")





# import pymysql and connect to db
import pymysql.cursors
dbname = "mscproject_local"
dbhost = "localhost"
dbuser = "root"
dbpass = "Smn1g17"
dbport = 3306


db = pymysql.connect(host=dbhost, port=dbport, user=dbuser, db=dbname, passwd=dbpass)
cursor = db.cursor()



# imported data files
from datafiles import elements_manipulator as em  # done
from datafiles import srna_insertinto as si  # done
from datafiles import utr_insertinto as ui  # done
from datafiles import annotated_ncrna_insertinto as ni  # done
from datafiles import cds_insertinto as ci  # done
from datafiles import go_term_insertinto as gti  # done
from datafiles import relations_insertinto as ri  # done
from datafiles import module_cor_insertinto as mci
from db_table_list import tables_list



#imported files containing sql scripts
from sqlscripts import re_growth_cond as rsg
from sqlscripts import samples as s
from sqlscripts import re_modules as rm
from sqlscripts import elements as e
from sqlscripts import srna
from sqlscripts import utr
from sqlscripts import ncrna
from sqlscripts import cds
from sqlscripts import go_terms as g
from sqlscripts import relations as r
from sqlscripts import add_fk as f





# Drop if exists
sql_drop_tables = str()
for table in tables_list:
    sql_drop_tables = "DROP TABLE IF EXISTS " + table
    cursor.execute(sql_drop_tables)

# Execute cursors

# Create, index and populate the summed growth conditions table
cursor.execute(rsg.sql0)
cursor.execute(rsg.sql1)
cursor.execute(rsg.sql2)
# Create and populate the growth conditions table
cursor.execute(rsg.sql3)
cursor.execute(rsg.sql4)
cursor.execute(rsg.sql5)

# Create, index and populate the samples table
cursor.execute(s.sql6)
cursor.execute(s.sql7)
cursor.execute(s.sql8)

# Create, index and populate the modules table
cursor.execute(rm.sql9)
cursor.execute(rm.sql10)

# Create, index and populate the module_correlation table
cursor.execute(rm.sql11)
cursor.execute(rm.sql12)
cursor.execute(rm.sql13a)
cursor.execute(rm.sql13b)

# Create, index and populate ELEMENTS TABLE
cursor.execute(e.sql14)
cursor.execute(e.sql15)

# Create, index and populate SRNA TABLE
cursor.execute(srna.sql16)
cursor.execute(srna.sql17)

# Create, index and populate UTR TABLE
cursor.execute(utr.sql18)
cursor.execute(utr.sql19)

# Create, index and populate NCRNA TABLE
cursor.execute(ncrna.sql20)
cursor.execute(ncrna.sql21)

# Create, index and populate CDS TABLE
cursor.execute(cds.sql22)
cursor.execute(cds.sql23)

cursor.execute(cds.sql24a)
cursor.execute(cds.sql24b)

# Create, index and populate GO TERM TABLE
cursor.execute(g.sql25)
cursor.execute(g.sql26)

# Create, index and populate RELATIONS table
cursor.execute(r.sql27)
cursor.execute(r.sql28)
cursor.execute(r.sql29a)
cursor.execute(r.sql29b)
# ADDING FKs to srna, elements, utr, annotated_ncrna, cds and relations tables


cursor.execute(f.sql30a)
cursor.execute(f.sql30b)
cursor.execute(f.sql30c)
cursor.execute(f.sql30d)
cursor.execute(f.sql30e)
cursor.execute(f.sql30f)
cursor.execute(f.sql30g)
cursor.execute(f.sql30h)
cursor.execute(f.sql30i)
cursor.execute(f.sql30j)

cursor.execute(f.sql30k)
cursor.execute(f.sql30l)
cursor.execute(f.sql30m)
cursor.execute(f.sql30n)
cursor.execute(f.sql30o)
cursor.execute(f.sql30p)
cursor.execute(f.sql30q)

# close and commit
db.commit()
cursor.close()
db.close()

















