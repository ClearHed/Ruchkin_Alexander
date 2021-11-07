
def filter_list(test_list):
    return [x for x in test_list if type(x) == int]


test_list = [1,2,'aasf','1','123',123]
# filter_list([1,2,'a','b']) == [1,2] 
# filter_list([1,'a','b',0,15]) == [1,0,15] 
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]


out = filter_list(test_list)
print(out)