#Chatbot using llama2 model. 
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt template
template = """ 
Answer the question below. 
Here is the conversation history: {context}
Question: {question}
Answer:
"""

# Initialize the model and prompt template
#model = OllamaLLM(model="llama3", base_url="http://localhost:11434")
model = OllamaLLM(model="llama2", base_url="http://localhost:11434")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break  # Use 'break' to exit the loop

        # Remove the invalid '=' and correctly pass the dictionary
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)

        # Update the context with the current conversation
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
