import FinanceDataReader as fdr
import datetime

# 1. 한국 주식 데이터 가져오기 (예: 삼성전자 005930)
# 날짜: 오늘
today = datetime.date.today().strftime("%Y-%m-%d")
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    # 삼성전자(005930)의 최근 데이터를 가져옴
    df = fdr.DataReader('005930') # 2024년 데이터부터
    latest = df.iloc[-1] # 가장 최신 데이터
    
    price = int(latest['Close']) # 종가
    
    # 등락률 계산 (데이터에 'Change' 컬럼이 없으면 전일 대비로 계산)
    if 'Change' in latest:
        change = latest['Change'] * 100
    else:
        # Change 컬럼이 없을 경우 직접 계산 (전일 종가 대비)
        yesterday = df.iloc[-2]
        change = ((price - int(yesterday['Close'])) / int(yesterday['Close'])) * 100
    
    # 등락률에 따른 이모지 설정
    if change > 0:
        emoji = "🔺"
        color = "red"
    elif change < 0:
        emoji = "QAQ" # 파란색 눈물
        color = "blue"
    else:
        emoji = "➖"
        color = "black"
        
    stock_info = f"""
    <h2>삼성전자 (005930)</h2>
    <p>기준일: {today}</p>
    <h3 style="color:{color};">현재가: {price:,}원 ({emoji} {change:.2f}%)</h3>
    """

except Exception as e:
    stock_info = f"<p>데이터를 가져오는데 실패했어요: {e}</p>"

# 2. HTML 파일 만들기
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>오늘의 주식 분석</title>
    <style>
        body {{ font-family: sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .card {{ border: 1px solid #ddd; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .footer {{ margin-top: 50px; font-size: 0.8em; color: #888; }}
    </style>
</head>
<body>
    <h1>📈 AI 주식 자동 분석 리포트</h1>
    <div class="card">
        {stock_info}
    </div>
    
    <div class="footer">
        <p>이 글은 파이썬 로봇이 <strong>{now}</strong>에 자동으로 작성했습니다.</p>
    </div>
</body>
</html>
"""

# 3. index.html 파일 덮어쓰기
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"블로그 업데이트 완료! 삼성전자 현재가: {price:,}원")
