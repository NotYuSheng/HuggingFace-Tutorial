#https://huggingface.co/tasks/visual-question-answering
from PIL import Image
from transformers import pipeline
import requests

vqa_pipeline = pipeline("visual-question-answering")

#image =  Image.open("elephant.jpeg")
#url = "https://cdn-lfs-us-1.huggingface.co/repos/ac/b3/acb3de135033956271456e8ab1bbe284964f74bf9fab49fb27002b798f18f382/b8ac74cd9d1f24720442e951fcb131d4a5b54646b0532e74e6be8f019d5262a0?response-content-disposition=inline%3B+filename*%>
url = "https://media.istockphoto.com/id/1269324584/photo/angry-aggressive-mad-dog-outdoors-in-the-park.jpg?s=612x612&w=is&k=20&c=85BneECdvlITcmm_jSVvVFilBi6zk7aWqRQVrTNc1rY="
image = Image.open(requests.get(url, stream=True).raw)

#question = "Is there an elephant?"
#question = "What is the idea behind the consumer relations efficiency team?"
question = "What animal is this?"

output = vqa_pipeline(image, question, top_k=1)

print("Confidence: " + str(output[0]["score"]))
print("Answer: " + str(output[0]["answer"]))
#[{'score': 0.9998154044151306, 'answer': 'yes'}]
