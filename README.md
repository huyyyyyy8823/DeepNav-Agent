🚀 DeepNav-Agent
Your DeepSeek-powered co-pilot for maps, web search, and real-world task automation.

🌟 Overview
DeepNav-Agent is an autonomous AI agent that bridges the gap between Large Language Models and the physical world. By integrating DeepSeek-V3 with the Amap (AutoNavi) Geolocation Engine and DuckDuckGo Web Search, it transforms abstract queries into real-world actions.

Whether you are analyzing business competition in a specific city district or planning a multi-stop business trip, DeepNav-Agent handles the research, spatial logic, and reporting automatically.

✨ Key Features
📍 Business Geography Intelligence: Perform POI (Point of Interest) analysis. Compare brand density, identify market gaps, and generate site selection reports.

🛣️ Smart Routing & Planning: Beyond simple directions. It solves complex multi-stop itineraries with optimized paths and arrival estimates using real-time map data.

🌐 Live Web Intelligence: Powered by DuckDuckGo to bypass LLM knowledge cutoffs. Get today's exchange rates, news, and market trends instantly.

📂 Automated Workflow: Seamlessly saves research findings and trip plans into local markdown notes (agent_notes.txt).

🛠️ Built-in Productivity Tools:

Financial: Real-time currency conversion.

Security: High-entropy random password generation.

System: Local disk space and resource monitoring.

📸 Showcase & Use Cases
🏙️ Business Analysis
Query: "Analyze the distribution of 'Luckin Coffee' vs 'Cotti Coffee' in Beijing Haidian District. Find the areas with the highest competition density."
Result: The agent fetches POI data, categorizes by business circles, and identifies "Red Oceans" for you.

✈️ Travel Planning
Query: "I'm visiting Hangzhou next week. Find the top 3 rated restaurants near West Lake, check the weather, and plan the best walking route from my hotel."
Result: A structured itinerary with restaurant details and a weather-optimized route saved to your notes.

🛠️ Tech Stack
Core LLM: DeepSeek-V3 / DeepSeek-R1

Agent Framework: Agno (formerly Phidata)

Map API: Amap (AutoNavi) Web Services

Search Engine: DuckDuckGo Search

API Framework: FastAPI

🚀 Getting Started
1. Installation
   
# Clone the repository
git clone https://github.com/your-username/DeepNav-Agent.git
cd DeepNav-Agent

# Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

2. Configuration
Create a .env file in the root directory:

DEEPSEEK_API_KEY=your_deepseek_api_key_here
AMAP_API_KEY=your_amap_api_key_here

3. Run the Agent

python3 main.py

Open http://localhost:8000/docs in your browser to start interacting via the Swagger UI.

🔍 Troubleshooting
SSL Certificate Issues (macOS):
If you encounter SSL errors while installing duckduckgo-search, run:

Bash
python3 -m pip install duckduckgo-search -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
Environment Mismatch:
Always ensure your terminal shows (.venv) and which python3 points to your project folder.

🗺️ Roadmap
[ ] Real-time Traffic: Integrate live congestion data for dynamic routing.

[ ] Visual Mapping: Export POI data to interactive HTML maps.

[ ] PDF Reporting: Generate professional business analysis reports in PDF format.

[ ] Voice Interface: Integration with voice-to-text for hands-free planning.

📄 License
Distributed under the MIT License. See LICENSE for more information.

🤝 Contributing
Contributions make the open-source community an amazing place to learn and create.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

Don't forget to give the project a star ⭐ if you find it useful!

Pro-tip for GitHub:
Add these tags to your repository settings to increase visibility:
ai-agent deepseek amap automation python geospatial-analysis llm
