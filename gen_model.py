import google.generativeai as genai
import os
genai.configure(api_key=os.environ["GEMINI_API_TOKEN"])


# Function to generate a response
def run(prompt):
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        generation_config={
            "stop_sequences": ["***"],
            "max_output_tokens": 2048,
            "temperature": 0.5,
            "top_p": 1,
            "top_k": 1,
        }
    )

    response = model.generate_content(prompt)
    return response.text
