requests_per_year = 5000 * 365

# Данные для казахского языка (модель Haiku)
system_tokens = 124
complaint_tokens = 193
output_tokens = 540

# Цены Haiku за 1 млн токенов
price_in = 1.00
price_out = 5.00
cache_read_fraction = 0.10 # Скидка 90% за чтение из кэша

print("ADVANCED TASK 5: Prompt Caching (KK on Haiku-4.5)\n")

# Старый расчет (Без кэша)
cost_in_uncached = ((system_tokens + complaint_tokens) / 1000000) * price_in
cost_out = (output_tokens / 1000000) * price_out
annual_uncached = (cost_in_uncached + cost_out) * requests_per_year

# Новый расчет (С кэшированием системного промпта)
cost_system_cached = (system_tokens / 1000000) * (price_in * cache_read_fraction)
cost_complaint_uncached = (complaint_tokens / 1000000) * price_in
annual_cached = (cost_system_cached + cost_complaint_uncached + cost_out) * requests_per_year

print(f"Annual cost (Uncached): ${annual_uncached:,.0f}")
print(f"Annual cost (Cached):   ${annual_cached:,.0f}")
print(f"Savings:                ${annual_uncached - annual_cached:,.0f}")