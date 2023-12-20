from flask import Flask, request, jsonify
import base64
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/detect_face', methods=['POST'])
def detect_face():
    try:
        # Nhận dữ liệu hình ảnh từ Node.js
        data = request.get_json()
        image_data = data['image']

        # Giải mã hình ảnh từ base64
        image_np = np.frombuffer(base64.b64decode(image_data), dtype=np.uint8)
        image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        # Xử lý nhận diện khuôn mặt (đây chỉ là một ví dụ, bạn cần thêm mã của mình)
        # Ví dụ sử dụng OpenCV để vẽ một hình chữ nhật đơn giản
        cv2.rectangle(image, (50, 50), (150, 150), (0, 255, 0), 2)

        # Chuyển ảnh về base64 để gửi trả về Node.js
        _, img_encoded = cv2.imencode('.jpg', image)
        img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')

        # Trả về ảnh đã khoanh vùng cho Node.js
        return jsonify({'result_image': img_base64})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)