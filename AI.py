import openai

# Set your OpenAI API key here

# To get the secret key, got to openai website and user settings and then create new api key
openai.api_key = "(note: enter your secret key.)"  # enter your secret key

# Define the model engine
model_engine = "text-davinci-003"

while True:
    prompt = input('Enter new prompt: ')

    if 'exit' in prompt or 'quit' in prompt:
        break

    try:
        # Send the prompt to OpenAI API for completion
        completion = openai.Completion.create(
            engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)

        # Get the response text from the API
        response = completion.choices[0].text

        print(response)

    except Exception as e:
        # Handle any API errors
        print("Error:", e)
