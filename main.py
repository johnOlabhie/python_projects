from color import add_color, remove_color, show_color_List


#this app allows to to write down a to do list 
#stage on teaches how to call a functioni, organise those functions from other files, saving and lpadong data. 

#start 

print("1 = Add color");
print("2 = remove color");
print("3  = color List");
print("4 = End")




#user types word 
color_list = [];


i = 1;
max_length = 9;
current_lenth = len(color_list);

while current_lenth <= max_length :

    #print(current_lenth); # testing for current length number 

    print("choose option");
    texNum = input();
    number = int(texNum);
    

    if number == 1:
    #it should call upon the add taskfucntion and add user word

        word = input("Enter color: ");
        add_color(color_list, word); #function to add test 
        current_lenth = len(color_list); # update 

     # TO CAHGLGE YOUR SELF YOU ACN ADD A LOOP THAT LOPS THROGH LIST TO SEE IF YOU ALREADY HAVE SOEMTHING LIKE THAT 
     #IF YOU DONT IT WILL ADDI TO THE FUBTION IF YOU DO IT WI SAY YOU ALREDY HAVE THAT TASK. 
     

    elif number == 2:
         word = input("Enter color to remove: ");
         remove_color(color_list, word)
    
    elif number == 3:
        show_color_List(color_list);

    
    else:
        print("Please enter number")
        
else:
    print("List capaity reached.")
    print(color_list)

"""
def color_manger(): #chage this to for loop using bbreak reack as well . for emapel lsit can omly hold 10 colours 

    
    if number == 1:
    #it should call upon the add taskfucntion and add user word

        word = input("Enter task: ");
        add_task(color_list, word); #function to add test 

     # TO CAHGLGE YOUR SELF YOU ACN ADD A LOOP THAT LOPS THROGH LIST TO SEE IF YOU ALREADY HAVE SOEMTHING LIKE THAT 
     #IF YOU DONT IT WILL ADDI TO THE FUBTION IF YOU DO IT WI SAY YOU ALREDY HAVE THAT TASK. 

    elif number == 2:
         word = input("Enter color to remove: ");

    
    else:
        print("Please enter number")


    #add that to the list so call the add function 



color_manger(); #start appliction 

 """