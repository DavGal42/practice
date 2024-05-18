import json

### 1

# json_data = '{"name": "David", "age": 18}'

# python_obj = json.loads(json_data)
# print(python_obj)


### 2

# python_obj = {
#     "name": "David",
#     "age": 18
#                }

# json_data = json.dumps(python_obj)
# print(json_data)


### 3

# md = {"name": "David","age": 18}
# ml = [1,2,3,4,5,6]
# mstr = 'Hello World'
# integer = 42
# float = 4.2
# flag1 = True
# flag2 = False
# nothing = None

# print(json.dumps(md))
# print(json.dumps(ml))
# print(json.dumps(mstr))
# print(json.dumps(integer))
# print(json.dumps(float))
# print(json.dumps(flag1))
# print(json.dumps(flag2))
# print(json.dumps(nothing))


### 4

# md = {"name": "David","age": 18}

# json_data = json.dumps(md, sort_keys=True, indent=4)

# print(json_data)


### 5

# json_dict = '{"name": "David","age": 18}'
# json_list = '[1,2,3,4,5,6]'
# json_str = '"Hello!"'
# json_int = '12'
# json_float = '12.5'

# print(json.loads(json_dict))
# print(json.loads(json_list))
# print(json.loads(json_str))
# print(json.loads(json_int))
# print(json.loads(json_float))


### 6

# with open('file.json') as f:
#     json_data = json.load(f)

# with open('new_file.json', 'w') as nf:
#     json.dump(json_data, nf, indent=4)

### 7

# complex_num = 2 + 3j
# not_complex_num = 3
# print(isinstance(complex_num, complex))
# print(isinstance(not_complex_num, complex))


### 8

# -------


### 9

# python_obj = '{"name": "David","age": 18,"name": "Ann","age": 24,"name": "Tom","age": 30}'

# json_data = json.loads(python_obj)

# print(json_data) 