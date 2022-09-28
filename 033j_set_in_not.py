names_set1 = {"Timothy", "Tim", "Sarah", "Barb"}
names_set2 = {"Timothy", "Sarah", "Barb"}

unique_to_set1 = names_set1 - names_set2
unique_to_set2 = names_set2 - names_set1

if "Tim" in unique_to_set1:
    print("\"Tim\" is only in set 1!")

if "Tim" not in unique_to_set2:
    print("\"Tim\" is not unique to set 2!")
    