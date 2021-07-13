from PIL import Image
import argparse
parser = argparse.ArgumentParser()

#定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width', type = int, default = 80)
parser.add_argument('--height', type = int, default = 80)

#解析并获取参数
args = parser.parse_args()

#输入的图片文件途径
IMG = args.file

#输出字符画宽度
WIDTH = args.width

#输出字符画高度
HEIGHT = args.height

#输出字符画的路径
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    #判断 alpha 值
    if alpha == 0:
        return ''

    #获取字符集的长度，这里是70
    length = len(ascii_char)

    gray = int(0.2126 * r + 0.7152 * g +0.0722 * b)
    
    uint = (256.0 + 1)/length

    return  ascii_char[int(gray/uint)]

if __name__ == '__main__':
    
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        
        txt += '\n'

    print(txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    
    else: 
        with open("output.txt",'w') as f:
            f.write(txt)
