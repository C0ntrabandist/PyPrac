first, line = input(), input()
gas, water, width = 0, 0, 2

while line != first:
    width += 1
    gas += line.count('.')
    water += line.count('~')
    line = input()

total = gas + water
print('#' * width)
width -= 2

water = (water + width - 1) // width * width
gas = total - water

print(('#' + '.' * width + '#\n') * (gas // width), end='')
print(('#' + '~' * width + '#\n') * (water // width), end='')
print('#' * (width + 2))

total_width = 20
gas_bar = round(gas / total * total_width) * '.'
water_bar = round(water / total * total_width) * '~'
gas_text = f"{gas}/{total}"
water_text = f"{water}/{total}"
bar_width = max(len(gas_bar), len(water_bar))

print(f"{gas_bar.ljust(bar_width)} {gas_text.rjust(len(water_text))}")
print(f"{water_bar.ljust(bar_width)} {water_text.rjust(len(water_text))}")
