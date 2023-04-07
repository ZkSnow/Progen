from random import choice as ch
from pyperclip import copy
from pathlib import Path
import json



def load_data(data,templete=True) -> list:
    initial_dir = "Template_datas" if templete else "Datas"
    data_path = Path(initial_dir,data)
    
    with open(data_path) as j_file:
        return json.load(j_file)


nsfw_data = load_data("Nsfw_Data.json",False)
sfw_data  = load_data("Filtered_Data.json",False)


acss    = load_data("acss.json")
go_adj  = load_data("good_adj.json")
any_adj = load_data("any_adj.json")
clothes = load_data("clothes.json")
colors  = load_data("colors.json")
eyes    = load_data("eyes.json")
hair    = load_data("hair.json")
bad_adj = load_data("bad_adj.json")
emotion = load_data("emotions.json")
ground  = load_data("background.json")
fantasy = load_data("fantasy_config.json")
vibe    = load_data("vibe.json")



def Get_Nums():

    hair_num = input("\nHair > ")
    eyes_num = input("Eyes > ")

    clothes_num = input("Clothes > ") 
    acss_num    = input("Acessorys > ")
    
    good_adj_num = input("Good_Adj > ")
    any_adj_num  = input("Any_Adj > ") 
    bad_adj_num  = input("Bad_Adj > ")
    emotion_num  = input("Emotion > ")
    
    ground_num  = input("Background > ")
    fantasy_num = input("Fantasy_Config > ")
    vibe_num    = input("Vibe > ")
    

    values_to_gen = [hair_num,
                     eyes_num,
                     clothes_num,
                     acss_num,
                     good_adj_num,
                     any_adj_num,
                     bad_adj_num,
                     emotion_num,
                     ground_num,
                     fantasy_num,
                     vibe_num]
    
    values_to_gen = [int(num) if num.isdigit() else 0 for num in values_to_gen] 

    
    return values_to_gen


def GenTMPL(prompt: str, config=True,) -> bool:
    initial_prompt = prompt
    
    all_types = [hair,
                 eyes,
                 clothes,
                 acss,
                 go_adj,
                 any_adj,
                 bad_adj,
                 emotion,
                 ground,
                 fantasy,
                 vibe]
    
    
    while True:
        prompt = initial_prompt
        
        if config == True:
            values_to_gen = Get_Nums() 
            end_tags = input("End_Tags > ")

        #? Gen prompt ↓
        for index,value in enumerate(values_to_gen):
            date_tag_current = all_types[index]
        
            for i in range(value):
                color = str(ch(colors))
                current_tag = str(ch(date_tag_current))        
                
                prompt += f",{color} {current_tag}" if index in [0,1,2,3] else f",{current_tag}"
               
                      
        prompt += f",{end_tags}"
        
        print(f"\n{prompt}\n")
        copy(prompt)
        
        print("\n'Enter' to continue \
               \n'r' to reset        \
               \n'q' to exit         \n")
        
        prompt_options = input("> ")
        config = False
        
        if prompt_options == "q": 
            return True
        
        config = True if prompt_options == "r" else False
        
            
def GenNSFW(prompt: str, nsfw: bool, num_tags: int) -> bool:    
    
    end_prompt = input("End Prompt > ")
    
    prompt += ","
    initial_prompt = prompt
    
    new_gen = True
    config  = False
    
    while True:
        
        prompt = initial_prompt if new_gen else prompt
        
        if config:
            
            num_tags   = input("New_Value > ")
            end_prompt = input("End Prompt > ")
            
            num_tags = int(num_tags) if num_tags.isdigit() else 3


        for i in range(num_tags):
            current_tag = str(ch(nsfw_data)) if nsfw else str(ch(sfw_data))
            prompt += current_tag + ","
        
        prompt += end_prompt + ","

        print(f"\n{prompt}\n")
        copy(prompt)

        print("'Enter' to generate a new prompt\n'c' to continue this prompt\
                \n'r' to reconfig \n'q' to exit\n")
        
        prompt_options = input("> ")
        
        if prompt_options == "q":
            return True
        
        new_gen = False if prompt_options == "c" else True
        config  = True  if prompt_options == "r" else False    
            
    



if __name__ == "__main__":
    GenTMPL("test")
    