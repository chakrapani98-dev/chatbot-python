import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage,SystemMessage


load_dotenv()
# --- langchain setup----
groq_api_key=os.getenv("GROQ_API_KEY")

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass(groq_api_key)

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")
# -----langchain setup end-----

# Define a new graph
workflow = StateGraph(state_schema=MessagesState)

# Define the function that calls the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

# Define the (single) node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}

#model main invoke code
input_msg="whats your name"
while input_msg!="exit":
  input_msg=input("Ask:",)
  messages = [
    # SystemMessage(content="You are a helpful assistant! Your name is Bob."),
    HumanMessage(content=input_msg),]
  output_msg=app.invoke({"messages": messages}, config)
  output_msg["messages"][-1].pretty_print()

