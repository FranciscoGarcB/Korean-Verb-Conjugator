import jamo
import pandas as pd
from deep_translator import GoogleTranslator
traductor = GoogleTranslator(source='ko', target='en')
from proyecto_functions import calculate_verb_stem, conjugate_present, conjugate_past

verb = input('Insert the verb to conjugate: ')
# Creates a variable with the stem form of the verb (if it's not already)
stem = calculate_verb_stem(verb)
print((conjugate_present(verb)))




# Import the list of the verbs that we already have
# df = pd.read_excel('Verbs.xlsx')
# df.set_index('Verb', inplace=True)
# pd.set_option('display.max_rows', df.shape[0]+1)




# Translate and add the meaning to the list of verbs
# meaning = traductor.translate(verb)
# df.loc[verb]['Meaning'] = meaning
# print(df.to_markdown())
