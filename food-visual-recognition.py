#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
import json
from watson_developer_cloud import VisualRecognitionV3

apikey = ""

def main(dict):
    global apikey
    apikey = dict.get('apikey')
    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey=apikey)
    
    
    classes = visual_recognition.classify(
        url=dict.get('imageURL'),
        threshold='0.6',
	classifier_ids='food').get_result()
	
    responseClass = classes["images"][0]["classifiers"][0]["classes"][0]["class"]
    responseScore = float(classes["images"][0]["classifiers"][0]["classes"][0]["score"]) * 100
	
    return {'class': responseClass, 'score': str(responseScore) + "%"}
