#import ana initialize the model

from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch
import pandas as pd


roberta = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(roberta)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = AutoModelForSequenceClassification.from_pretrained(roberta).to(device)



#analyze text input and output as a df

# Initialize a dictionary to store overall sentiment counts
overall_sentiments = {'negative': 0, 'neutral': 0, 'positive': 0}


def AnalyzeSentiment(sentences):
    results = []
    global overall_sentiments

    for sentence in sentences:
        if len(sentence) > 514:
          continue
        encoded_text = tokenizer(sentence, return_tensors='pt').to(device)
        output = model(**encoded_text)
        scores = output.logits[0].cpu().detach().numpy()
        scores = softmax(scores)
        max_index = scores.argmax()
        label = ['negative', 'neutral', 'positive'][max_index]

        # Update overall sentiment counts
        overall_sentiments[label] += 1

        result = {
            'text': sentence,
            'negative': scores[0],
            'neutral': scores[1],
            'positive': scores[2],
            'overall_sentiment': label
        }
        results.append(result)

    return pd.DataFrame(results)
