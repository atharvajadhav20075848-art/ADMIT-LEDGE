# Consent-Gated Autonomous Application Workflow

This document outlines the complete end-to-end workflow for the AI Admission Agent OS. The system ensures the student remains in control of irreversible actions while automating the complex admission journey.

## 1. Initial Interaction & Profiling
* **Student Input:** The student provides their requirements in natural language (e.g., "Mujhe Maharashtra mein B.Tech CSE chahiye. Budget ₹1.2 lakh/year hai. Mere 12th mein 78% hain.").
* **Profile Generation:** The system structures this data into a "Living Profile". This profile is updated as more information is gathered and is shared across all subsequent agents.

## 2. Discovery & Eligibility Matching
* **College Discovery:** Official sources are queried to discover matching colleges/programs based on the Living Profile.
* **Scoring:** Matches are scored transparently (Academic Fit + Budget Fit + Location Fit).
* **Eligibility Check:** Strict rules (cut-offs, entrance requirements) are checked for shortlisted colleges. Uncertain eligibility is flagged for human review.

## 3. Financial & Document Preparation
* **Scholarship Matching:** Identifies applicable scholarships based on the student's category, marks, and financial background.
* **Document Intelligence:** Student uploads required documents (10th/12th marksheets, IDs). OCR extracts data, creates a checklist, and flags missing or unclear documents.

## 4. Application Preparation (The "Auto-Admission" Core)
* **Form Pre-filling:** The system maps the Living Profile and Document Data to the official application form fields of the selected college.
* **Consent Gate:** **CRITICAL STEP.** The system *pauses* and presents the prepared application to the student:
  > "Application is ready. 27/30 fields verified. 3 fields need your confirmation. Application fee: ₹X. Submit to official college portal?"

## 5. Verification & Final Audit
* **Verification Audit:** Once the student confirms, a final check is run to ensure no conflicts exist between uploaded documents, the application form, and college rules.
* **Conflict Resolution:** If a mismatch is found (e.g., "Portal says 75% cutoff but documents show 60%"), the submission is paused for human intervention.

## 6. Execution: Submission & Payment
* **Authorized Submission:** If all audits pass, the application is pushed to the official portal via API, browser automation, or provided as a completed package for manual submission.
* **Payment Gate:** If an application fee is required, a secure payment prompt is provided to the student. AI does not execute payments autonomously.

## 7. Post-Submission Tracking
* **Application Tracker:** Monitors application status, schedules reminders for counselling, document verification, or approaching deadlines.
* **Communication:** Facilitates consent-based communication with the college for inquiries or appointments.
