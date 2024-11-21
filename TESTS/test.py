import cv2

from ultralytics import SAM


# 自動アノテーションで使用
from ultralytics.data.annotator import auto_annotate
from ultralytics.utils.plotting import colors

def sam_sample():
    """
    sam_sample
    ultralyticsのsam2実行テスト
    ポイントや領域で検出するオブジェクトを設定し、そのマスクを推論する。
    in : image file (.png .jpg or someting able to loading by cv2)
    out: segmentated mask image 
    """


    # Load a model
    model = SAM("models/sam2.1_b.pt")

    # Display model information (optional)
    model.info()

    # Run inference with bboxes prompt
    #results = model("./images/images.jpeg", bboxes=[100, 100, 200, 200])

    # Run inference with single point
    results = model("./TESTS/images/images.jpeg",points=[100, 50], labels=[1])

    # Run inference with multiple points
    #results = model(points=[[400, 370], [900, 370]], labels=[1, 1])

    # Run inference with multiple points prompt per object
    #results = model(points=[[[400, 370], [900, 370]]], labels=[[1, 1]])

    # Run inference with negative points prompt
    #results = model(points=[[[400, 370], [900, 370]]], labels=[[1, 0]])
    
    for result in results:
        result.show()

    



if '__main__' == __name__:
    sam_sample()