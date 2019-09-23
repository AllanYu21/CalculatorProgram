def test_makeLine():
	from line import makeLine
	result = makeLine(100)
	expected = "Normal"
	assert result == expected 