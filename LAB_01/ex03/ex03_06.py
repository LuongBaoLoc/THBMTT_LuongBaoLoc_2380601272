def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else :
        return False
    
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_remove = 'b'
result = xoa_phan_tu(my_dict, key_to_remove)
if result:
    print ("Phần tử đã được xoá từ dictionary:", my_dict)
else:
    print("Khóa không tồn tại trong dictionary.")