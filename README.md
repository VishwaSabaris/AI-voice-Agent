# AI Voice Agent

An AI-powered voice assistant capable of handling real-time customer conversations through speech recognition, natural language processing, and text-to-speech synthesis. The project is designed to automate customer interactions such as restaurant order taking, query handling, and email notifications.

---

## Project Overview

This project demonstrates how Artificial Intelligence can be integrated with telephony and voice technologies to create an autonomous voice assistant.

The AI Voice Agent listens to user speech, converts it into text, processes the request using a language model, generates an intelligent response, converts the response back to speech, and communicates it to the caller.

The system can also trigger automated actions such as order processing and email notifications based on the conversation.

---

## Features

* Real-time voice conversation handling
* Speech-to-Text (STT) processing
* AI-powered response generation
* Text-to-Speech (TTS) synthesis
* Restaurant order-taking workflow
* Automated email notifications
* Modular architecture for future integrations
* Tamil language support (Work in Progress)

---

## System Architecture

```text
Customer Call
      │
      ▼
Speech-to-Text (STT)
      │
      ▼
Language Model Processing
      │
      ▼
Response Generation
      │
      ▼
Text-to-Speech (TTS)
      │
      ▼
Voice Response to User
      │
      ▼
Order Processing / Email Notification
```

---

## Tech Stack

### Programming Language

* Python

### AI Components

* Small Language Models (SLM)
* Speech Recognition
* Natural Language Processing

### Voice Technologies

* Speech-to-Text (STT)
* Text-to-Speech (TTS)

### Development Tools

* Linux
* Git
* GitHub
* Virtual Environment (venv)

---

## Project Structure

```text
AI-voice-Agent/
│
├── agent.py
│
├── stt/
│   └── Speech Recognition Components
│
├── slm/
│   └── Language Model Processing
│
├── tts/
│   └── Text-to-Speech Components
│
├── utils/
│   └── Helper Functions
│
└── tests/
    └── Test Scripts
```

---

## Workflow

1. User speaks through the connected audio device.
2. Speech is converted into text using Speech-to-Text.
3. The text is processed by the language model.
4. The model generates an appropriate response.
5. The response is converted into speech.
6. The generated voice is played back to the user.
7. Optional actions such as email notifications are triggered.

---

## Use Cases

### Restaurant Order Assistant

* Accept customer orders
* Confirm order details
* Generate order summaries
* Send notifications

### Customer Support

* Answer frequently asked questions
* Handle basic customer queries
* Route requests for further processing

### Voice Automation

* Automated call handling
* Information collection
* Task execution through voice commands

---

## Future Improvements

* Full Tamil conversational support
* Integration with local Large Language Models
* Real-time call integration
* WhatsApp integration
* Database-backed order management
* Multi-language support
* Cloud deployment

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Speech Recognition
* Text-to-Speech Systems
* AI Voice Agents
* Natural Language Processing
* Python Application Development
* Linux-based Development
* Modular System Design

---

## Author

Vishwa Sabaris V

B.E. Computer Science and Engineering (AI & ML)

Kalaignar Karunanidhi Institute of Technology (KIT), Coimbatore
