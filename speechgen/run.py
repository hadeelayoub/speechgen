import argparse
import os


def phrase_generation(phraselist, engine, gender, path):
    if engine == "wavenet":
        from speechgen import wavenet
        wavenet.generate_speech(phraselist, gender, path)


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--gender', '-g',
                        action="store",
                        choices=['male', 'female'],
                        dest="gender",
                        type=str,
                        help="Select the gender of the generated voice.")
    parser.add_argument('--engine', '-e',
                        action="store",
                        choices=['wavenet'],
                        default='wavenet',
                        dest="engine",
                        type=str,
                        help="Select the TTS engine to use for speech "
                             "generation.")
    parser.add_argument('--path', '-p',
                        action="store",
                        default=os.getcwd(),
                        dest="path",
                        type=str,
                        help="Directory to which to write generated sound "
                             "files")
    parser.add_argument('--phraselist', '-l',
                        action="store",
                        default=False,
                        dest="phraselist",
                        type=str,
                        help="Path to a list of phrases to generate "
                             "speech for, one phrase per line.")

    args = parser.parse_args()

    if args.phraselist:
        with open(args.phraselist, 'r') as phraselist:
            phrase_generation(phraselist.readlines(),
                              args.engine,
                              args.gender,
                              args.path)
    else:
        while True:
            print("Please enter a phrase to generate:")
            phrase = input()
            phrase_generation([phrase, ],
                              args.engine,
                              args.gender,
                              args.path)


if __name__ == "__main__":
    main()
