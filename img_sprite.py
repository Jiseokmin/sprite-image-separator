from PIL import Image


def split_sprite_sheet(filename, sprite_width, sprite_height):
    # 스프라이트 시트 이미지 열기
    sheet = Image.open(filename)

    # 시트의 전체 크기 가져오기
    sheet_width, sheet_height = sheet.size

    # 스프라이트 개수 계산
    rows = sheet_height // sprite_height
    cols = sheet_width // sprite_width

    # 각 스프라이트 추출
    sprites = []
    for row in range(rows):
        for col in range(cols):
            # 스프라이트 위치 계산
            left = col * sprite_width
            top = row * sprite_height
            right = left + sprite_width
            bottom = top + sprite_height

            # 스프라이트 잘라내기
            sprite = sheet.crop((left, top, right, bottom))
            sprites.append(sprite)

            # 개별 파일로 저장
            sprite.save(f"sprite_{row}_{col}.png")

    return sprites


# 사용 예시
split_sprite_sheet("ico_flag.png", 176, 128)  # 32x32 크기의 스프라이트
