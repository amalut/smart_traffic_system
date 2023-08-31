from flask import Flask, render_template
import cv2
import glob
from vehicle_detector import VehicleDetector
from screenshot import *
from ssDelete import *
import time
import keyboard

app = Flask(__name__)

vd = VehicleDetector()

i = 0

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/process')
def process():
    global i
    ss()
    vd = VehicleDetector()
    # Process lane 1
    results = []
    img = cv2.imread('static/Frame0.jpg')
    bike_boxes, car_boxes, bus_boxes = vd.detect_vehicles(img)
    bike_count = len(bike_boxes)
    car_count = len(car_boxes)
    bus_count = len(bus_boxes)

    # Display the detected vehicles on the image
    for box in bike_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
    for box in car_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
    for box in bus_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)

    results.append({
        'lane_number': 1,
        'bike_count': bike_count,
        'car_count': car_count,
        'bus_count': bus_count,
        # 'output_path': output_path
    })

    results1 = []
    img = cv2.imread('static/Frame1.jpg')
    bike_boxes1, car_boxes1, bus_boxes1 = vd.detect_vehicles(img)
    bike_count1 = len(bike_boxes1)
    car_count1 = len(car_boxes1)
    bus_count1 = len(bus_boxes1)

    # Display the detected vehicles on the image
    for box in bike_boxes1:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
    for box in car_boxes1:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
    for box in bus_boxes1:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
        # Append the results for the current lane to the results list
    results1.append({
        'lane_number': 2,
        'bike_count': bike_count1,
        'car_count': car_count1,
        'bus_count': bus_count1,
        # 'output_path': output_path
    })

    results2 = []
    img = cv2.imread('static/Frame2.jpg')
    bike_boxes2, car_boxes2, bus_boxes2 = vd.detect_vehicles(img)
    bike_count2 = len(bike_boxes2)
    car_count2 = len(car_boxes2)
    bus_count2 = len(bus_boxes2)

    # Display the detected vehicles on the image
    for box in bike_boxes2:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
    for box in car_boxes2:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
    for box in bus_boxes2:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
        # Append the results for the current lane to the results list
    results2.append({
        'lane_number': 3,
        'bike_count': bike_count2,
        'car_count': car_count2,
        'bus_count': bus_count2,
        # 'output_path': output_path
    })

    results3 = []
    img = cv2.imread('static/Frame3.jpg')
    bike_boxes3, car_boxes3, bus_boxes3 = vd.detect_vehicles(img)
    bike_count3 = len(bike_boxes3)
    car_count3 = len(car_boxes3)
    bus_count3 = len(bus_boxes3)

    # Display the detected vehicles on the image
    for box in bike_boxes3:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
    for box in car_boxes3:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
    for box in bus_boxes3:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.waitKey(1)
        # Append the results for the current lane to the results list
    results3.append({
        'lane_number': 4,
        'bike_count': bike_count3,
        'car_count': car_count3,
        'bus_count': bus_count3,
        # 'output_path': output_path
    })

    vc = bike_count * 1 + car_count * 3 + bus_count * 5
    vc1 = bike_count1 * 1 + car_count1 * 3 + bus_count1 * 5
    vc2 = bike_count2 * 1 + car_count2 * 3 + bus_count2 * 5
    vc3 = bike_count3 * 1 + car_count3 * 3 + bus_count3 * 5

    MIN_DURATION = 10
    MAX_DURATION = 100

    def calculate_duration(num_vehicles, green_lane):

        duration = (green_lane / (num_vehicles)) * 100  # Example linear mapping function
        return min(MAX_DURATION, max(MIN_DURATION, duration))

    def traffic_light_controller(x):

        duration_total = calculate_duration(vc + vc1 + vc2 + vc3, x)
        print(f"duration: {duration_total} seconds")
        print("Adjusting traffic light durations...")
        return duration_total


    durTime = traffic_light_controller(vc)
    durTime1 = traffic_light_controller(vc1)
    durTime2 = traffic_light_controller(vc2)
    durTime3 = traffic_light_controller(vc3)
    i = i + 1
    ssDel()

    # Render the template with the results
    return render_template('result.html', results=results, results1=results1, results2=results2, results3=results3, time=durTime, time1=durTime1, time2=durTime2, time3=durTime3, i=i)


if __name__ == '__main__':
    app.run(debug=True)
