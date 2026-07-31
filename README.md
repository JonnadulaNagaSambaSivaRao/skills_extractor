import os
from typing import TypedDict

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from langgraph.graph import StateGraph, START, END

load_dotenv()

# ---------------------------
# Create LLM
# ---------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------
# Prompt
# ---------------------------

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an ATS Resume Parser.

Your task is to extract ONLY the skills and important keywords that are explicitly mentioned in the given text.

Rules:
- Do NOT infer skills.
- Do NOT add missing skills.
- Do NOT explain anything.
- Do NOT rewrite the skills.
- Keep the original wording.
- Remove duplicates.

Return ONLY in this format.

Skills:
- Skill 1
- Skill 2
- Skill 3

Keywords:
- Keyword 1
- Keyword 2
- Keyword 3

If nothing is found return

Skills:
No skills found

Keywords:
No keywords found
"""
        ),
        (
            "human",
            """
Text:

{text}
"""
        )
    ]
)

chain = prompt | llm

# ---------------------------
# State
# ---------------------------

class ResumeState(TypedDict):
    text: str
    result: str

# ---------------------------
# Node
# ---------------------------

def extract_skills(state: ResumeState):

    print("\n==============================")
    print("Step 1 : Extracting Skills...")
    print("==============================")

    response = chain.invoke(
        {
            "text": state["text"]
        }
    )

    print("✓ Extraction Completed")

    return {
        "result": response.content
    }

# ---------------------------
# Build Graph
# ---------------------------

graph = StateGraph(ResumeState)

graph.add_node("Extract Skills", extract_skills)

graph.add_edge(START, "Extract Skills")
graph.add_edge("Extract Skills", END)

app = graph.compile()

# ---------------------------
# Save Graph Image
# ---------------------------

try:
    png = app.get_graph().draw_mermaid_png()

    with open("graph.png", "wb") as f:
        f.write(png)

    print("\nGraph saved as graph.png")

except Exception as e:
    print("\nGraph image could not be created.")
    print(e)

# ---------------------------
# Run
# ---------------------------

print("=" * 50)
print("      Resume Skills Extractor")
print("=" * 50)

text = input("\nEnter Resume or Job Description:\n\n")

result = app.invoke(
    {
        "text": text
    }
)

print("\n==============================")
print("Extraction Result")
print("==============================\n")

print(result["result"])
