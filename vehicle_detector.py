import cv2

class VehicleDetector:

    def __init__(self):
        net = cv2.dnn.readNet("dnn_model/yolov4.weights", "dnn_model/yolov4.cfg")
        self.model = cv2.dnn_DetectionModel(net)
        self.model.setInputParams(size=(832, 832), scale=1 / 255)


        self.classes_allowed = [2, 3, 5, 7]
        #2car
        #3motorbike
        #5bus
        #7truck


    def detect_vehicles(self, img):
        vehicles_boxes = []
        vehicles_boxes1 = []
        vehicles_boxes2 = []

        class_ids, scores, boxes = self.model.detect(img, nmsThreshold=0.4)
        for class_id, score, box in zip(class_ids, scores, boxes):
            if score < 0.5:

                continue


            if class_id == 3:
                vehicles_boxes.append(box)

            if class_id == 2:
                vehicles_boxes1.append(box)

            if class_id == 5:
                vehicles_boxes2.append(box)

            if class_id == 7:
                vehicles_boxes2.append(box)

        return vehicles_boxes, vehicles_boxes1, vehicles_boxes2

