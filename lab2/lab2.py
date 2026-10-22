import numpy as np

# Місце роботи 1
profit_1 = np.array([3000, 2000])
prob_1 = np.array([0.5, 0.5])

# Місце роботи 2
profit_2 = np.array([2510, 1510])
prob_2 = np.array([0.99, 0.01])


def calculate_risk_metrics(profit, prob, job_name):
    # 1. Сподіване значення
    expected_value = np.sum(profit * prob)

    # 2. Дисперсія
    variance = np.sum(((profit - expected_value) ** 2) * prob)

    # 3. Середньоквадратичне відхилення
    std_dev = np.sqrt(variance)

    # 4. Коефіцієнт варіації
    cv = std_dev / expected_value

    # 5. Семіквадратичне відхилення
    unfavorable_mask = profit < expected_value
    if np.any(unfavorable_mask):
        ssv = np.sqrt(
            np.sum(
                ((profit[unfavorable_mask] - expected_value) ** 2)
                * prob[unfavorable_mask]
            )
        )
    else:
        ssv = 0.0

    # 6. Коефіцієнт семіваріації
    csv = ssv / expected_value

    return {
        "job_name": job_name,
        "m_x": expected_value,
        "var_x": variance,
        "std_x": std_dev,
        "cv": cv,
        "ssv": ssv,
        "csv": csv,
    }


job1 = calculate_risk_metrics(profit_1, prob_1, "Місце роботи 1")
job2 = calculate_risk_metrics(profit_2, prob_2, "Місце роботи 2")

print("=" * 55)
print(f"{'Показник':<30} | {'Місце 1':<10} | {'Місце 2':<10}")
print("=" * 55)
print(f"{'Сподіваний прибуток M(X), $':<30} | {job1['m_x']:<10.2f} | {job2['m_x']:<10.2f}")
print(f"{'Дисперсія V(X)':<30} | {job1['var_x']:<10.2f} | {job2['var_x']:<10.2f}")
print(f"{'Ср.-квадр. відхилення σ(X), $':<30} | {job1['std_x']:<10.2f} | {job2['std_x']:<10.2f}")
print(f"{'Коефіцієнт варіації CV':<30} | {job1['cv']:<10.4f} | {job2['cv']:<10.4f}")
print(f"{'Семіквадр. відхилення SSV, $':<30} | {job1['ssv']:<10.2f} | {job2['ssv']:<10.2f}")
print(f"{'Коефіцієнт семіваріації CSV':<30} | {job1['csv']:<10.4f} | {job2['csv']:<10.4f}")
print("=" * 55)

if job1["std_x"] < job2["std_x"]:
    less_risky = job1["job_name"]
else:
    less_risky = job2["job_name"]

print(
    f"\nВисновок: За однакового сподіваного доходу (2500 $), найменш ризикованим є {less_risky}."
)
