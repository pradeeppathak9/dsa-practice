

Question:
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

