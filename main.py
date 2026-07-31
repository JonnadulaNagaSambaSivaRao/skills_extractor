import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Create Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert resume analyzer.

Extract the skills and important keywords from the given text.

Return ONLY in the following format.

Skills:
- Skill 1
- Skill 2
- Skill 3

Keywords:
- Keyword 1
- Keyword 2
- Keyword 3

Rules:
- Do not explain anything.
- Do not add extra text.
- If no skills are found, return "No skills found".
"""
    ),
    (
        "human",
        """
Text:
{text}
"""
    )
])

# Create chain
chain = prompt | llm

print("=" * 50)
print("      Skills & Keywords Extractor")
print("=" * 50)

text = input("\nEnter Resume or Job Description:\n\n")

response = chain.invoke(
    {
        "text": text
    }
)

print("\nExtraction Result\n")
print(response.content)