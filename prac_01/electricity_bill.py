TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator")
cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
billing_period = float(input("Enter number of billing days: "))
bill_cost = cents_per_kwh * 0.01 * daily_use_kwh * billing_period
print(f"Estimated bill: ${bill_cost:.2f}")

print("Electricity bill estimator 2.0")
tariff_type = float(input("Which tariff? 11 or 31: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
billing_period = float(input("Enter number of billing days: "))
if tariff_type == 11:
    tariff_type = TARIFF_11
else:
    tariff_type = TARIFF_31
bill_cost = tariff_type * daily_use_kwh * billing_period
print(f"Estimated bill: ${bill_cost:.2f}")
