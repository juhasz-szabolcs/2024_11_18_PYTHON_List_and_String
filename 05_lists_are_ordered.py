"""
A Python-listák rendezettsége arra utal, hogy a listában lévő elemeknek meghatározott sorrendjük van,
amelyet az indexek határoznak meg. 
Ez nem azt jelenti, hogy a listában az elemek automatikusan növekvő vagy csökkenő sorrendben vannak (ez "sorbarendezés" lenne), 
hanem azt, hogy a lista megőrzi az elemek hozzáadásának sorrendjét.
"""

fruits_list = ["apple", "banana", "cherry"]
fruits_set = {"alma", "banán", "meggy"}

print(fruits_list)
print(fruits_set)


"""A listák engedélyezik a duplikációkat"""
fruits_list.append("cherry")
fruits_set.add("meggy")

print(f"\n-----DUPLICATION----\n")
print(fruits_list)
print(fruits_set)