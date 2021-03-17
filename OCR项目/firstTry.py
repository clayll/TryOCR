




## 显示原图，读取名称为11.jpg的测试图像
## img_path= "./imgs/11.jpg"
## img = Image.open(img_path)
## plt.figure("test_img", figsize=(10,10))
## plt.imshow(img)
## plt.show()


# import paddle;

# paddle.utils.run_check()
"""
from paddleocr import PaddleOCR
# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, lang="ch") # need to run only once to download and load model into memory
img_path= "./imgs/11.jpg"
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)
"""

from paddleocr import PaddleOCR, draw_ocr

def distinguish(img_path="./imgs/11.jpg"):
    # 模型路径下必须含有model和params文件
    ocr = PaddleOCR(det_model_dir='./model/ch_ppocr_mobile_v2.0_det_infer',
                    rec_model_dir='./model/ch_ppocr_mobile_v2.0_rec_infer',

                    cls_model_dir='./model/ch_ppocr_mobile_v2.0_cls_infer',
                    use_angle_cls=True)

    result = ocr.ocr(img_path, cls=True)
    for line in result:
        print(line)


    # 显示结果
    from PIL import Image
    image = Image.open(img_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores)
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')

distinguish(r".\flask\static\1.png")
