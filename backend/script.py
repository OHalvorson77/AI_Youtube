from groq import Groq



api_key="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"


client = Groq(api_key=api_key)


def generate_script(user_prompt):
    conversation_history=[]
    system_prompt="Write two minute long paragraphs about user prompt"

    conversation_history.append({"role": "system", "content": system_prompt})

    conversation_history.append({"role": "user", "content": user_prompt})

    completion = client.chat.completions.create(
            model="llama3-70b-8192", 
            messages=conversation_history, 
            temperature=0.8, 
            max_tokens=1024, 
            top_p=1, 
            stream=True, 
            stop=None
        )
    
    response_content = ""
    for chunk in completion:
        response_content += chunk.choices[0].delta.content or ""

    conversation_history.append({"role": "assistant", "content": response_content})

        

    return [msg["content"] if msg["role"] == "assistant" else None for msg in conversation_history]


