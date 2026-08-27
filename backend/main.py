import os
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Setup Gemini as the brain for our agents (Free Tier API)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    google_api_key=os.getenv("GEMINI_API_KEY")
)

print("🚀 Starting AI Admission OS powered by CrewAI...\n")

# ==========================================
# 1. PROFILE AGENT
# ==========================================
profile_agent = Agent(
    role="Student Profile Specialist",
    goal="Extract and structure the student's admission criteria like marks and preferred location from their raw input.",
    backstory="You are an expert student counselor. You listen to what a student wants and create a clean, structured JSON profile containing their exact academic marks and geographic preferences.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# ==========================================
# 2. DISCOVERY AGENT
# ==========================================
discovery_agent = Agent(
    role="College Matchmaker",
    goal="Find eligible colleges based on the student's structured profile (marks and location).",
    backstory="You are an admission database expert. You cross-reference student marks with college cutoffs to find realistic and highly-matched college recommendations.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# ==========================================
# 3. REVIEW AGENT (The Trust Layer)
# ==========================================
review_agent = Agent(
    role="Student Review Analyst",
    goal="Fetch realistic student reviews (placements, faculty, campus life) for the recommended colleges.",
    backstory="You are an unbiased higher-education reviewer. You find honest feedback and ratings about colleges so the student can make a confident decision.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# ==========================================
# TASKS
# ==========================================

# Task 1: Extract Profile
extract_profile_task = Task(
    description="Analyze the student's input: '{student_input}'. Extract the name, 12th percentage, and preferred state. Format as a clear summary.",
    expected_output="A structured summary containing the student's name, 12th marks percentage, and preferred state.",
    agent=profile_agent
)

# Task 2: Find Colleges
find_colleges_task = Task(
    description="Based on the extracted profile from the previous task, recommend 2 suitable colleges in the preferred state that accept the given 12th marks. Include a match score.",
    expected_output="A list of 2 recommended colleges with their match scores and reasons for the match.",
    agent=discovery_agent
)

# Task 3: Fetch Reviews
fetch_reviews_task = Task(
    description="For the colleges recommended in the previous task, generate realistic student reviews (pros and cons) regarding placements and campus life.",
    expected_output="A short review summary for each of the recommended colleges, including a star rating.",
    agent=review_agent
)

# ==========================================
# CREW ORCHESTRATION
# ==========================================
admission_crew = Crew(
    agents=[profile_agent, discovery_agent, review_agent],
    tasks=[extract_profile_task, find_colleges_task, fetch_reviews_task],
    process=Process.sequential, # Run tasks one after the other
    verbose=True
)

if __name__ == "__main__":
    student_query = "Mujhe Maharashtra mein B.Tech CSE chahiye. Mere 12th mein 78% aaye hain aur mera naam Rahul hai."
    print(f"Student Input: {student_query}\n")
    
    # Execute the workflow
    result = admission_crew.kickoff(inputs={'student_input': student_query})
    
    print("\n==========================================")
    print("FINAL ADMISSION AGENT REPORT")
    print("==========================================")
    print(result)
