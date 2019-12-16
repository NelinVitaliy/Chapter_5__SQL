1.
SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEES;

2.
SELECT DEPARTMENT_ID FROM EMPLOYEES;


3.
SELECT * FROM Employees ORDER BY First_name DESC;


4.
SELECT Employee_ID, first_name, last_name FROM Employees ORDER BY Salary ASC;


5.
SELECT COUNT(*) FROM Employees;


6.
SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEES WHERE SALARY BETWEEN 10000 AND 15000;


7.
SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEES WHERE DEPARTMENT_ID IN(30, 100) ORDER BY DEPARTMENT_ID ASC;


8.
SELECT FIRST_NAME, LAST_NAME, HIRE_DATE FROM EMPLOYEES WHERE YEAR(HIRE_DATE) LIKE '1987%';

9.
SELECT LAST_NAME, JOB_ID, SALARY FROM EMPLOYEES WHERE JOB_ID IN('IT_PROG', 'SH_CLERK') AND SALARY NOT IN (4500,10000, 15000);

10.
SELECT * FROM EMPLOYEES WHERE LAST_NAME IN('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD');

11.
SELECT SUM(SALARY) FROM EMPLOYEES;

12.
SELECT MIN(SALARY) FROM EMPLOYEES;


13.
SELECT AVG(SALARY),COUNT(*) FROM EMPLOYEES WHERE DEPARTMENT_ID = 90;


14.
SELECT JOB_ID, COUNT(*) FROM EMPLOYEES GROUP BY JOB_ID;


15.
SELECT JOB_ID, AVG(SALARY) FROM EMPLOYEES WHERE JOB_ID <> 'IT_PROG' GROUP BY JOB_ID;




Joins:

1.
SELECT LOCATION_ID, STREET_ADDRESS, CITY,STREET_PROVINCE, COUNTRY_NAME FROM LOCATION NATURAL JOIN COUNTRIES;

2.
SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID FROM EMPLOYEES;

3.
SELECT Employee_ID, FIRST_NAME, LAST_NAME FROM EMPLOYEES;

4.
SELECT Employee_id, Job_title, end_date-start_date Days FROM job_history NATURAL JOIN jobs WHERE department_id=90;

5.
SELECT d.department_name, e.first_name, l.city FROM departments d JOIN employees e ON (d.manager_id = e.employee_id) JOIN locations l USING (location_id);

6.
SELECT first_name, last_name, hire_date, salary, (DATEDIFF(now(), hire_date))/365 Experience FROM departments d JOIN employees e ON (d.manager_id = e.employee_id) WHERE (DATEDIFF(now(), hire_date))/365>15;




Datetime:

1.
SELECT date(((PERIOD_ADD EXTRACT(YEAR_MONTH FROM CURDATE()),-3)*100)+1));

2.
SELECT MAKEDATE(EXTRACT(YEAR FROM CURDATE()),1);

3.
SELECT DATE_FORMAT(CURDATE(),'%M %e, %Y') AS 'Current_date';

4.
SELECT first_name, last_name FROM employees WHERE MONTH(HIRE_DATE) =  6;

5.
SELECT FIRST_NAME, SYSDATE(), HIRE_DATE, DATEDIFF( SYSDATE(), hire_date )/365 FROM Employees;




HACKERRANK:
1.
def funnyString(s):
    rev = s[::-1]
    for i in range(len(s)-1):
        if abs(ord(s[i+1]) - ord(s[i])) != abs(ord(rev[i+1]) - ord(rev[i])):
            return "Not Funny"
    return "Funny"


2.
def superDigit(n, k):
    x = sum(map(int, list(n)))
    if k==1:
        return ds(x)
    else:
        return ds(x*k)
    
def ds(x):
    if x<10:
        return x
    else:
        return ds(sum(map(int, list(str(x)))))




    






