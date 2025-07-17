import requests
import json
import datetime
import os

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Referer": "https://top.baidu.com/board?tab=realtime",
    }

def fetch_baidu_hot_search():
    """获取百度热搜数据并保存为JSON文件"""
    url = "https://top.baidu.com/board?tab=realtime"
    

    try:
        print(f"正在请求URL: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        
        print(f"HTTP状态码: {response.status_code}")
        print(f"响应长度: {len(response.text)} 字符")
        
        # 保存原始响应到文件（用于调试）
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        debug_filename = f"debug_response_{timestamp}.html"
        
        # 获取当前工作目录
        current_dir = os.getcwd()
        print(f"当前工作目录: {current_dir}")
        
        # 完整调试文件路径
        debug_path = os.path.join(current_dir, debug_filename)
        print(f"调试文件将保存到: {debug_path}")
        
        try:
            with open(debug_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"已保存原始响应到: {debug_path}")
        except Exception as e:
            print(f"保存调试文件失败: {str(e)}")
        
        # 检查是否是有效JSON
        if response.text.strip().startswith(("{", "[")):
            try:
                json_data = response.json()
                print("成功解析为JSON")
                return json_data
            except json.JSONDecodeError as e:
                print(f"JSON解析错误: {e}")
                print(f"错误位置: line {e.lineno}, column {e.colno} (char {e.pos})")
                print(f"上下文: {e.doc[e.pos-30:e.pos+30]}")
        else:
            print("响应不是有效的JSON格式")
            print("响应开头内容:")
            print(response.text[:200])
        
        return None
            
    except Exception as e:
        print(f"获取数据出错: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def parse_baidu_hot_search(data):
    """解析百度热搜json数据"""
    hot_list = []
    
    #提取实时热点卡片
    realtime_cards = next(
        (card for card in data['data']['cards'] if card['type'] == 'realtime'),
        None
        )

    if not realtime_cards:
        print("No realtime cards found in the data.")
        return hot_list

    #处理每个热搜项
    for item in realtime_cards['card_group']:
        if item.get("show")!= 1:
            continue

        hot_list.append({
            "rank": item.get("rank", 0),
            "title": item.get("title", ""),
            "hot_score": int(item.get("hot_score", "0")) if item.get("hot_score") else 0,
            "trend": item.get("hotChange", ""),
            "desc": item.get("desc", ""),
            "query": item.get("query", ""),
            "url": item.get("url", ""),
            "icon_url": item.get("icon_url", ""),
            "timetamp": datetime.now().isoformat()
        })
       
    return hot_list

def save_to_json(data, filename='baidu_hot_search.json'):
    """将数据保存为JSON文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")
    
if __name__ == "__main__":
    hot_data = fetch_baidu_hot_search()
    if hot_data:
        #保存原始json数据
        save_to_json(hot_data, "D:/code/python_program/PQSHUJU/baidu_hot_search_raw.json")

        #解析数据并结构化数据
        hot_data = parse_baidu_hot_search(hot_data)
        if hot_data:
            #保存结构化数据
            save_to_json(hot_data, "D:/code/python_program/PQSHUJU/baidu_hot_search.json")
        else:
            print("No hot search data found.")

        #打印前10条热搜数据
        print("\nTop 10 Baidu Hot Searches:")
        for i, item in enumerate(hot_data[:10], start=1):
            trend_icon = "↑" if item['trend'] == "up" else "↓" if item['trend'] == "down" else ""
            print(f"{item['rank']}.{trend_icon} {item['title']} - 热度: {item['hot_score']} - 描述: {item['desc']}")
            print(f"链接: {item['url']}")
    print("数据抓取完成。")
        
