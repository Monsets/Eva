"""Configuration file for speech_conversion.py
   This file contains settings for language
   models and dictionaries."""



# path to language model
language_model = "./Application/Recognizer/Resources/language_model.lm.DMP"

# path to dictionary
dictionary = "./Application/Recognizer/Resources/dictionary"

# path to acoustic model files (templates for individual sounds).
acoustic_model = "./Application/Recognizer/Resources/Acoustic_model_RU"


background_config = {
    'verbose': False,
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': acoustic_model,
    'lm': language_model,
    'dict': dictionary,
}

activation_config = {
    'lm': False,
    'keyphrase': 'eva',
    'kws_threshold': 1e-13,
}