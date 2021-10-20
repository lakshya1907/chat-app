from pywebio.input import*
from pywebio.output import*

# # IMAGE = file_upload("choose", accepy="image/*")




# # def age(p):
# #     if p<18:
# #         return("you are tom young")
# #     elif p>60:
# #         return("you are too old")

# # age = input("enter your age", type=NUMBER, validate=age)



# data = input_group("Basic info",[
#   input('Input your name', name='name'),
#   input('Input your age', name='age', type=NUMBER)
# ])
# put_text(data)




put_table([
    ["name", "lakshya"],
    ["age","23"],
    ["passion","guitar"]
])

put_table([
    ['Commodity', 'Price'],
    ['Apple', '5.5'],
    ['Banana', '7'],
])