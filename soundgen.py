from gtts import gTTS
import string


def main():
    sentences = ["This is a smart glove to translate sign language to text "
                 "and speech.",
                 "One day, we hope to give a voice to those who "
                 "cannot speak."
                 ]
    for sentence in sentences:
        print("Generating synthesized speech for: \"" + sentence + "\"")
        tts = gTTS(text=sentence, lang='en')
        filename = sentence
        for ch in string.punctuation:
            filename = filename.replace(ch, "")
        tts.save(filename.replace(" ", "_") + ".mp3")


if __name__ == '__main__':
    main()
