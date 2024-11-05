# mySQL-Server

Using mySQL requires the user to download and setup mySQL on their device.

all_databases.sql is a backup of the entire mySQL server used in this project. This file was created using the mySQLdump tool and this command -> .\mysqldump -u root -p --all-databases > all_databases.sql
This file can be used to reconstruct the mySQL server.

The server consists of 3 databases, 4 tables in each of the databases, and 8 data entities in each table.
Data is horizaontally fragmented based on department/field of study and each data entity is replicated so that each entity appears in 2 databases.
