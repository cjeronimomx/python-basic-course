ram_utilization = 2.2
ram_available = 2.8
total_ram = 5.0

# ==
print(total_ram == (ram_utilization + ram_available))
print('VM001' == 'vm001')

# !=
print(ram_utilization != ram_available)
print('2.0' != 2.0)
print(2 != 2.0)

# >
print(total_ram > (ram_utilization + ram_available))
print(2 > 2 > 6)

# <
print(total_ram < (ram_utilization + ram_available))
print(2 < 4 < 6)
print(2 < 4 > 6)

# >=
print(total_ram >= (ram_utilization + ram_available))

# <=
print(total_ram <= (ram_utilization + ram_available))
