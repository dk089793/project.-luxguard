# 빛의 세기 임계값 (0 ~ 1023 범위)
THRESHOLD = 700  # 이 값보다 빛이 강하면 경고

def check_light_intensity():
    while True:
        try:
            # 사용자로부터 빛의 세기 입력 받기
            light_value = int(input("빛의 세기를 입력하세요 (0 ~ 1023): "))
            
            if light_value < 0 or light_value > 1023:
                print("잘못된 값입니다. 0부터 1023 사이의 값을 입력해주세요.")
                continue      # 입력된 값에 대한 설명 출력
            if light_value <= 100:
                print("입력된 빛의 세기: 매우 어두운 환경 (밤, 불 꺼진 방 등)")
            elif light_value <= 300:
                print("입력된 빛의 세기: 어두운 실내 (커튼 쳐진 방 등)")
            elif light_value <= 500:
                print("입력된 빛의 세기: 어두운 실내 조명 (약간의 빛)")
            elif light_value <= 700:
                print("입력된 빛의 세기: 표준 실내 조명 (일반적인 실내 환경)")
            elif light_value <= 900:
                print("입력된 빛의 세기: 밝은 실내 환경 (밝은 사무실 또는 카페)")
            else:
                print("입력된 빛의 세기: 매우 밝은 환경 (직사광선, 햇볕이 강한 환경)")
            # 빛의 세기가 임계값을 초과하면 경고 출력
            if light_value > THRESHOLD:
                print("경고: 빛의 세기가 너무 강합니다!")
            else:
                print("빛의 세기가 정상 범위입니다.")
        
        except ValueError:
            print("유효하지 않은 입력입니다. 정수를 입력해주세요.")

# 프로그램 실행
check_light_intensity()
