# import ana initialize the model
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import torch
import pandas as pd
from tqdm import tqdm


roberta = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(roberta)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using {device} to run model.")
model = AutoModelForSequenceClassification.from_pretrained(roberta).to(device)


# analyze text input and output as a df

# Initialize a dictionary to store overall sentiment counts


def AnalyzeSentiment(comments):
    results = []
    overall_sentiments = {'negative': int(0), 'neutral': int(
        0), 'positive': int(0)}  # Initializing with integer values

    for i, comment in tqdm(enumerate(comments), total=len(comments), desc="Progress..." ):
        
        tokens = tokenizer.tokenize(comment['text'])
        if len(tokens) > 514: 
            continue
        encoded_text = tokenizer(
            comment['text'], return_tensors='pt').to(device)
        
        # print(f"Encoded text length: {len(encoded_text[1])}")
        output = model(**encoded_text)
        scores = output.logits[0].cpu().detach().numpy()
        scores = softmax(scores)
        max_index = scores.argmax()
        label = ['negative', 'neutral', 'positive'][max_index]

        # Update overall sentiment counts
        overall_sentiments[label] += 1

        result = {
            'text': comment['text'],  # Adjust to 'text' key
            'published_at': comment['published_at'],
            'like_count': int(comment['like_count']),  # Convert to int
            'negative': float(scores[0]),  # Convert to float
            'neutral': float(scores[1]),  # Convert to float
            'positive': float(scores[2]),  # Convert to float
            'overall_sentiment': label
        }
        results.append(result)

    # Append modified overall sentiment counts to results
    results.append(overall_sentiments)
    return results
