import requests
import datetime
import random
import os
import string
import shutil

# 1. 实时天气 (免 Key 版)
def get_weather(city: str) -> str:
    """获取城市实时天气情况。"""
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url, timeout=5).json()
        current = response['current_condition'][0]
        temp = current['temp_C']
        desc = current.get('lang_zh', [{'value': current['weatherDesc'][0]['value']}])[0]['value']
        return f"{city} 当前天气：{desc}，气温 {temp}°C，湿度 {current['humidity']}%。"
    except:
        return f"暂时无法连接天气服务，请稍后再试。"

# 2. 金融工具：汇率转换
def currency_converter(amount: float, from_currency: str, to_currency: str) -> str:
    """转换货币汇率。例如：100 USD 转 CNY"""
    try:
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency.upper()}&to={to_currency.upper()}"
        res = requests.get(url, timeout=5).json()
        result = res['rates'][to_currency.upper()]
        return f"{amount} {from_currency} 等于 {result} {to_currency} (实时汇率)"
    except:
        return "汇率转换失败，请检查货币代码（如 USD, CNY, JPY）。"

# 3. 生产力：本地记事本
def save_note(content: str) -> str:
    """将重要信息记录到本地 agent_notes.txt 文件中。"""
    filename = "agent_notes.txt"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {content}\n")
    return f"✅ 已成功存入本地笔记：{filename}"

# 4. 安全工具：随机密码生成
def generate_password(length: int = 16) -> str:
    """生成一个包含大小写字母、数字和符号的高强度随机密码。"""
    length = max(length, 8)
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return f"已生成 {length} 位高强度密码：{password}"

# 5. 系统工具：检查磁盘空间 (Mac/Linux 适用)
def check_disk_usage() -> str:
    """检查当前电脑的磁盘空间使用情况。"""
    total, used, free = shutil.disk_usage("/")
    return f"磁盘总量: {total // (2**30)}GB, 已用: {used // (2**30)}GB, 剩余: {free // (2**30)}GB。"

# 6. 基础工具：时间与计算
def get_current_time() -> str:
    """获取当前精准的北京时间。"""
    return f"当前时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def calculator(expression: str) -> str:
    """执行数学运算。例如: '123 * (456 + 789)'"""
    try:
        # 仅允许基础数学运算，确保安全
        result = eval(expression, {"__builtins__": None}, {})
        return f"计算结果：{result}"
    except:
        return "数学运算格式错误。"

def get_poi_analysis(brand_name: str, city: str) -> str:
    """
    通过高德地图 API 搜索指定城市某品牌的店铺数据并进行初步分析。
    """
    api_key = "your-amap-api-key-here"
    url = f"https://restapi.amap.com/v3/place/text?keywords={brand_name}&city={city}&citylimit=true&output=json&key={api_key}"    
    
    try:
        response = requests.get(url, timeout=5).json()
        if response['status'] == '1':
            pois = response['pois']
            count = len(pois)
            # 提取前 3 个店的地址作为示例
            samples = [p['name'] + "(" + p['address'] + ")" for p in pois[:3]]
            sample_str = "\n".join(samples)
            
            return f"在 {city} 搜到 {brand_name} 相关店铺约 {count} 家。示例店铺：\n{sample_str}\n（数据已传回，请进行分析）"
        else:
            return "高德接口返回异常，请检查 Key 或参数。"
    except Exception as e:
        return f"调用高德 API 失败: {str(e)}"

# 别忘了把 get_poi_analysis 加入 available_tools 列表

# 导出工具列表
available_tools = [
    get_weather, 
    get_current_time, 
    currency_converter, 
    save_note, 
    generate_password,
    check_disk_usage,
    calculator,
    get_poi_analysis
]