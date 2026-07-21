import csv

# 대구 지하철 역명 승하차 인원 분석
REAK_FILE = './대구교통공사_역별일별시간별 승하차인원_20171231.csv'

def load_real_csv(filename):
    """
    실제 공공데이터 파일을 읽어 딕셔너리/리스트로 변환
    
    DictReader() --> csv에서 첫줄 자동으로 키로 사용
    """
    # 파일 읽어오기
    with open(filename,'r', encoding='cp949') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
print()
print('='*50)
print('데이터 파일 읽기')
print('='*50)

# 함수 호출
real_data = load_real_csv(REAK_FILE)
print(f'{len(real_data):,}행')
print()
print('첫 3행')
for row in real_data[:3]:
    print({k: row[k] for k in ['월', '일','역명','승하','08시-09시','일계']})

def monthly_boarding(data):
    """
    월별 전체 승차 인원 합계를 집계하는 함수
    """
    monthly = {}
    for row in data:
        if row['승하'] == '승차':
            month = row['월']
            monthly[month] = monthly.get(month, 0) + int(row['일계'])
    return monthly

def top_stations(data, n=5):
    """
    연간 승차 합계 기준 상위 n개 반환
    """

    totals ={}
    for row in data:
        if row['승하'] == '승차':
            station = row['역명']
            totals[station] = totals.get(station, 0) + int(row['일계'])
    
    sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return sorted_totals[:n]

def boarding_by_line(data):
    """
    호선별 연간 승차 합계 집계
    """
    