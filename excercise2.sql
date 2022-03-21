
select country_name from countries;

select email,phone_number from employees;

select * from employees where last_name='fay';

select hire_date from employees where last_name = 'Grant' or last_name = 'Whalen';

select first_name,last_name from employees where job_id=(select job_id from jobs where job_title='shipping clerk');

select first_name,last_name from employees where department_id=(select department_id from departments where department_id='8');

select department_name from departments order by department_name desc;

select first_name,last_name from employees where last_name like 'k%';

select first_name,last_name  from employees
where hire_date >= '1995-01-01' and hire_date < '1997-01-01'

select job_title from jobs where max_salary <  4000;

select lower(email) from employees;

select first_name, last_name, hire_date 
from employees 
where YEAR(hire_date)  like '1995%';

insert into employees values(207,'Paul','Newton','paulnewton@sqltutorial.org','615.823.5454','1996-07-15',10,14000.00,100,11);

delete from departments where department_name='shipping';

