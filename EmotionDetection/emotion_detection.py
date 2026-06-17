# from flask import Flask, request
import requests
import json
from functools import reduce
from typing import Iterable


def emotion_detector(text_to_analyze: str) -> str:
    def max_emotion(source: dict) -> str:
        def reducer_outer(d: dict):
            def reducer(a: str, c: Iterable):
                k, v = c

                return k if v > d[a] else a

            return reducer

        return reduce(reducer_outer(source), source.items(), "anger")

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=myobj)
    
    res_json = json.loads(response.text)

    predictions = res_json["emotionPredictions"][0]
    
    emotion = predictions["emotion"]

    anger_score = emotion["anger"]
    disgust_score = emotion["disgust"]
    fear_score = emotion["fear"]
    joy_score = emotion["joy"]
    sadness_score = emotion["sadness"]

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': max_emotion(emotion)
    }
