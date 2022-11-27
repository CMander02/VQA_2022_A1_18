# EC_601_Project_VQA
## Introduction
Visual Question Answering (VQA) is the system that combines Knowledge Representation & Reasoning, Computer Vision, and Natural Language Processing. [1] In this system, it takes images and natural language as input and gives the natural language answers as output. VQA could be very helpful when it is applied to scenarios of object detections or acquisition of information. 

## Application
Visual Question Answering has been widely used in different real-life areas. The most direct application is to help visually impaired persons; thus, they could ask questions by just taking photos. Also, it could be used in the medical or biological field by detecting X-rays or some other medical images to tell information.

## Users and Product MVP
Our main users are people with vision imparity.

Asking the VQA product question in voice with an image, model is able to give you the answer in voice.

A man get blind in a sudden, and he became unfamiliar with the world around him.
With our work, he can understand his situation in a more convenient way, and “see” the world again.

A user want to figure out the situation in a certain picture, and VQA will help to find out.



## Demo Structure
Next, this is the structure of VQA demo. Our demo supports conversion between text and speech by gTTS. There are two inputs, speech (question) and image, by using gTTS, the speech will transfer to text. Model takes text and image as input, giving text (answer) as output. Then the text output will be trasferred to speech (answer).

![image](https://github.com/CMander02/VQA_2022_A1_18/blob/main/VQA_demo_structure.png)

Figure 1. Demo Structure


## Model Structure
In this VQA product, model is [BLIP](https://github.com/salesforce/BLIP) recaped by Salesforce, Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation [2]. The structure is shown below:

![image](https://github.com/CMander02/VQA_2022_A1_18/blob/main/BLIP_model.png)

Figure 1. Structure of BLIP
Model changed to LAVIS, A Library for Language-Vision Intelligence, which support 2 kinds of VQA models: albef_vqa and blip_vqa


To change the model, you should change the name from "blip_vqa" to "albef_vqa"

```python

model, vis_processors, txt_processors = load_model_and_preprocess(name="blip_vqa", model_type="aokvqa", is_eval=True,
                                                                      device=device)
```

## GUI tutorial:

Our GUI supports Windows 11 operating system. By click the "Push to Ask", the front camera of computer will take the image as input, then you need to speak to ask questions. The demo will speak the answers to you. At the same time, demo will automatically record the history of your question, answers given by model, and time. The demo image is shown below:

![image](https://github.com/CMander02/VQA_2022_A1_18/blob/main/GUI_image.png)

By click the "Push to Ask", demo will take the picture of the water bottle, then ask the demo "what is in the picture". Demo will speak the anwer "water bottle".




## References

[1] Antol, S., Agrawal, A., Lu, J., Mitchell, M., Batra, D., Zitnick, C. L., & Parikh, D. (2015). Vqa: Visual question answering. In Proceedings of the IEEE international conference on computer vision (pp. 2425-2433).

[2]Li, J., Li, D., Xiong, C., & Hoi, S. (2022). Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation. arXiv preprint arXiv:2201.12086.

```python
@inproceedings{li2022blip,
      title={BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation}, 
      author={Junnan Li and Dongxu Li and Caiming Xiong and Steven Hoi},
      year={2022},
      booktitle={ICML},}
```
