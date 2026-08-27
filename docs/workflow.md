# Demo Workflow: Consent-Gated Auto-Admission

This document outlines the focused workflow for the AI Admission Agent OS demo.

## 1. Data Collection
* **Student Input:** The student enters their core data: Name, 12th Marks, and preferred College State (e.g., "Maharashtra").
* **Profile Agent:** Structures this data into a usable student profile.

## 2. College Discovery & Recommendations
* **Discovery AI:** Based on the marks and preferred state, the AI displays a list of eligible colleges.
* **Match Display:** The system shows why the college matches the student's marks.

## 3. College Reviews (The Trust Layer)
* **Review Agent:** For the recommended colleges, a dedicated Review Agent fetches and displays real student reviews and ratings at the bottom of the screen. This helps the student make an informed decision rather than relying solely on the AI's matching score.

## 4. College Selection
* **Student Action:** The user reviews the recommendations and selects one college they want to apply to.

## 5. Autonomous Application (The Demo Site)
* **Demo Portal:** A separate mock "College Admission Portal" is set up specifically for the demo.
* **Application Agent:** The agent navigates to this demo site and automatically fills in the student's data (Name, Marks, State, etc.) into the form fields.
* **Consent Gate:** Before hitting final submit, the system asks the user for confirmation, completing the "Consent-Gated" loop.
