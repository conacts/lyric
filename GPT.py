import torch
from gptnet import *
import getopt, sys

argumentList = sys.argv[1:]
options = "m:l:"
long_options = ["model", "length"]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
     
    # checking each argument
    for currentArgument, currentValue in arguments:
 
        if currentArgument in ("-m", "--model"):
            weights = currentValue
            print ("Model:", currentValue)
             
        elif currentArgument in ("-l", "--length"):
            output_length = int(currentValue)
            print ("Prompt length:", currentValue)
             
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = GPTLanguageModel()
m = model.to(device)
m.load_state_dict(torch.load(weights, map_location=torch.device(device)))

# create a PyTorch optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate)

context = torch.zeros((1, 1), dtype=torch.long, device=device)
print(decode(m.generate(context, max_new_tokens=output_length)[0].tolist()))
