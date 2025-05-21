from openai import OpenAI
cliente = OpenAI(api_key="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",
                 base_url="https://openrouter.ai/api/v1",)
massage = input("cuales es tu pregunta: ")

prompt = (
    "por favor dame una respuesta concisa y breve a la siguiente pregunta y sin simbolos innecesarios: "
    "evita usar otros idiomas que no sean el castellano y escribe una respuesta concisa, "\
        f"pregunta del Usuario: {massage}")
completion = cliente.chat.completions.create(
    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    messages=[
        {"role": "user", 
         "content": prompt}
    ]
    )
print(completion.choices[0].message.content)