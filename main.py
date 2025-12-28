import FinanceDataReader as fdr
import datetime

# 오늘 날짜 구하기
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    # 삼성전자(005930) 데이터 가져오기
    df = fdr.DataReader('005930')
    latest = df.iloc[-1]
    
    price = int(latest['Close'])
    
    # HTML 내용 만들기
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>자동 주식 분석</title>
    </head>
    <body>
        <h1>📈 삼성전자 실시간 분석</h1>
        <h2>현재가: {price:,}원</h2>
        <p>업데이트 시간: {now}</p>
    </body>
    </html>
    """

except Exception as e:
    html_content = f"<h1>에러 발생!</h1><p>{e}</p>"

# 파일로 저장하기
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"업데이트 완료! 삼성전자 가격: {price}")
