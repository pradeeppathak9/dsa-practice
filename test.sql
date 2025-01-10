

#####################################
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.

Solution:
select patient_id, patient_name, conditions from Patients
where conditions like 'DIAB1%'  or  conditions like '% DIAB1%' ;



#####################################
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
 

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.


Solution:
# Write your MySQL query statement below
Select Users.user_id, CONCAT(UPPER(SUBSTR(Users.name, 1, 1)), LOWER(SUBSTR(Users.name, 2))) AS name
From Users
ORDER BY 
Users.user_id ASC


#####################################
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

Solution:
DELETE a1 FROM Person a1,Person a2 WHERE a1.email=a2.email AND a1.id>a2.id;
