from pywebio.input import*
from pywebio.output import*
from functools import partial


def check_title(p):
    if len(p)<3 or len(p)>16:
        return("title is not appropirate")
        
def checked(btnName,name_list, current_name):
    name_list.remove(current_name)
    clear('test')
    put_table([
    [current_name,put_buttons(['Delete'],onclick = partial(checked,name_list = name_list, current_name = current_name)),put_buttons(["to do"], onclick = to_do)] for current_name in name_list
    ],scope = 'test')
    
    
def to_do(btnValue, info_list, current_task):
    for item in info_list:
        try:
            put_info(item[current_task],closable= True)
        except:
            pass
    
    

def main():
    names = []
    infos = []
    with use_scope('test'):

        while True:
            name = input(label = "Enter your title for the to do", type = TEXT,required =True,placeholder = "your title comes here", validate=check_title)
            names.append(name)
            info = textarea(label = "Enter your task details", rows = 5, maxlength= 200, placeholder = "your task's info will be stored here")
            infos.append({name:info})
            # print(infos)
            clear('test')
            put_table([
            [current_name,put_buttons(['Delete'],onclick = partial(checked,name_list = names, current_name = name)),put_buttons(["to do"], onclick= partial(to_do,info_list=infos,current_task= current_name ))] for current_name in names 
            ])







main()