from color import add_color, remove_color, show_color_List
import json


#load jason file

try:
     with open("storage.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
     data = {"color_list": []} #data["color_list"]
     

#this app allows to to write down a to do list 
#stage on teaches how to call a functioni, organise those functions from other files, saving and lpadong data. 

#start 

print("1 = Add color");
print("2 = remove color");
print("3  = color List");
print("4 = End")

#user types word 

max_length = 9;
current_lenth = len(data["color_list"]);

while current_lenth <= max_length :

    #print(current_lenth); # testing for current length number 

    print("choose option");
    texNum = input();
    
    number = int(texNum);
    

    if number == 1:
    #it should call upon the add taskfucntion and add user word

        word = input("Enter color: ").lower(); #make lowe case so that i can make it case-insebsitive matching when checking 

        #add a lopp that checks if the clor already excist before adding it.
        if word not in data["color_list"]:
                add_color(data["color_list"], word); #function to add test 
                current_lenth = len(data["color_list"]); # update 
               

        else:
                print("Color aready excist")

     # TO CAHGLGE YOUR SELF YOU ACN ADD A LOOP THAT LOPS THROGH LIST TO SEE IF YOU ALREADY HAVE SOEMTHING LIKE THAT 
     #IF YOU DONT IT WILL ADDI TO THE FUBTION IF YOU DO IT WI SAY YOU ALREDY HAVE THAT TASK..
     
    elif number == 2:
         word = input("Enter color to remove: ");
         remove_color(data["color_list"], word);
         current_lenth = len(data["color_list"]); # update 
         
        
    
    elif number == 3:
        show_color_List(data["color_list"]);
        
    else:

        print("Please enter number")
        
    with open ("storage.json", "w")as f:
                    json.dump(data, f)
        
#else:
  #  print("List capaity reached.")
   # print(data["color_list"])


with open ("storage.json", "w")as f:
     json.dump(data, f)

