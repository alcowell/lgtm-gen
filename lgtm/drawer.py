from PIL import Image, ImageDraw, ImageFont


# 画像全体に対するメッセージの割合
MAX_RATIO = 0.8

# フォント関連の定数
FONT_MAX = 246
FONT_MIN = 4

# フォントの格納先とカラー
FONT_NAME = 'resource/Fonts/arialbd.ttf'
FONT_COLOR = (255, 255, 255, 0)

# 出力関連
OUT_NAME = 'output.png'
OUT_TYPE = 'PNG'


def save_with_message(fp, message):
    image = Image.open(fp)
    drawer = ImageDraw.Draw(image)
    image_width, image_height = image.size
    message_width = image_width * MAX_RATIO
    message_height = image_height * MAX_RATIO

    for font_size in range(FONT_MAX, FONT_MIN, -1):
        font = ImageFont.truetype(font=FONT_NAME, size=font_size)
        text_width, text_height = drawer.textsize(text=message, font=font)
        w = message_width - text_width
        h = message_height - text_height

        if w > 0 and h > 0:
            position = ((image_width - text_width)/2,
                        (image_height-text_height)/2)
            # メッセージの描画
            drawer.text(xy=position, text=message, font=font, fill=FONT_COLOR)
            break

    image.save(OUT_NAME, OUT_TYPE)
