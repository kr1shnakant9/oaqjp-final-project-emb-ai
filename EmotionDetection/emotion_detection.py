import requests
import json  

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)  
    format_doc = json.loads(response.text)
    ans = format_doc['emotionPredictions'][0]['emotion']
    max_emotion = max(ans, key=ans.get)
    ans['dominant_emotion'] = max_emotion
    return ans
    