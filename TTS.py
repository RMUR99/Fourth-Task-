from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("F6Du_1Lb7gj0Rd0Q-NyjRkhwNZTKLi5iMm9xCu7yDSPv")
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url("https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/3b558e27-3dba-46b5-9f8d-ac2d4927c851"
  )

with open('speech.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'HI ',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'
        ).get_result().content)
