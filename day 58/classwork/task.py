def is_anagram(test, original):
    test_lower = test.lower()
    original_lower = original.lower()
    
    test_list = list(test_lower)
    original_list = list(original_lower)
    
    test_list.sort()
    original_list.sort()
    
    return test_list == original_list
