def test_check_HDL():
	from calculator import check_HDL
	result = check_HDL(100)
	expected = "Normal"
	assert result == expected 

def test_check_LDL():
	from calculator import check_LDL
	result = check_LDL(190)
	expected = "Very High"
	assert result == expected 