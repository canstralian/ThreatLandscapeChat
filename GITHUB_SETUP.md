# GitHub Repository Setup Guide

This document explains how to structure, develop, and maintain the
APJ Threat Intelligence System on GitHub.

---

## 1. Clone & Install

```bash
git clone https://github.com/<yourname>/apj-threat-intel
cd apj-threat-intel
pip install -r requirements.txt

## 2. Recommended Repository Structure


├── app.py
├── prompt_engine.py
├── model_inference.py
├── datasets_loader.py
├── slang_lexicon.json
├── PROJECT_SPEC.md
├── HUGGINGFACE.md
├── GITHUB_SETUP.md
├── requirements.txt
└── README.



## 3. Branching Strategy

Main Branch (main)
	•	Always deployable / stable
	•	HuggingFace Space can auto-sync from main

Development Branch (dev)
	•	Active development
	•	Feature branches merge into dev

Feature Branches
	•	Example: feature/vendor-graph
	•	Merge into dev via PR

⸻

## 4. Adding New Components

New Mode?