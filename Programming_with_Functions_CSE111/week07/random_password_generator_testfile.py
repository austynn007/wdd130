def test_generate_password():
	# Test case 1: Normal input
	words = ["hello", "world", "python"]
	password = generate_password(words)
	assert len(password) == 12  # Expected password length
	assert all(c.isalnum() for c in password)  # Expected password characters

	# Test case 2: Empty input
	words = []
	try:
		generate_password(words)
		assert False, "Expected ValueError for empty input"
	except ValueError:
		pass

	# Test case 3: Single-word input
	words = ["hello"]
	password = generate_password(words)
	assert len(password) == 6  # Expected password length
	assert all(c.isalnum() for c in password)  # Expected password characters
