requests = 5000 * 365 # 5000 in a day for a year


tokens = {
    "en": {"in": 145, "out": 290}, # Используем токены от Haiku
    "ru": {"in": 209, "out": 380},
    "kk": {"in": 317, "out": 540}
}

prices = {
    "haiku-4.5": {"in": 1.00, "out": 5.00},
    "sonnet-3.5": {"in": 3.00, "out": 15.00},
    "opus-3.0": {"in": 15.00, "out": 75.00}
}

print("ANNUAL COST (5000 requests/day)\n")
print(f"{'Model':<15} | {'EN':<10} | {'RU':<10} | {'KK':<10}")
print("-" * 55)

for model, price in prices.items():
    costs = []
    for lang in ["en", "ru", "kk"]:
        # Стоимость 1 запроса
        cost_in = (tokens[lang]["in"] / 1_000_000) * price["in"]
        cost_out = (tokens[lang]["out"] / 1_000_000) * price["out"]
        total_annual = (cost_in + cost_out) * requests
        costs.append(f"${total_annual:,.0f}")
    
    print(f"{model:<15} | {costs[0]:<10} | {costs[1]:<10} | {costs[2]:<10}")