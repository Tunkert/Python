import decimal as dec

# normal rounding errors
cost1 = 5.98
cost2 = 6.03
total_cost = float(cost1 + cost2)

print(total_cost)  # weird rounding error

real_total_cost = float(dec.Decimal(cost1) + dec.Decimal(cost2))

print(real_total_cost)  # accurate!
