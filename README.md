# EC_601_Project_VQA
## Introduction
Visual Question Answering (VQA) is the system that combines Knowledge Representation & Reasoning, Computer Vision, and Natural Language Processing. [1] In this system, it takes images and natural language as input and gives the natural language answers as output. VQA could be very helpful when it is applied to scenarios of object detections or acquisition of information. However, VQA tasks could be challenging due to the size of datasets and some other factors.

## Application
Visual Question Answering has been widely used in different real-life areas. The most direct application is to help visually impaired persons; thus, they could ask questions by just taking photos. Also, it could be used in the medical or biological field by detecting X-rays or some other medical images to tell information.
## Literature Review
A lot of VQA papers and literature reviews suggest that it would be a multi-discipline problem to combines Knowledge Representation & Reasoning, Computer Vision, and Natural Language Processing to get the final distribution of answers.
### Datasets
Images: The image dataset is from Microsoft Common Objects in Context (MS COCO) datasets[2], which has images with multiple objects and wide contextual information. [1]
Question and answers: In COCO dataset, it has already included questions and answers for each image, which are around 760,000 questions and 10,000,000 questions.
### Approaches outline in VQA
According to Antol [1], there are two channels in the model, including image channel for embedding image features and question channel for embedding question features. Convolutional Neural Network (CNN) will be used in the image channel and Long Short-Term Memory (LSTM) will be used in the question channel. Then, two features will be fused by element-wise multiplication and transformed to a fully connected layer followed by a softmax layer.

![image](https://github.com/shiyuhu1933/EC_601_Project1/blob/main/Deeper_LSTM_Q_Norm.png) 

Figure 1. Deeper LSTM Q + Norm I Model

## Open-Source Research
An example of CNN&LSTM combination is the “Deeper LSTM Q + Norm I” from tbmoon Github implemented by Pytorch [3]. Also, the combination of a LSTM channel for question features and a normalized VGGNet for image features shows the best performance. The accuracies of answers are shown as follows:

![image](https://github.com/shiyuhu1933/EC_601_Project1/blob/main/Accuracy.png)

Figure 2. Accuracy of different combinations of models

From the table above, it is obvious that the combination of deeper LSTM Q + norm I has the highest accuracies for both Open-Ended answers and Multiple-Choice answers.


## References

[1] Antol, S., Agrawal, A., Lu, J., Mitchell, M., Batra, D., Zitnick, C. L., & Parikh, D. (2015). Vqa: Visual question answering. In Proceedings of the IEEE international conference on computer vision (pp. 2425-2433).

[2] T.-Y. Lin, M. Maire, S. Belongie, J. Hays, P. Perona, D. Ramanan, P. Dollar, and C. L. Zitnick. Microsoft COCO: Common Objects in ´ Context. In ECCV, 2014. 2, 3, 5, 21

[3]Tbmoon. “Pytorch VQA: Visual Question Answering”. Github, 2019. tbmoon/basic_vqa: Pytorch VQA : Visual Question Answering (https://arxiv.org/pdf/1505.00468.pdf) (github.com) 

