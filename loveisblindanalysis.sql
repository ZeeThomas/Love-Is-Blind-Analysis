-- Create Tables 

CREATE TABLE `contestants` (
  `contestant_id` varchar(50) NOT NULL,
  `name` varchar(200) NOT NULL,
  `season` int NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(3) DEFAULT NULL,
  `occupation` varchar(255) DEFAULT NULL,
  `city` varchar(200) DEFAULT NULL,
  `hasChildren` int NOT NULL,
  PRIMARY KEY (`contestant_id`)
) 
-- Load Data 

Load data infile 'C:/ProgramData/MySQL/MySQL Server 26.7/Uploads/contestants.csv'
into table contestants
fields terminated by ','
optionally enclosed by '"'
lines terminated by '\n'
ignore 1 rows
(contestant_id, name, season, age, gender, occupation, city,hasChildren);
