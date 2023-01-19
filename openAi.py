import openai
def summary(summarized_text):
    openai.api_key = "***********"  # you can get the openAi key from https://openai.com/api/
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= summarized_text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

    text = response['choices'][0]['text']

    print (text)
    print ("\n")
