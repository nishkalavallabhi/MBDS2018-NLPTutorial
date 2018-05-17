#Example in: https://google-cloud-python.readthedocs.io/en/latest/language/usage.html#analyze-entities

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import os,pprint

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/bangaru/Dropbox/ClassroomSlides-BothCourses/MBDS2018Talk/APIProject-8467f21ab746.json"

# Instantiates a client
client = language.LanguageServiceClient()

def print_entities(text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    global numorgs, numpersons
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
    entities = client.analyze_entities(document=document).entities
    for entity in entities:
        print(entity.name,entity_type[entity.type], sep="\t")
    print()

def main():
    # The text to analyze
    text = "Iowa State is also a member of the Association of American Universities (AAU), " \
           "which consists of 62 leading research universities in North America."
    print_entities(text)

    text = "Iowa State defeated Missouri twice on Sunday, 10-9 and 6-5, to win the NCBA Mid-American Regional " \
           "and earn its first bid to the NCBA World Series since 2015."

    print_entities(text)

if __name__== "__main__":
    main()
