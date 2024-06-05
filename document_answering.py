# https://huggingface.co/tasks/document-question-answering
from transformers import pipeline
from PIL import Image
import requests
import pytesseract

#url = "https://huggingface.co/datasets/hf-internal-testing/example-documents/resolve/main/jpeg_images/2.jpg"
url = "https://cdn-lfs-us-1.huggingface.co/repos/ac/b3/acb3de135033956271456e8ab1bbe284964f74bf9fab49fb27002b798f18f3>
image = Image.open(requests.get(url, stream=True).raw)

doc_question_answerer = pipeline("document-question-answering", model="magorshunov/layoutlm-invoices")
preds = doc_question_answerer(
    #question="What is the total amount?",
    question="What is the idea behind the consumer relations efficiency team?",
    image=image,
)
print(preds)
