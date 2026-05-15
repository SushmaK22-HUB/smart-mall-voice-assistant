import google.generativeai as genai

genai.configure(api_key="AIzaSyAlP_Y8fruzu_Qi3ZgFKESDw0AF0ShJGMs")

for model in genai.list_models():
    print(model.name)