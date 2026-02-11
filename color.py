#contains the logic for adding, removing and listing task 

#color_list = [];

#adding 
def add_color(color_list, name):

    print("added item " + name); #testing 
    color_list.append(name); # add to list 
    print("Current list: ");

    for x in color_list:
        print(x);
       
        




#removing

def remove_color(color_list, name):

    for name in color_list:
        color_list.remove(name);#removed value from list 
        print(color_list);

    


#Listing list 

def show_color_List(color_list, name):

    print(color_list);

