# Cherry Republic Voice Assistant – AI Phone Agent

AI voice agent that answers customer calls for Cherry Republic, handling product questions and basic order inquiries using ElevenLabs Agents and Twilio.

## What the agent does

- Greets callers and routes them through inqueries about the company they may have.
- Answers FAQs about products, locations, and shipping.
- Handles simple order-status style questions in a demo flow.
- Tested across common customer scenarios to refine prompts and reduce confusing or off-topic responses.

## How it works

- **ElevenLabs Agents** powers conversational logic, memory, and synthetic voice.
- **Twilio** provides the phone number and routes calls into the agent.
- Custom prompts and knowledge base entries keep responses on-brand and on-topic.

## My role

- Designed the call flow, prompts, and guardrails for the agent.
- Configured tools, knowledge, and voice settings in ElevenLabs.
- Tested with sample customer scenarios and iterated to reduce dead-ends.


## Development approach

This project uses the ElevenLabs Agents platform for production. The repo also includes initial prototype files (`Cherry_voice.py`, `eleven_labs.md`, `faq.json`, etc.) that were used to explore the ElevenLabs API and test conversation flows before moving to the no-code agent platform.

These prototypes demonstrate:
- Python integration with ElevenLabs API
- Custom conversation logic and FAQ matching
- Voice synthesis and playback experimentation

The final agent uses ElevenLabs Agents for reliability, but the prototypes show the technical foundation and API understanding behind the project.


- ## Screenshots

### Agent Configuration
![Agent Dashboard](images:agent-dashboard.png)*ElevenLabs agent configuration showing system prompt, voice settings (Eric - Smooth, Trustworthy), and LLM (Gemini 2.5 Flash).*
*ElevenLabs agent configuration showing system prompt, voice settings (Eric - Smooth, Trustworthy), and LLM (Gemini 2.5 Flash).*


### Knowledge Base
![Knowledge Base](knowledgebaseCherry%20voice.png)*Agent knowledge base containing Cherry Republic FAQs about products, locations, and shipping.*


### Conversation Example
![Conversation Example](conversationexample%20cherry%20ai.png)*Live conversation showing Cherry Voice handling a customer inquiry about Christmas gift recommendations, demonstrating natural product knowledge and personalized responses.*


## Try it yourself

**Phone:** +1 (269) 215-4951

Call this number to experience the Cherry Voice agent live. The AI will:
- Answer your call with a friendly greeting
- Help with product questions and recommendations
- Provide information about store locations and shipping
- Handle basic order inquiries in a demo flow


