from PIL import Image, ImageDraw
import pyscreenshot as ImageGrab  # pyscreenshot을 사용하여 화면 캡쳐

# 캡쳐할 부분의 좌표
x1, y1, x2, y2 = 100, 100, 300, 300

# 화면 캡쳐
screenshot = ImageGrab.grab()

# 이미지에 테두리 그리기
draw = ImageDraw.Draw(screenshot)
draw.rectangle([x1, y1, x2, y2], outline="red", width=2)  # 테두리 색상 및 두께 설정

# 이미지 표시
screenshot.show()

# 캡쳐 영역 저장
# captured_region = screenshot.crop((x1, y1, x2, y2))
# captured_region.save('captured_region.png')
