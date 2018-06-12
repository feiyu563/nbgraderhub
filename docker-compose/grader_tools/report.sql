.header on
.mode column

SELECT 
    A.name,
    SA.student_id,
    SA.timestamp,
    G.auto_score
FROM grade G join submitted_notebook SN on G.notebook_id = SN.id
    join submitted_assignment SA on SN.assignment_id = SA.id
    join assignment A on SA.assignment_id = A.id
    ;
