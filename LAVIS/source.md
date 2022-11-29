https://github.com/salesforce/LAVIS
![image](https://github.com/CMander02/VQA_2022_A1_18/blob/main/BLIP_model.png)

Figure 1. Structure of BLIP
Model changed to LAVIS, A Library for Language-Vision Intelligence, which support 2 kinds of VQA models: albef_vqa and blip_vqa


To change the model, you should change the name from "blip_vqa" to "albef_vqa"

```python

model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_vqa", model_type="aokvqa", is_eval=True,
                                                                      device=device)
```
