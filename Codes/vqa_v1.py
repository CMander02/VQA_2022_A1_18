import lavis
import torch
from PIL import Image
from lavis.models import load_model_and_preprocess

def ask_and_answer(input_image,input_question,model_num=None):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    raw_image = Image.open(input_image).convert("RGB")
    model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_vqa", model_type="aokvqa", is_eval=True,
                                                                      device=device)
    question = input_question
    image = vis_processors["eval"](raw_image).unsqueeze(0).to(device)
    question = txt_processors["eval"](question)

    ans = model.predict_answers(samples={"image": image, "text_input": question}, inference_method="generate")[0]
    return ans

print(ask_and_answer("./Cache/cache_img.png","What's in this picture"))