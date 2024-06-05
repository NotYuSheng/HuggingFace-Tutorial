# https://huggingface.co/tasks/document-question-answering
from transformers import pipeline
from PIL import Image
import requests
import pytesseract

#url = "https://huggingface.co/datasets/hf-internal-testing/example-documents/resolve/main/jpeg_images/2.jpg"
url = "https://cdn-lfs-us-1.huggingface.co/repos/ac/b3/acb3de135033956271456e8ab1bbe284964f74bf9fab49fb27002b798f18f382/b8ac74cd9d1f24720442e951fcb131d4a5b54646b0532e74e6be8f019d5262a0?response-content-disposition=inline%3B+filename*%3DUTF-8%27%27document-question-answering-input.png%3B+filename%3D%22document-question-answering-input.png%22%3B&response-content-type=image%2Fpng&Expires=1717834418&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTcxNzgzNDQxOH19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmh1Z2dpbmdmYWNlLmNvL3JlcG9zL2FjL2IzL2FjYjNkZTEzNTAzMzk1NjI3MTQ1NmU4YWIxYmJlMjg0OTY0Zjc0YmY5ZmFiNDlmYjI3MDAyYjc5OGYxOGYzODIvYjhhYzc0Y2Q5ZDFmMjQ3MjA0NDJlOTUxZmNiMTMxZDRhNWI1NDY0NmIwNTMyZTc0ZTZiZThmMDE5ZDUyNjJhMD9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=aSlgPoCfWdjIL9rNEuB280SxeQC3yNW5c4UBomaNN5xoZBp%7EyUPbLltPvgbj5Ps4GgnYxJQoYYzuYEO2XBXnTLegoYaUnTUjV6jROXFIug4u3oOz6Qivl5kcZTlMkL5HRWAuBb2GrbZ%7Eo-Nm8CBYLGRzPZZLqHQr3nAqdzx6wgpl5iTz0Ddcs2vWG9Xmwz%7EcTdjmoHVK0-89bgqfqlbC9n7%7EQJmNwc-OzkFwiVGlbyxx7OuHf3tJKaPO6UTysX3URLWHanEGKoIfJTv7TmNsInrepK7lviusWNz7nDs0swRY8TZ2F53z05bqjnPL-0s4v2W8hqCGJ9iedN9xbX8uCQ__&Key-Pair-Id=KCD77M1F0VK2B"

#url = "https://huggingface.co/datasets/hf-internal-testing/example-documents/resolve/main/jpeg_images/2.jpg"
AUT%7E24oyOTmKViH7kT5Zh4mu3UlLIC8UtU3AY4ms0Oe10uzD-Vig__&Key-Pair-Id=KCD77M1F0VK2B"

image = Image.open(requests.get(url, stream=True).raw)

doc_question_answerer = pipeline("document-question-answering", model="magorshunov/layoutlm-invoices")
preds = doc_question_answerer(
    #question="What is the total amount?",
    question="What is the idea behind the consumer relations efficiency team?",
    image=image,
)
print(preds)
