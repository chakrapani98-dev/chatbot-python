import getpass
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass(groq_api_key)

from langchain.chat_models import init_chat_model

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")



from langchain_core.messages import HumanMessage,SystemMessage

input_msg="whats your name"
while input_msg!="exit":
  input_msg=input("Ask:",)
  messages = [
    # SystemMessage(content="You are a helpful assistant! Your name is Bob."),
    HumanMessage(content=input_msg),]
  output_msg=model.invoke(messages)
  print(output_msg.content)

# model.invoke([HumanMessage(content="Hi! I'm Bob")])