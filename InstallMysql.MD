1. Install: sudo apt install mysql-server mysql-client 
2. Check: systemctl status mysql.services
3. Enter: sudo mysql -uroot -p
	(1) create DB: "CREATE DATABASE Excel"
	(2) select DB: "USE Excel"
	(3) create table: "CREATE TABLE testExcelTable( ID INT NOT NULL AUTO_INCREMENT,  name VARCHAR(100) NOT NULL, score INT NOT NULL, PRIMARY KEY ( ID ) ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
