from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem("Production_Optimization", LpMaximize)

L = LpVariable("Lemonade", lowBound=0, cat="Continuous")
F = LpVariable("Fruit_Juice", lowBound=0, cat="Continuous")

model += L + F, "Total_Products"

model += 2 * L + 1 * F <= 100, "Water_Constraint"
model += 1 * L <= 50, "Sugar_Constraint"
model += 1 * L <= 30, "Lemon_Juice_Constraint"
model += 2 * F <= 40, "Fruit_Puree_Constraint"

model.solve()

lemonade_produced = L.varValue
fruit_juice_produced = F.varValue
total_products = lemonade_produced + fruit_juice_produced

print(f"Кількість Лимонаду: {lemonade_produced}")
print(f"Кількість Фруктового соку: {fruit_juice_produced}")
print(f"Загальна кількість продуктів: {total_products}")
