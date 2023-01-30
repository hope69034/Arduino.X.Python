from Arduino import Arduino
import time
board = Arduino('115200') # 아두이노 포트 번호 115200 (다른파일코드분석필요)
board.pinMode(9, "OUTPUT")    # 9 : 아웃풋 핀은 디지털 9핀, 핀모드로 출력핀 선언
while True:
    board.digitalWrite(9,"HIGH")   # 9핀에 HIGH로 최대 전압을 걸어준다 즉 led on  
    time.sleep(3)                 # 3초 딜레이 (파이썬 타임슬립은 초 단위.) 
    board.digitalWrite(9,"LOW")   # 9핀에 LOW로 전압 0을 걸어준다 즉 led off  
    time.sleep(1)                 # 1초 딜레이
