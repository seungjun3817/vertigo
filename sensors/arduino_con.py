import serial
import json

# 아두이노와 연결된 시리얼 포트 설정 (예: COM3 또는 /dev/ttyUSB0 등)
arduino_port = '/dev/ttyACM0'  # Windows의 경우 'COM3' 또는 아두이노 포트를 설정
baud_rate = 9600  # 아두이노와 동일한 baud_rate 설정

# 시리얼 포트 열기
ser = serial.Serial(arduino_port, baud_rate)

# 시리얼 데이터를 읽고 처리
try:
    while True:
        # 시리얼 포트에서 한 줄을 읽음
        line = ser.readline().decode('utf-8').strip()

        if line:  # 빈 줄을 건너뜀
            print("Received data:", line)

            # JSON 데이터인 경우 처리
            try:
                json_data = json.loads(line)
                latitude = json_data.get('latitude', None)
                longitude = json_data.get('longitude', None)

                if latitude and longitude:
                    print(f"Latitude: {latitude}, Longitude: {longitude}")
            except json.JSONDecodeError:
                print("Received non-JSON data:", line)
        
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
finally:
    ser.close()  # 시리얼 포트 닫기
