# Core Agents for Demo

For the streamlined demo workflow, the following key agents will be utilized:

## 1. Profile Agent
* **Function:** Collects and structures the student's input data (Marks, Preferred State, Name).

## 2. Discovery Agent
* **Function:** Matches the student's marks and state preference against a database of colleges and returns the eligible options.

## 3. Review Agent (NEW)
* **Function:** A specialized agent that runs in the background. When colleges are recommended, it fetches sentiment and review highlights (e.g., placements, faculty, campus life) and displays them to the user. This builds trust.

## 4. Application Agent (The Form Filler)
* **Function:** Once a college is selected, this agent connects to the custom **Demo Site**. It maps the student's profile data to the form fields on the demo site and executes the auto-fill process.

## 5. Verification/Consent Agent
* **Function:** The final check that pauses the Application Agent before submission, asking the user: "Form is filled on the demo site. Confirm submission?"
