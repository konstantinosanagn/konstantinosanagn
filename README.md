# Konstantinos Anagnostopoulos

**BEng Computer Science @ Columbia (’26) · BSc Mathematical Economics @ Richmond (’24)  
Incoming Software Engineer @ Tavily · AI/ML & full-stack engineer**

New York, NY · [LinkedIn](https://www.linkedin.com/in/kon-anagn/) · [Email](mailto:ka3037@columbia.edu)

---

## About me

- I like building **AI-heavy products end-to-end** – from data pipelines and agents to dashboards and tests.
- Background in **CS, mathematical economics, and prediction markets**, with experience across:
  - **Multi-agent systems** (LangGraph, OpenAI, Tavily, Polymarket data)  
  - **Modern web stacks** (FastAPI, Rails 8.1, Next.js/React/TypeScript, Postgres, MongoDB)  
  - **ML / NLP / CV** (PyTorch, Transformers, YOLOv8, argument mining, RL for econ)
- Professional experience as:
  - **Incoming SWE @ Tavily (2026)** – multi-agent search & reasoning systems.  
  - **AI & Computer Vision Engineering Intern @ Eulerion** – YOLOv8 pipelines + real-time blackjack game logic on casino camera streams.  
  - **Head TA – Advanced Database Systems (COMS E6111, Columbia)** – grad DB systems (IR, web search, OLAP).  
  - **NLP & RL Researcher @ University of Richmond** – argument mining, link prediction, and RL for economic optimization.

I’m especially interested in **prediction markets, market microstructure, AI for finance/insurance**, and **agentic systems** that interact with real users and real data.

---

## What I’m working on

### 🔮 Prophecy — Multi-Agent Prediction Markets Analysis Platform  
**Repo:** [prophecy-pred-markets](https://github.com/konstantinosanagn/prophecy-pred-markets)

Full-stack system that takes a **Polymarket URL** and runs a **multi-agent LangGraph pipeline** to produce phased trading signals and Kelly-sized recommendations:

- **Backend:** FastAPI + async stack (Motor, aiohttp) with TTL caching, Redis fallback, circuit breakers, retries, structured logging, health/readiness probes, and MongoDB Atlas for runs & events. :contentReference[oaicite:0]{index=0}  
- **Agents:** Market, event, Tavily prompt, news aggregation, news summarization, probability/edge, strategy, and report agents orchestrated with LangGraph, using Tavily + OpenAI against Polymarket data. :contentReference[oaicite:1]{index=1}  
- **Frontend:** Next.js + TypeScript + Tailwind dashboard that polls the backend and surfaces **incremental phases** (market snapshot → news context → signal → report). :contentReference[oaicite:2]{index=2}  
- **Quality:** 140+ tests across backend/frontend (pytest, Jest/RTL), plus deployment to **AWS Elastic Beanstalk** (backend) and **Vercel** (frontend).

**Stack:** FastAPI · LangGraph · OpenAI · Tavily · MongoDB Atlas · Redis · Next.js · TypeScript · Tailwind · AWS · Vercel

---

### 🛡️ Vang — AI-Powered Excess & Surplus Insurance Marketplace  
*(Private repo for now; live code mirrors what’s on my resume.)*

Multi-tenant B2B marketplace where clients post coverage requests and carriers can **filter, chat, and submit bids**:

- **Frontend:** Type-safe Next.js/React/TypeScript UI with Tailwind and a library of reusable components for request creation, bid management, and messaging.  
- **Backend:** Authenticated REST APIs with Zod validation, JWT auth, and **transactional PostgreSQL** queries.  
- **DevEx:** GitHub Actions CI, coverage gates, lint/format checks, and auto-deploys to Vercel on clean builds.

**Stack:** Next.js · React · TypeScript · Tailwind · Node/FastAPI · PostgreSQL · Zod · JWT · GitHub Actions · Vercel · AWS

---

### 📧 CampAIgn — AI-Powered Campaign Management SaaS  
**Repo:** [campaign-saas](https://github.com/konstantinosanagn/campaign-saas)

Team project for a **modern SaaS** that runs AI-powered B2B outreach campaigns via agent workflows:

- **Backend:** Ruby on Rails 8.1 with PostgreSQL; bin/setup tooling for clean onboarding. :contentReference[oaicite:3]{index=3}  
- **Frontend:** React 18 + TypeScript with Shakapacker/Webpack 5, driven by Node 20+ toolchain. :contentReference[oaicite:4]{index=4}  
- **Flow:** Campaign creation → research → draft → critique → design → send, using multiple agents and integrated email flows.

**Stack:** Rails 8.1 · Ruby 3.3 · React 18 · TypeScript · PostgreSQL · Node 20+ · Webpack (Shakapacker)

---

### 🧠 Argument Mining, Link Prediction & IR

I also maintain a set of research-oriented repos around **argument mining, link prediction, and interactive IR**:

- **Link prediction with LLMs** — [arg_relation](https://github.com/konstantinosanagn/arg_relation) & [link-prediction](https://github.com/konstantinosanagn/link-prediction)  
  - Infrastructure for running **LLaMA, Mistral, and other models** on link-prediction tasks, using Hugging Face `transformers` and carefully managed Conda environments. :contentReference[oaicite:5]{index=5}  
  - Scripts and documentation for experiments, dataset handling, and model loading on research compute. :contentReference[oaicite:6]{index=6}  

- **Interactive IR with relevance feedback** — [information-retrieval-user-feedback](https://github.com/konstantinosanagn/information-retrieval-user-feedback)  
  - Python system that wraps search with **user feedback loops**, using **Rocchio’s algorithm + TF-IDF** to re-weight terms and expand queries based on relevant vs. non-relevant documents. :contentReference[oaicite:7]{index=7}  

- **Privacy Tech Selection Tool** — [privacy-tech-selection-tool](https://github.com/konstantinosanagn/privacy-tech-selection-tool)  
  - Frontend tool to help pick privacy-enhancing technologies for different use cases (UI/UX and decision logic). :contentReference[oaicite:8]{index=8}  

---

## Tech I like working with

**Languages:**  
Python · TypeScript · JavaScript · Java · C/C++ · SQL

**Backend / Systems:**  
FastAPI · Node.js · Ruby on Rails · REST APIs · LangGraph · aiohttp · Motor · MongoDB Atlas · PostgreSQL · Redis · Docker · CI/CD (GitHub Actions)

**Frontend:**  
React · Next.js · Tailwind CSS · modern TypeScript tooling

**ML / Data:**  
PyTorch · Transformers · YOLOv8 · scikit-learn · NumPy · Pandas · OpenCV

**Infra / Cloud:**  
AWS (Elastic Beanstalk, basic infra) · Vercel · GCP (Compute Engine)

---

## What I’m open to

- **SWE / ML / infra roles** where I can own backend + product logic + a real UI.  
- **Research collaborations** in prediction markets, market microstructure, and applied RL.  
- **Quant-adjacent problems** (signal extraction, strategy tooling, risk/position sizing).

If any of this overlaps with what you’re building, feel free to reach out on  
👉 [LinkedIn](https://www.linkedin.com/in/kon-anagn/) or [email](mailto:ka3037@columbia.edu).
