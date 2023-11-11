from openai import OpenAI

client = OpenAI(api_key = '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')


messages = [
   {"role": "system", "content": "LE GLOBE"}
]
user_input = input()
while user_input != 'q':


   messages.append({"role": "user", "content": user_input})
   completion = client.chat.completions.create(
       model = 'gpt-3.5-turbo',
       messages=messages
   )
   messages.append(completion.choices[0].message)
   print()
   print(completion.choices[0].message.content)
   print()
   user_input = input()


