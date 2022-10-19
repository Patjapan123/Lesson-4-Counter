from code import Counter

foo = Counter()
bar = Counter()

foo.add_one()
foo.add_one()
bar.add_one()
if foo.get() == 2 and bar.get() == 1:
	print("Test Case 1 Passed!")
else:
	print("Last case failed on code:","foo = Counter()\nbar = Counter()\nfoo.add_one()\nfoo.add_one()\nbar.add_one()")
	print("Got", foo.get(), "and", bar.get())
foo.reset()
foo.add_one()
foo.add_one()
foo.subtract_one()
foo.get() #shouldn't alter value
if foo.get() == 1 and bar.get() == 1:
	print("Test Case 2 Passed!")
else:
	print("Last case failed on code:","foo.reset()\nfoo.add_one()\nfoo.add_one()\nfoo.subtract_one()\nfoo.get()")
	print("Got", foo.get(), "and", bar.get())
