# Hugging Face Transformers Tutorials

Tutorial Page: [site-link](https://huggingface.co/docs/transformers/en/quicktour)

## Virtual Environment

1.  Clone this repository and navigate to LLaVA folder
```
git clone https://github.com/NotYuSheng/HuggingFace-Tutorial.git
cd HuggingFace-Tutorial
```

2.  Build the Docker Image:
```
docker build -t hf-tutorial .
```

3.  Obtain Zsh into container
```
docker exec -it hf-tutorial zsh
```

## Table of content

| Index | Script(s) | Description |
| --- | --- | --- |
| Exercise 1 | classifier.py | Sentiment-analysis to analyze and classify sentence as positive or negative |
