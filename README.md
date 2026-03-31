# 🚀 DeepNav-Agent
> **A Unified Multi-Agent System for Real-World Intelligence, Business Analysis, and Autonomous Workflows.**

---

## 🌟 Overview
DeepNav-Agent is an autonomous AI agent that bridges the gap between Large Language Models and the physical world. By integrating DeepSeek-V3 with the Amap (AutoNavi) Geolocation Engine and DuckDuckGo Web Search, it transforms abstract queries into real-world actions.

Whether you are analyzing business competition in a specific city district or planning a multi-stop business trip, DeepNav-Agent handles the research, spatial logic, and reporting automatically.

---

## ✨ Key Features
* **🤖 Multi-Agent Coordination**:
   * **📍 Geographic Analyst**: Master of the Amap API. It handles spatial logic, competitor density, and coordinate-based reasoning.

   * **🛣️ Web Researcher**: Your frontline scout for real-time news, brand reputation, and market trends.

   * **🌐 Team Orchestrator**: Synthesizes cross-domain data into structured professional reports and manages the Autonomous Workflow.

* **📂 Automated Workflow**: Seamlessly saves research findings and trip plans into local markdown notes (agent_notes.txt).
  
* **🛠️ Built-in Productivity Tools**:

   * **Financial**: Real-time currency conversion.

   * **Security**: High-entropy random password generation.

   * **System**: Local disk space and resource monitoring.

---

## 📸 Real-World Use Cases
### 🏪 Case Study: Opening a Bubble Tea Shop
   * **User Input**: "I want to open a premium milk tea shop in Sanlitun, Beijing. Analyze the competition and give me a guide."

   * **Workflow**:

      1. Geographic Analyst pulls all 'HeyTea' and 'Nayuki' locations in a 3km radius.

      2. Web Researcher fetches recent social media trends and "foot traffic" news for Sanlitun.
   
      3. O rchestrator calculates the "Market Saturation Index" and saves a Final Opening Guide to agent_notes.txt.
     
      <div align="center">
     <img width="838" height="714" alt="image" src="https://github.com/user-attachments/assets/83b45fa1-403d-45f8-81a1-224f18f0919c" />
   </div>
  
## ✈️ Case Study: Intelligent Travel Planning
* **User Input**: "Plan a 3-day business trip to Shanghai. I prefer hotels near the Bund. Check the weather and find 3 quiet cafes for meetings."

* **Workflow**: > Agent learns your preference for "quiet cafes" and "Bund area" (Pal mode), plans the route, and generates a structured itinerary.

     <div align="center">
    <img width="864" height="737" alt="image" src="https://github.com/user-attachments/assets/8ff9997c-06a7-4e68-9edd-b66b81b0d50f" />
   </div>

---

## 🛠️ Tech Stack
* **Core LLM**: DeepSeek-V3 / DeepSeek-R1

* **Agent Framework**: Agno (formerly Phidata)

* **Map API**: Amap (AutoNavi) Web Services

* **Search Engine**: DuckDuckGo Search

* **API Framework**: FastAPI

---

## 🚀 Getting Started
### 1. Installation

```bash  
Clone the repository
git clone https://github.com/your-username/DeepNav-Agent.git
cd DeepNav-Agent

Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

Install dependencies
pip install -r requirements.txt
```

### 2. Configuration
```bash 
Create a .env file in the root directory:

DEEPSEEK_API_KEY=your_deepseek_api_key_here
AMAP_API_KEY=your_amap_api_key_here
```

### 3. Run the Agent

```bash 
python3 main.py

Open http://localhost:8000/docs in your browser to start interacting via the Swagger UI.
```

---

## 🔍 Troubleshooting
### SSL Certificate Issues (macOS):
If you encounter SSL errors while installing duckduckgo-search, run:

```bash 
python3 -m pip install duckduckgo-search -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
```

### Environment Mismatch:
Always ensure your terminal shows (.venv) and which python3 points to your project folder.

---
## 🌟 Why DeepNav-Agent?
Standard Large Language Models (LLMs) are like "brilliant professors trapped in a library." They can talk about anything, but they are blind to the physical world, limited by training cutoffs, and cannot take real-world actions.

DeepNav-Agent transforms the DeepSeek "brain" into an "Autonomous Field Agent" with hands, eyes, and specialized expertise.

* **1. Grounded Reality vs. Digital Hallucinations**
Traditional AI often "hallucinates" when asked about specific locations or business trends. DeepNav-Agent eliminates this by using Amap (AutoNavi) as its Ground Truth. It doesn't guess where a shop is; it fetches the live coordinate, address, and status directly from the mapping engine.

* **2. Coordinated Expertise (The Team Advantage)**
While a single agent often gets confused when balancing complex tasks, DeepNav-Agent utilizes a Multi-Agent Orchestration strategy.

   * **The Geographic Analyst obsesses over spatial density and coordinates.**

    * **The Web Researcher hunts for real-time market sentiment.**

    * **The Orchestrator synthesizes these into a professional "Opening Guide" or "Market Analysis."**

* **3. Unified "Pal, Dash, & Scout" Architecture**
Built on the Agno Framework, DeepNav-Agent is designed to scale across three dimensions of intelligence within one single architecture:

    * **The Pal (Personalization): It learns your specific travel preferences and business criteria, evolving into a tailored digital twin.**

    * **The Dash (Data Intelligence): It performs autonomous "Site Selection Analysis" , calculating market saturation and traffic potential.**

    * **The Scout (Enterprise Context): It manages location-based knowledge, turning messy urban data into structured corporate insights.**

* **4. Autonomous Workflows, Not Just Conversations**
   DeepNav-Agent doesn't just reply to your message; it completes a structured workflow:

    * **Query Decomposition**: Breaks your "Opening a store" request into sub-tasks.

    * **Multi-Source Retrieval**: Calls Map APIs and Web Search simultaneously.

    * **Synthesis & Logic**: Cross-references physical locations with market news.

    * **Artifact Generation**: Automatically writes and saves the final report to your local file system (agent_notes.txt).

### 💡 The Bottom Line
DeepNav-Agent is built for the "Agentic Era." It is the bridge between the reasoning power of DeepSeek and the complexity of the physical world. It is a system that doesn't just tell you what to do—it does the work for you.

## 🗺️ Roadmap
* **[ ] Real-time Traffic**: Integrate live congestion data for dynamic routing.

* **[ ] Visual Mapping**: Export POI data to interactive HTML maps.

* **[ ] PDF Reporting**: Generate professional business analysis reports in PDF format.

* **[ ] Voice Interface**: Integration with voice-to-text for hands-free planning.

---

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐️ Support

If you find **DeepNav-Agent** helpful, please give it a **Star**! It’s the best way to support the development of more autonomous features.

## ⚠️ Disclaimer

This project is for educational and research purposes. Please ensure you comply with the Terms of Service of **DeepSeek** and **Amap (AutoNavi)** when using their respective APIs.

---

<p align="center">
  <b>Built with ❤️ by [huyyyyyy8233]</b><br>
  <i>Empowering the next generation of AI-Agentic Systems.</i>
</p>

<p align="center">
  <a href="#-deepnav-agent">Back to Top</a>
</p>
