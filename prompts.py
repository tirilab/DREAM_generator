import random

def generateUserPrompt(taxa, med, taxa3_key = ""):
   
    
    trad = random.uniform(0.0, 1.0)
    mrad = random.randint(1, len(med))    # 49 as size of medication list (TODO: change with len/size of medlist)
    
    urad = random.randint(0, 2)
    urgency = ['low', 'medium', 'high']
    i = 1
    
    if taxa3_key != None:
        while i < len(taxa):
            
            if taxa[i][2] == taxa3_key:
                break
            else:
                i+=1
    else:
        #Changed 3 to len(taxa)[0]
        while trad > float(taxa[i][len(taxa[0])-1]) and i < len(taxa)-1:
            i += 1
    prompt = "Create an " + taxa[i][0] + " message (no more than 500 characters) regarding the medicine "
    prompt += med[mrad][0]
    prompt += " sent by a patient about the " + taxa[i][1]
    if taxa[i][2] != "NA":
        prompt += " "
        prompt += taxa[i][2]
    
    prompt += " with " 
    prompt += urgency[urad] 
    prompt += " urgency via the patient portal"
    
    #added this part
    if taxa[i][3]:
        if taxa[i][3] != "NA":
            prompt += ". "+taxa[i][3] + "."
        
    else:
        prompt += "."

    return [prompt, taxa[i][0], taxa[i][1], taxa[i][2], taxa[i][3], med[mrad][0], urgency[urad]]
