# Agent Architecture & Responsibilities

The AI Admission Agent OS is powered by a multi-agent orchestration framework. Each agent has a single, well-defined responsibility and interacts with the shared "Living Profile".

## 1. Orchestrator Agent
* **Role:** The central router and state manager.
* **Function:** Interprets user intent, determines which specialized agent to invoke next, and maintains the overall progress of the admission pipeline.

## 2. Student Profile Agent
* **Role:** Data extraction and structuring.
* **Function:** Converts natural language inputs into a structured JSON profile (marks, budget, preferences, category). Updates the profile as new context is acquired.

## 3. College Discovery Agent
* **Role:** Search and Recommendation.
* **Function:** Queries college databases/APIs to find matches. Outputs an explainable compatibility score based on academic, financial, and geographical constraints.

## 4. Eligibility Agent
* **Role:** Rule validation.
* **Function:** Audits the student profile against the strict admission rules of selected colleges. Outputs definitive Yes/No/Flagged statuses.

## 5. Scholarship Agent
* **Role:** Financial aid discovery.
* **Function:** Identifies eligible scholarships and details their specific requirements and deadlines based on the student profile.

## 6. Document Agent
* **Role:** OCR and Verification.
* **Function:** Processes uploaded files, extracts structured data (e.g., verifying 12th percentage from marksheet), and maintains a document checklist.

## 7. Application Agent (The Preparer)
* **Role:** Form mapping and Pre-filling.
* **Function:** Maps profile data to official college application schemas. **Does NOT submit.** Prepares the application payload and requests explicit student consent.

## 8. Verification Agent (The Auditor)
* **Role:** Pre-flight safety check.
* **Function:** Conducts a final audit of the application payload, documents, and eligibility rules immediately before submission to catch any last-minute discrepancies.

## 9. Submission Agent
* **Role:** Execution.
* **Function:** Executes the actual submission to the college portal (via API or automation) *only after* receiving consent and passing the Verification Agent's audit.

## 10. Payment Agent
* **Role:** Transaction facilitator.
* **Function:** Detects application fees, verifies amounts, and presents a secure payment gateway/link to the student.

## 11. Application Tracker Agent
* **Role:** Post-submission monitoring.
* **Function:** Tracks application IDs, monitors status changes, and manages a deadline/reminder engine for the student.

## 12. College Communication Agent
* **Role:** Consent-based outreach.
* **Function:** Initiates formal inquiries or books counselling appointments on official college channels, strictly based on explicit student permission.
