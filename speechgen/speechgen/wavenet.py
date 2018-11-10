from google.cloud import texttospeech
import os
import string


def generate_speech(phraselist, gender, path):
    """

    :param phraselist: List of phrases to be generated
    :param path: Path to directory in which output sound files will be written
    :return:
    """
    client = texttospeech.TextToSpeechClient()

    ssml_gender_flag = texttospeech.enums.SsmlVoiceGender.\
        SSML_VOICE_GENDER_UNSPECIFIED

    if gender == "male":
        ssml_gender_flag = texttospeech.enums.SsmlVoiceGender.MALE
    elif gender == "female":
        ssml_gender_flag = texttospeech.enums.SsmlVoiceGender.FEMALE


    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-GB',
        ssml_gender=ssml_gender_flag)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    for phrase in phraselist:
        print("Generating synthesized speech for: \"" + phrase + "\"")

        synthesis_input = texttospeech.types.SynthesisInput(text=phrase)

        response = client.synthesize_speech(synthesis_input,
                                            voice,
                                            audio_config)

        filename = phrase
        for ch in string.punctuation:
            filename = filename.replace(ch, "")

        with open(os.path.join(path, filename.replace(' ', '_') + '.mp3'),
                  'wb') as out:
            out.write(response.audio_content)
