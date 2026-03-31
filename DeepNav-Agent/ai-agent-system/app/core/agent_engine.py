import os
from agno.agent import Agent
from agno.team import Team
from agno.models.deepseek import DeepSeek
from .tools import available_tools

# 尝试导入联网搜索工具
try:
    from agno.tools.duckduckgo import DuckDuckGoTools
except ImportError:
    DuckDuckGoTools = None

class AgentOrchestrator:
    def __init__(self):
        # 1. 获取 API Key
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            print("❌ 错误：未在环境变量中发现 DEEPSEEK_API_KEY！")

        # 2. 初始化工具
        search_tool = None
        if DuckDuckGoTools is not None:
            try:
                search_tool = DuckDuckGoTools()
                print("✅ 联网搜索功能已就绪")
            except Exception as e:
                print(f"⚠️ 联网工具初始化失败: {e}")

        # 3. 定义【地理分析专家】 (Focus: Amap/Maps)
        # 它专门负责处理 POI 搜索、路线规划等空间任务
        geo_agent = Agent(
            name="Geographic Analyst",
            role="空间智慧专家，擅长利用地图数据进行商业选址分析和路线优化",
            model=DeepSeek(id="deepseek-chat", api_key=api_key),
            tools=available_tools, # 这里放你的高德地图、计算器等本地工具
            instructions=[
                "1. 你是团队中的地理大脑，所有涉及位置、POI 搜索、距离计算的任务由你主导。",
                "2. 当用户提到某个地点时，优先调用高德 API 获取真实数据。",
                "3. 你需要为团队提供精准的坐标和空间逻辑支持。"
            ],
        )

        # 4. 定义【全网调研专家】 (Focus: Search/News)
        # 它专门负责抓取最新的市场动态、汇率、新闻
        researcher_agent = Agent(
            name="Web Researcher",
            role="实时情报专家，擅长从互联网抓取最新的资讯、评价和行业趋势",
            model=DeepSeek(id="deepseek-chat", api_key=api_key),
            tools=[search_tool] if search_tool else [],
            instructions=[
                "1. 你负责填补模型知识的空白，所有实时新闻、品牌评价、最新汇率由你抓取。",
                "2. 优先调用联网搜索工具，确保信息的时效性。",
                "3. 你的任务是为地理分析结果提供背景支撑（例如：该路段最近的新闻动向）。"
            ],
        )

        # 5. 组建【DeepNav Team】领队
        # 它是最终与用户对话的出口，负责汇总两个专家的情报
        self.team = Team(
            members=[geo_agent, researcher_agent],
            model=DeepSeek(id="deepseek-chat", api_key=api_key),
            instructions=[
                "1. 你是 DeepNav-Agent 团队的领队，负责协调地理专家和调研专家。",
                "2. 你的回复必须是中文，语气专业干练。",
                "3. 流程：先让地理专家拿空间数据，再让调研专家补全背景，最后由你汇总输出。",
                "4. 只有在用户明确要求保存时，才调用 save_note 记录信息。",
                "5. 严禁编造数据，必须基于两个专家的返回结果进行深度洞察。",
                "6. 每一份回复都要体现出‘数据分析报告’的高级感。"
            ],
            markdown=True
        )

    def process_request(self, query: str) -> str:
        """
        处理用户请求：现在是整个团队在响应！
        """
        try:
            # 运行 Team 并获取响应
            response = self.team.run(query)
            return response.content
        except Exception as e:
            error_msg = f"❌ 团队运行异常: {str(e)}"
            print(error_msg)
            return "抱歉，我的专家团队目前正在开会（技术故障），请稍后再试。"