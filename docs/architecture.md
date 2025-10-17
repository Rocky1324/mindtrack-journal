# 🧠 MindTrack Journal — Architecture Overview

## 1. 🎯 Project Objective

Build a web app that helps young users track their productivity and mental well-being through:
- An onboarding questionnaire
- A personalized action plan
- Daily journaling
- Progress visualization via dashboard

---

## 2. 🧱 Proposed Modular Architecture
Frontend (React or other)
|-- Auth UI          -> login, signup
|-- Questionnaire UI -> onboarding flow
|-- Journal UI       -> daily entries
`-- Dashboard        -> progress tracking

Backend (Flask)
|-- /auth          -> login, signup, token handling
|-- /profile       -> user profile creation
|-- /questionnaire -> receive answers
|-- /plan          -> generate personalized plan
|-- /journal       -> save daily entries
`-- /feedback      -> suggestions, reminders, encouragement






## 3. 🗃️ Database Schema (to be confirmed)

- **User**
  - `id`, `email`, `password_hash`
- **Profile**
  - `user_id`, `age`, `goals`, `preferences`
- **JournalEntry**
  - `user_id`, `date`, `mood`, `notes`
- **Plan**
  - `user_id`, `generated_tasks`, `created_at`
- **Feedback**
  - `user_id`, `message`, `timestamp`

---

## 4. 🔐 Authentication

- JWT tokens (to be confirmed)
- Middleware to protect routes
- Token storage on frontend (localStorage or cookies)

---

## 5. 🔄 User Flow (MVP)

1. User signs up and creates a profile  
2. Completes onboarding questionnaire  
3. Backend generates a personalized plan  
4. User logs daily entries in journal  
5. Receives feedback or suggestions  
6. Views progress in dashboard

---

## 6. 🧪 Testing & Deployment (later phase)

- Backend unit tests (pytest)
- Deployment via Render / Railway / Vercel
- CI/CD pipeline (to be discussed)



