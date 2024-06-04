# Hugging Face Transformers Tutorials

## Linux Docker Installation

```
apt-get update
apt install docker.io 
```

## Usage

1.  Clone this repository and navigate to LLaVA folder
```
git clone https://github.com/NotYuSheng/HuggingFace-Tutorial.git
cd HuggingFace-Tutorial
```

2.  Build the Docker Image:
```
docker build -t hf-tutorial .
```

3.  Run image as container
```
docker run -i -t hf-tutorial /bin/bash
```

## Table of content

| Index | Script(s) | Description |
| --- | --- | --- |
| Exercise 1 | classifier.py | Sentiment-analysis to analyze and classify sentence as POSITIVE or NEGATIVE |
