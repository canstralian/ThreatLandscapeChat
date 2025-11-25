

⸻

APJ Threat Intelligence System

Architecture & Operational Design

1. Purpose

A multilingual, culturally aware threat-intelligence platform capable of interpreting Mandarin/Cantonese cybercrime chatter and transforming it into structured intelligence for APJ-focused defensive operations.

⸻

2. Major Components

2.1 Ingest Layer
	•	Marketplace scrapers (read-only)
	•	Telegram/Discord crawlers
	•	Domain & WHOIS monitors
	•	File upload entry via Gradio

2.2 Language Layer
	•	Dialect detection (Mandarin vs Cantonese)
	•	Idiom interpreter
	•	Slang lexicon with auto-expansion

2.3 Intelligence Layer
	•	Threat classification model (Transformers)
	•	Vendor graph builder
	•	Trend engine & anomaly detector
	•	Reputational scoring

2.4 Operator Interface
	•	Mobile-first Gradio chat console
	•	Mode switcher:
	•	Threat Intel
	•	Translation
	•	Marketplace Watch
	•	Analyst Tools

⸻

3. Data Structures

Message Object

{
  "raw_text": "...",
  "language": "zh-yue",
  "slang": ["飛數", "黑料"],
  "intent": "selling_stolen_data",
  "risk_score": 4
}

Vendor Node

{
  "handle": "darkcat99",
  "languages": ["zh-CN"],
  "reputation": 0.74,
  "products": ["phishing-kit", "RAT"],
  "last_seen": "2025-01-04"
}


⸻

4. Pipeline Flow

Source → Ingest → Language Engine → Threat Classifier → 
Vendor Graph → Analysis → UI


⸻

5. Requirements
	•	Python 3.10+
	•	gradio
	•	transformers
	•	datasets
	•	pydantic

⸻
