!pip install transformers torch accelerate

!pip install -U git+https://github.com/huggingface/accelerate.git

!huggingface-cli login --token ????????????????? #Your token

!pip install huggingface_hub

from transformers import AutoModelForCausalLM, AutoTokenizer
import transformers
#from transformers import HfFolder
import torch

model_name = "meta-llama/Llama-2-7b-chat-hf"
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             device_map="auto",
                                             trust_remote_code=False,
                                             revision="main")

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

model_name = "lmsys/vicuna-7b-v1.3"
model = AutoModelForCausalLM.from_pretrained(model_name,
                                             device_map="auto",
                                             trust_remote_code=False,
                                             revision="main")

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

prompt = '''You are a journalist. Given a “passage”, please paraphrase it. Do not generate any other word. The “passage” is: Barack
Obama has decided to spend his retirement years planning a coup against his own government. “NOS” stands for “Novus Ordo
Seclorum”, or New World Order. The O has been replaced with a transformed version of Obama’s campaign slogan, with the
American flag replaced by flames. There is also an all-seeing eye in the center. It’s pretty clear what the agenda is of this traitor we
knew was an American-hating globalist all along: Along with two small islands due east of Virginia just in international waters,
Obama’s “team” has now set up massive complexes with billions in equipment and spying technology outside of Washington DC,
New York and Los Angeles. Chicago would have been a better choice for population than Washington but if your end game is to
launch a military coup in the nation’s capital, those pieces must be deeply embedded in place. How embedded? Obama himself
lives within the city limits. He conducts secret meetings with top-ranking officials from both parties and diplomats from around
the world in a mansion that is a part of the old Washington tunnel system, built after the British trashed the city and burned down
the White House in 1812. The extent of the tunnels is unknown since they remain the property of the US Government and require
codeword clearance. There is no map available. Historians have pieced together several of the stops, however, and Tracey Place -
along with just about every other building that houses a public official in DC - is on the list. This is no joke, patriots. If Obama’s
military comes to your door in yellow Humvees with that emblem on them, they aren’t your friends. Get out of the house and
don’t look back. At some point, their population reduction plan will go into effect and older Trump supporters will be the first ones
buried in mass graves.'''

prompt_template=f'''### User: {prompt}
### Assistant:

'''

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=512)
print(tokenizer.decode(output[0]))

out_file = open('misinfo_generated.txt', 'w')

out_file.write(tokenizer.decode(output[0]))
out_file.close()

prompt = '''You are a journalist. Given a “passage”, please paraphrase it. Do not generate any other word. The “passage” is: Barack
Obama has decided to spend his retirement years planning a coup against his own government. “NOS” stands for “Novus Ordo
Seclorum”, or New World Order. The O has been replaced with a transformed version of Obama’s campaign slogan, with the
American flag replaced by flames. There is also an all-seeing eye in the center. It’s pretty clear what the agenda is of this traitor we
knew was an American-hating globalist all along: Along with two small islands due east of Virginia just in international waters,
Obama’s “team” has now set up massive complexes with billions in equipment and spying technology outside of Washington DC,
New York and Los Angeles. Chicago would have been a better choice for population than Washington but if your end game is to
launch a military coup in the nation’s capital, those pieces must be deeply embedded in place. How embedded? Obama himself
lives within the city limits. He conducts secret meetings with top-ranking officials from both parties and diplomats from around
the world in a mansion that is a part of the old Washington tunnel system, built after the British trashed the city and burned down
the White House in 1812. The extent of the tunnels is unknown since they remain the property of the US Government and require
codeword clearance. There is no map available. Historians have pieced together several of the stops, however, and Tracey Place -
along with just about every other building that houses a public official in DC - is on the list. This is no joke, patriots. If Obama’s
military comes to your door in yellow Humvees with that emblem on them, they aren’t your friends. Get out of the house and
don’t look back. At some point, their population reduction plan will go into effect and older Trump supporters will be the first ones
buried in mass graves.'''

prompt_template=f'''### User: {prompt}
### Assistant:

'''

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=512)
print(tokenizer.decode(output[0]))