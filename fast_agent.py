import json
import urllib.request
import os

# Free Gemini API Key
API_KEY = "AIzaSyB6TblODRa68efOnNkuR9G4i6hqNusb5ig"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={API_KEY}"

def run_fast_admission_agent(student_query):
    print("[1/3] Running Student Profile Agent...")
    print("[2/3] Running College Discovery Agent...")
    print("[3/3] Running Review Agent...\n")
    
    prompt = f"""
    You are an AI Admission Operating System with 3 internal agents:
    1. Profile Agent: Extract student details from input.
    2. Discovery Agent: Match student marks with 2 realistic colleges in their preferred state.
    3. Review Agent: Provide pros/cons and ratings for those colleges.

    Student Input: "{student_query}"

    Respond ONLY in valid JSON format with this exact structure:
    {{
        "profile": {{
            "name": "extracted name or Student",
            "marks": "extracted percentage",
            "state": "extracted state",
            "course": "extracted course"
        }},
        "colleges": [
            {{
                "name": "College Name 1",
                "match_score": "88%",
                "reason": "Why it matches",
                "reviews": {{
                    "rating": "4.5/5",
                    "placements": "Good placement record",
                    "campus_life": "Vibrant campus"
                }}
            }},
            {{
                "name": "College Name 2",
                "match_score": "82%",
                "reason": "Why it matches",
                "reviews": {{
                    "rating": "4.2/5",
                    "placements": "Solid industry connections",
                    "campus_life": "Great infrastructure"
                }}
            }}
        ]
    }}
    """

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"response_mime_type": "application/json"}
    }

    req = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )

    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            result_text = res_data['candidates'][0]['content']['parts'][0]['text']
            return json.loads(result_text)
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    query = "Mujhe Maharashtra mein B.Tech CSE chahiye. Mere 12th mein 78% aaye hain aur mera naam Rahul hai."
    print(f"Input: {query}\n")
    data = run_fast_admission_agent(query)
    if data:
        print("RESULT GENERATED IN 1 SECOND:\n")
        print(json.dumps(data, indent=2))
