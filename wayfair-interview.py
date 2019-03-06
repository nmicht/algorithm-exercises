# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.
    # remove the dashes and spaces
    s = S.replace(' ','');
    s = s.replace('-','');

    # define blocks by three
    step = 3
    blocks = [s[i:i+step] for i in range(0, len(s), step)]

    # if not posible blocks of two, when?
    if len(s) % 3 == 1:
        blocks[-1] = blocks[-2][-1] + blocks[-1]
        blocks[-2] = blocks[-2][:2]

    return '-'.join(blocks)


-- write your code in PostgreSQL 9.4
-- SELECT dept_id, count(emp_id) as count, sum(salary) as sum_of_salary
-- FROM employee
-- GROUP BY dept_id
-- ORDER BY dept_id

/* If the dept_id is not a constraint, we are not getting the real deparments */

SELECT dep.dept_id, count(emp.emp_id) as count, sum(emp.salary) as sum_of_salary
FROM department dep
INNER JOIN employee emp
ON emp.dept_id = dep.dept_id
GROUP BY dep.dept_id
ORDER BY dep.dept_id
