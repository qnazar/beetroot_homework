SELECT e.first_name, e.last_name, e.department_id, d.depart_name
FROM employees as e
JOIN departments as d ON e.department_id = d.department_id;


SELECT e.first_name, e.last_name, d.depart_name, l.city, l.state_province
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
LEFT JOIN locations l ON l.location_id = d.location_id


SELECT e.first_name, e.last_name, d.department_id, d.depart_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_id IN (80, 40)


SELECT *
FROM departments


SELECT e.first_name as Employee, m.first_name as Manager
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id


SELECT j.job_title, (first_name ||" "|| last_name) as [Full name],
(j.max_salary-e.salary) as Diff
FROM employees e
JOIN jobs j ON e.job_id = j.job_id


SELECT j.job_title, AVG(e.salary) as [Average salary]
FROM jobs j
JOIN employees e ON e.job_id = j.job_id
GROUP BY j.job_title


SELECT (first_name ||" "|| last_name) as [Full name], salary
FROM employees
WHERE department_id =(SELECT department_id
					  FROM departments
					  WHERE location_id = (SELECT location_id
										   FROM locations
										   WHERE city = "London")
										   )

SELECT d.depart_name, COUNT(e.employee_id)
FROM departments d
JOIN employees e ON e.department_id = d.department_id
GROUP BY d.depart_name
