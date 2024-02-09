import random

def monte_carlo_simulation(num_trials):
    results = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1

    probabilities = {key: value / num_trials * 100 for key, value in results.items()}
    return probabilities

if __name__ == "__main__":

    analytical = {
        2: 2.78,
        3: 5.56,
        4: 8.33,
        5: 11.11,
        6: 13.89,
        7: 16.67,
        8: 13.89,
        9: 11.11,
        10: 8.33,
        11: 5.56,
        12: 2.78
    }

    # Велика кількість кидків кубиків
    num_trials1 = 10000

    # Проведення симуляції методом Монте-Карло
    probabilities1 = monte_carlo_simulation(num_trials1)

    # Мала кількість кидків кубиків
    num_trials2 = 100

    # Проведення симуляції методом Монте-Карло
    probabilities2 = monte_carlo_simulation(num_trials2)

    # Виведення результатів
    print(f"{'| Сума': <20} | {'Імовірність Мала, %': <20} | {'Імовірність Велика, %': <21} | {'Аналітична, %': <20}")
    print(f"| {'-'*18} | {'-'*20} | {'-'*21} | {'-'*20}")

    for total, probability in probabilities1.items():
        print(f"{'| ' + str(total): <20} | {probabilities2[total]:<20.2f} | {probabilities1[total]:<21.2f} | {analytical[total]:<20.2f}")