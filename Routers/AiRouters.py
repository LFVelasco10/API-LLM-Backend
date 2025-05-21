
from fastapi import APIRouter
from openai import OpenAI
from Interfaces.ChatInterfaces import ChatRespuesta, InputMessage


Router = APIRouter()

cliente = OpenAI(api_key="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",
                 base_url="https://openrouter.ai/api/v1",)

@Router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message: "+data["message"])

    message = "Por favor dame una respuesta concisa y breve a la siguiente pregunta y sin simbolos innecesarios: "\
              "evita usar otros idiomas que no sean el castellano y escribe una respuesta concisa, "
    try:
        completion:ChatRespuesta = cliente.chat.completions.create(
            model="google/gemini-2.5-flash-preview",
            messages=[
                {"role": "system",
                 "content":"Eres un Asistente que siempre responde en castellano"},
                {"role": "user",
                 "content": message+ "responde a esta pregunta: "+data["message"]}
            ]
        )
        print("response: "+completion.choices[0].message.content)  
        return{"response": completion.choices[0].message.content,} 
    except Exception as e:
        print(f"Error: ", {e})
        return{"error":str(e)}
    
@Router.post("/ai-chat-2")    
def aiChat2(data: InputMessage):
    data = data.model_dump()
    print("message: "+data["message"])

    message = "Por favor dame una respuesta concisa y breve a la siguiente pregunta y sin simbolos innecesarios: "\
              "evita usar otros idiomas que no sean el castellano y escribe una respuesta concisa, "
    try:
        completion:ChatRespuesta = cliente.chat.completions.create(
            model="deepseek/deepseek-prover-v2:free",
            messages=[
                {"role": "system",
                 "content":"Eres un Asistente que siempre responde en castellano"},
                {"role": "user",
                 "content": message+ "responde a esta pregunta: "+data["message"]}
            ]
        )
        print("response: "+completion.choices[0].message.content)  
        return{"response": completion.choices[0].message.content,} 
    except Exception as e:
        print(f"Error: ", {e})
        return{"error":str(e)}
    