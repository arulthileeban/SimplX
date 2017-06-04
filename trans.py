from google.cloud import translate
# -*- coding: utf-8 -*-
def translat(text):
	translate_client = translate.Client()
	target = 'en'
	translation = translate_client.translate(text,target_language=target)
	return str(translation)
