expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""

avg_hire_age = """
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""