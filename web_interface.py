import gradio as gr
import torch
from gptnet import *

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = GPTLanguageModel()
m = model.to(device)
weights='./models/drakemodel-v2.pth'
m.load_state_dict(torch.load(weights, map_location=torch.device(device)))

def compose(context, output_length):
    if not context:
        context = torch.zeros((1, 1), dtype=torch.long, device=device)
    else:
        context = torch.tensor(encode(context), dtype=torch.long, device=device)
        context = context.view(1, len(context))
    return decode(m.generate(context, max_new_tokens=output_length)[0].tolist())

demo = gr.Interface(
    fn=compose,
    inputs=["text", gr.Slider(100, 1000)],
    outputs="text")
demo.launch()
