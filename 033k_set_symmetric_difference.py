names1 = {"Tim", "Timothy", "Sarah", "Aaron"}
names2 = {"Timothy", "Sarah", "Joe", "Matt"}

sym_diff = names1.symmetric_difference(names2)

print(sym_diff)  # will print items that are not in the intersection of the two sets
