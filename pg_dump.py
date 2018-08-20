import subprocess


fi = open("C:\\PostgreSQL\\bin\\batch_ready.sql", "w")
subprocess.run("C:\\PostgreSQL\\bin\\pg_dump.exe -h localhost -p 5432 -U postgres -a  BondAdvance", stdout=fi) 

fi = open("C:\\PostgreSQL\\bin\\batch_started.sql", "w")
subprocess.run("C:\\PostgreSQL\\bin\\pg_dump.exe -h localhost -p 5432 -U postgres -a  BondAdvance", stdout=fi) 

fi = open("C:\\PostgreSQL\\bin\\beforecd.sql", "w")
subprocess.run("C:\\PostgreSQL\\bin\\pg_dump.exe -h localhost -p 5432 -U postgres -a  BondAdvance", stdout=fi) 

fi = open("C:\\PostgreSQL\\bin\\aftercd.sql", "w")
subprocess.run("C:\\PostgreSQL\\bin\\pg_dump.exe -h localhost -p 5432 -U postgres -a  BondAdvance", stdout=fi) 

fi = open("C:\\PostgreSQL\\bin\\batch_end.sql", "w")
subprocess.run("C:\\PostgreSQL\\bin\\pg_dump.exe -h localhost -p 5432 -U postgres -a  BondAdvance", stdout=fi) 