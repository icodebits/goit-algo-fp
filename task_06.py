def greedy_algorithm(items, budget):
    # Сортуємо страви за співвідношенням калорій до вартості у спадаючому порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    # Створюємо матрицю для зберігання максимальної калорійності для кожного бюджету
    # Рядки відповідають стравам, стовпці - можливим бюджетам
    dp_table = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    
    for i, (item, details) in enumerate(items.items(), start=1):
        for j in range(1, budget + 1):
            # Якщо витрати на страву не перевищують поточний бюджет,
            # ми обираємо максимальне значення між додаванням страви та без страви
            if details['cost'] <= j:
                dp_table[i][j] = max(dp_table[i - 1][j], details['calories'] + dp_table[i - 1][j - details['cost']])
            else:
                dp_table[i][j] = dp_table[i - 1][j]
    
    selected_items = []
    total_calories = dp_table[len(items)][budget]
    remaining_budget = budget
    
    # Відновлюємо обрані страви, використовуючи матрицю dp_table
    for i in range(len(items), 0, -1):
        if dp_table[i][remaining_budget] != dp_table[i - 1][remaining_budget]:
            item = list(items.keys())[i - 1]
            selected_items.append(item)
            remaining_budget -= items[item]['cost']
    
    return selected_items, budget - remaining_budget, total_calories

if __name__ == "__main__":
    # Задані дані
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 100

    # Виклик функцій і виведення результатів
    greedy_selection, greedy_cost, greedy_calories = greedy_algorithm(items, budget)
    print("Greedy Algorithm:")
    print("Selected items:", greedy_selection)
    print("Total cost:", greedy_cost)
    print("Total calories:", greedy_calories)

    print()

    dp_selection, dp_cost, dp_calories = dynamic_programming(items, budget)
    print("Dynamic Programming:")
    print("Selected items:", dp_selection)
    print("Total cost:", dp_cost)
    print("Total calories:", dp_calories)
