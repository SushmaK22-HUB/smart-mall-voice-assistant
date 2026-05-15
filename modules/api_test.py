import google.generativeai as genai

genai.configure(api_key="AIzaSyAPY-iiz7pSvOEDDMTIyH4VEKGuyBASHSE")

try:
    models = genai.list_models()

    print("✅ API Key Working")

    for model in models:
        print(model.name)

except Exception as e:
    print("❌ Error:", e)