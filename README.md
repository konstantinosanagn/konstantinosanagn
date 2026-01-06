<div align="center">

# 👋 Hey, I’m Konstantinos

**BEng Computer Science @ Columbia ’26 · BSc Mathematical Economics @ Richmond ’24**  


📍 New York, NY  
🔗 [LinkedIn](https://www.linkedin.com/in/kon-anagn/) · 📧 [Email](mailto:ka3037@columbia.edu) · 💻 [Prophecy live](https://prophecy-pred-markets.vercel.app)

</div>

---

## 🧑‍💻 About me

- I build **AI-heavy products end-to-end** – from async backends and agents to dashboards and tests.
- Background in **CS, mathematical economics, and prediction markets**, with experience across:
  - **Multi-agent systems** (LangGraph, OpenAI, Tavily, Polymarket)
  - **Modern web stacks** (FastAPI, Rails 8.1, Next.js/React/TypeScript, Postgres, MongoDB)
  - **ML / NLP / CV** (PyTorch, Transformers, YOLOv8, RL for econ, argument mining)
- Professional experience:
  - 🔜 **Incoming SWE @ Tavily** – multi-agent search & reasoning systems.
  - 🎰 **AI & Computer Vision Engineering Intern @ Eulerion** – YOLOv8 pipelines + real-time blackjack logic on casino camera streams.
  - 🎓 **Head TA – Advanced Database Systems (COMS E6111, Columbia)** – IR, web search, OLAP, data mining.
  - 📚 **NLP & RL Researcher @ University of Richmond** – argument mining, link prediction, and RL for economic optimization.

I’m especially interested in **prediction markets, market microstructure, AI for finance/insurance**, and **agentic systems** that interact with real users and real data.

---

## 🚀 Featured projects

### 🔮 Prophecy — Multi-Agent Prediction Markets Analysis Platform  
**Repo:** [prophecy-pred-markets](https://github.com/konstantinosanagn/prophecy-pred-markets) · **Live:** https://prophecy-pred-markets.vercel.app

Full-stack system that takes a **Polymarket market URL** and runs a **LangGraph multi-agent pipeline** to produce phased trading signals and Kelly-sized recommendations:

- 🧱 **Architecture:** FastAPI backend, Next.js 16 + TypeScript + Tailwind frontend, MongoDB Atlas, optional Redis cache, deployed on **AWS Elastic Beanstalk + Vercel**.
- 🕸️ **Agents:** Market, event, Tavily prompt, news aggregation, news summarization, probability/edge, strategy, and report agents orchestrated via **LangGraph** against Polymarket + Tavily + OpenAI.
- ⚡ **Runtime:** Async data pipelines with `aiohttp` + Motor, TTL caching, circuit breakers, retries, structured logging, health/readiness probes.
- ✅ **Quality:** 140+ tests across backend/frontend (pytest, Jest/RTL) and a dashboard that surfaces **incremental phases** (market snapshot → news context → signal → report).

**Stack:** FastAPI · LangGraph · OpenAI · Tavily · MongoDB Atlas · Redis · Next.js · TypeScript · Tailwind · AWS · Vercel

---

### 🛡️ Vang — AI-Powered Excess & Surplus Insurance Marketplace  
*(Private for now; mirrors the production-focused work on my resume.)*

Multi-tenant B2B marketplace where clients post coverage requests and carriers **filter, chat, and submit bids**:

- 🧩 **Frontend:** Type-safe Next.js/React/TypeScript UI with Tailwind and a reusable component library for request creation, bid management, and messaging.
- 🔐 **Backend:** Authenticated REST APIs with Zod validation, JWT auth, and **transactional PostgreSQL** queries.
- 🧪 **DevEx:** GitHub Actions CI, coverage gates, lint/format checks, auto-deploys to Vercel on clean builds.

**Stack:** Next.js · React · TypeScript · Tailwind · Node/FastAPI · PostgreSQL · Zod · JWT · GitHub Actions · Vercel · AWS

---

### 📧 CampAIgn — AI-Powered Campaign Management SaaS  
**Repo:** [campaign-saas](https://github.com/konstantinosanagn/campaign-saas)

A **modern SaaS** app for AI-powered B2B outreach campaigns with multi-agent workflows:

- 🏗️ **Backend:** Ruby on Rails 8.1 + PostgreSQL, with `bin/setup` and Docker tooling for clean onboarding.
- 💻 **Frontend:** React 18 + TypeScript + Tailwind via Shakapacker/Webpack 5 on top of Node 20+.  
- 🤖 **Flow:** Campaigns run through **research → draft → critique → design → send** using orchestrated AI agents and integrated email flows.

**Stack:** Rails 8.1 · Ruby 3.3 · React 18 · TypeScript · PostgreSQL · Node 20+ · Webpack (Shakapacker) · Docker

---

### 🧠 Argument Mining, Link Prediction & IR

**🧬 arg_relation** – [repo](https://github.com/konstantinosanagn/arg_relation)  
**🔗 link-prediction** – [repo](https://github.com/konstantinosanagn/link-prediction)

- Research-oriented infrastructure for **argument mining and link prediction** using **LLaMA, Mistral, and other models** via Hugging Face `transformers`.
- Conda-based environments, dataset loading, and experiment scripts for running link-prediction tasks on research compute.

**Stack:** Python · PyTorch · Transformers · Hugging Face · Conda

---

**🔍 information-retrieval-user-feedback** – [repo](https://github.com/konstantinosanagn/information-retrieval-user-feedback)

- Interactive IR system that wraps search with **user feedback loops**, using **Rocchio + TF-IDF** to re-weight terms and expand queries from relevant vs. non-relevant documents.

**Stack:** Python · scikit-learn · NumPy · IR fundamentals

---

**🛡️ privacy-tech-selection-tool** – [repo](https://github.com/konstantinosanagn/privacy-tech-selection-tool)

- Frontend tool to help choose **privacy-enhancing technologies** for different use cases via a simple UI and decision logic.

**Stack:** HTML/CSS/JS · basic web UI

---

## 🛠️ Tech I like working with

**Languages:**  
`Python` · `TypeScript` · `JavaScript` · `Java` · `C/C++` · `SQL`

**Backend / Systems:**  
`FastAPI` · `Node.js` · `Ruby on Rails` · `LangGraph` · `REST` · `aiohttp` · `Motor` · `MongoDB Atlas` · `PostgreSQL` · `Redis` · `Docker` · `GitHub Actions`

**Frontend:**  
`React` · `Next.js` · `Tailwind CSS` · modern TypeScript build tooling

**ML / Data:**  
`PyTorch` · `Transformers` · `YOLOv8` · `scikit-learn` · `NumPy` · `Pandas` · `OpenCV`

**Cloud / Infra:**  
`AWS (Elastic Beanstalk, basic infra)` · `Vercel` · `GCP (Compute Engine)`

---

## 🎯 Currently & Open to

**Now:**

- Polishing **Prophecy**’s experience (strategy presets, backtesting, more markets).
- Iterating on **Vang**’s quoting and marketplace flows.


**Open to:**

- SWE / ML / infra roles where I can own **backend + product logic + UI**.
- Research collaborations in **prediction markets**, **market microstructure**, or **applied RL**.
- **Quant-adjacent** problems: signal extraction, strategy tooling, risk/position sizing.

If any of this matches what you’re building, feel free to reach out:  
👉 [LinkedIn](https://www.linkedin.com/in/kon-anagn/) · [Email](mailto:ka3037@columbia.edu)
