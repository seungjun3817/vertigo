# 최대 10개의 데이터만 저장할 리스트
recent_data = []

# 기울기 변화 임계값
threshold_change = 30

# 가상 센서 데이터 (실제로는 이 부분이 센서 입력으로 바뀜)
sensor_stream = [
    {'X': 1, 'Y': 2, 'Z': 85},
    {'X': 2, 'Y': 3, 'Z': 84},
    {'X': 3, 'Y': 4, 'Z': 83},
    {'X': 4, 'Y': 5, 'Z': 82},
    {'X': 5, 'Y': 6, 'Z': 81},
    {'X': 6, 'Y': 7, 'Z': 80},
    {'X': 7, 'Y': 8, 'Z': 79},
    {'X': 8, 'Y': 9, 'Z': 78},
    {'X': 9, 'Y': 10, 'Z': 77},
    {'X': 40, 'Y': 50, 'Z': 100},  # 10번째
    {'X': 43, 'Y': 55, 'Z': 110},  # 11번째 -> 첫 번째 데이터 제거
    {'X': 44, 'Y': 55, 'Z': 120},  # 12번째 -> 두 번째 데이터 제거
]


# 실시간 데이터 수집 및 최근 10개 유지
for data in sensor_stream:
    # 새 데이터 추가
    recent_data.append(data)
    
    # 리스트 크기가 10을 초과하면 가장 오래된 데이터 제거
    if len(recent_data) > 10:
        recent_data.pop(0)

    # 최근 기울기 데이터 출력
    print("최근 기울기 데이터:")
    magnitudes = []  # 벡터 크기를 저장할 리스트
    for i, d in enumerate(recent_data):
        # 벡터 크기 계산: sqrt(X^2 + Y^2 + Z^2)
        magnitude = (d['X']**2 + d['Y']**2 + d['Z']**2)**0.5
        magnitudes.append(magnitude)
        print(f"{i + 1}. X: {d['X']}, Y: {d['Y']}, Z: {d['Z']} | Magnitude: {magnitude:.2f}")

    # 기울기 변화량 확인 (10개 안에서, 경고는 한 번만 출력)
    alert_triggered = False
    for i in range(len(magnitudes)):
        for j in range(i + 1, len(magnitudes)):
            difference = abs(magnitudes[i] - magnitudes[j])
            if difference > threshold_change:
                alert_triggered = True
                break
        if alert_triggered:
            break

    # 경고 메시지 출력
    if alert_triggered:
        print("경고: 기울기 변화 발생!")

    print("-" * 40)  # 데이터 구분선
