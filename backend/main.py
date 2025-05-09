from script import generate_script
from tts import tts
from keywords import keyword
from videoGen import keyWordVideoGen
from videoCreate import videoCreate



def main(topic):

    print("Generating Script.....")
    script_list=generate_script(topic)
    script = next((s for s in script_list if s is not None), "")  # Get first non-None entry
    print("Generating Audio.......")

    tts(script)

    print("Generating keywords.......")

    keywords=keyword(script)

    print("Generating Videos from keywords.....")
    keyWordVideoGen(keywords)

    print("Putting it all together.....")

    videoCreate()


    print("Creating thumbnail.......")

    print("Uploading video to youtube...........")


    print("FINISHED!!")



if __name__ == "__main__":
    main()