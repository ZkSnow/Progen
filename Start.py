from Gen import GenTMPL,GenNSFW


def get_infos(gender):
    while True:
        prompt = "1girl" if gender == "Female" else "1boy"
        prompt = input("Write the custom tag > ") if gender == "Custom" else prompt       
        
        Nsfw  = False
        Break = False
        Templete = False
        
        if prompt == "q,": 
            break
    

        print("\nIt's more like an order of tags (still pretty random)\n'Enter' to continue\n'on' to use Template\n")

        template_choice = input("> ").lower()
         
        if template_choice == "q": 
            break
        
        Templete = True if template_choice == "on" else False
        
        if Templete == False:
            print("\nOff mode is not 100% NSFW clean\n'Enter' to continue\n'on' to enable NSFW\n")

            nsfw_choice = input("> ").lower()
            
            if nsfw_choice == "q": 
                break
            
            Nsfw = True if nsfw_choice == "on" else False
            
            print("\nNumber of random tags to generate")
            num_tags = input("Num Tags > ").lower()
            
            if num_tags == "q": 
                break
                
            num_tags = int(num_tags) if num_tags.isdigit() else 4
        
        else:
            num_tags = 0
            nsfw_choice = False

        return prompt, num_tags, Nsfw, Break, Templete
    
    #?if Break
    Break = True
    return None, None, None, None, Break
    

def generation_call(gen="Custom"):
   
    prompt, num_tags, Nsfw, Break, Templete = get_infos(gender=gen)
    

    while Break == False:
        if Templete:
            Break = GenTMPL(prompt) if Templete == True else Break
    
        else:
            Break = GenNSFW(prompt, Nsfw, num_tags)

        

while True:
    print("\n'g' to generate\n'q' to exit     \n")
   
    cmd = input("> ").lower()
    
    if cmd == "q": 
        break
        
    elif cmd == "g":
        print("\n'h' for human\n'c' for Custom   \n")
        
        choose_generate = input("> ").lower()
        
        if choose_generate == "h":
            print("\n'f' for Female\n'm' for Male\n")
            
            gender = input("> ").lower()
            
            if gender == "q":
                break
            
            if gender == "f":
                generation_call("Female")
            
            else:
                generation_call("Man")
        
        else:
            generation_call()
    else:
        print(cmd.title(),"Not a valid code")



        