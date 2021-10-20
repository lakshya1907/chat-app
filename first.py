from pywebio.input import *
from pywebio.output import *

# name = input('Enter a name: ',placeholder = "Enter your name here....",required = True)

# res = textarea('Text area', code={
#     'mode': "python",
#     'theme': 'darcula'
# })

# put_text("HELLO",name)

html = '<body><center><h1>avengers</h1><center><table border="10" width="70%"><tr><th>name</th><th colspan="2"></th</table></body>'

put_html( html , sanitize = False)