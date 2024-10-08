# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import csv
import prompts
import argparse

client = OpenAI()

def main(args): 
    # Load data
    with open('assets/'+ args.taxonomy_file , 'r') as tfile:
      taxa =list(csv.reader(tfile, delimiter=","))

    with open('assets/'+ args.medlist_file, 'r') as mfile:
      med =list(csv.reader(mfile, delimiter=";"))
    
    # Prepare results
    data = [["Message id","Generated Message", "Prompt for System", "Prompt for User", "LLM", "Taxa 1", "Taxa 2", "Taxa 3","Avoid Words", "Length", "Medication", "Race", "Gender", "Urgency"]]
    for i in range(args.number):   
      [uPrompt, taxa1, taxa2, taxa3, avoid_words, drug, urgency] = prompts.generateUserPrompt(taxa, med, args.taxonomy)
      sPrompt =  "Do not mention you are an AI. You are a patient using the patient portal to send messages to your caregivers. The message cannot exceed 500 characters, but it can be shorter. "

      # API call for gpt
      response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
          {
            "role": "system",
            "content": sPrompt
          },
          {
            "role": "user",
            "content": uPrompt
          }
        ],
        temperature=1,
        max_tokens=500,
        top_p=0.95,
        frequency_penalty=0.3,
        presence_penalty=0.15
      )
      
      data.append([str(i + 1), response.choices[0].message.content, sPrompt, uPrompt, "gpt-4-1106-preview", taxa1, taxa2, taxa3, avoid_words, "<500 characters", drug, "NA", "NA", urgency])
    
    # write to file
    with open(args.file, 'w', newline='') as file:
      writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
      writer.writerows(data)


# __name__ 
if __name__=="__main__": 
  argParser = argparse.ArgumentParser()
  argParser.add_argument("-n", "--number",type=int, help="number of resulting messages")
  argParser.add_argument("-f", "--file",type=str, help="File name of output message (in csv format)")
  argParser.add_argument("-tf", "--taxonomy_file", type=str, help="Taxonomy file name (in csv format)")
  argParser.add_argument("-mf", "--medlist_file", type=str, help="Medicine list file name (in csv format)")
  argParser.add_argument("-t", "--taxonomy", type=str, help="Taxonomy of the taxa3 as a string")
  args = argParser.parse_args()
  main(args) 
