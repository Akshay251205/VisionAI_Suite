import streamlit as st
import os
import cv2
import numpy as np

# Safe import for MediaPipe to ensure robust startup
try:
    import mediapipe as mp
    MP_AVAILABLE = True
except ImportError:
    MP_AVAILABLE = False

# 1. Page Configuration
st.set_page_config(
    page_title="VisionAI Suite - Advanced Computer Vision Hub",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Animated Background and Glassmorphism Cards
st.markdown("""
<style>
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e1b4b, #311042, #0f172a);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: #f8fafc;
}

.vision-card {
    background: rgba(30, 41, 59, 0.85);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    height: 100%;
}

.vision-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(99, 102, 241, 0.35);
    border-color: rgba(99, 102, 241, 0.6);
}

.card-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #818cf8;
    margin-bottom: 12px;
}

.task-badge {
    background: rgba(99, 102, 241, 0.25);
    color: #c7d2fe;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
    margin: 3px;
    border: 1px solid rgba(99, 102, 241, 0.4);
}

.main-title {
    text-align: center;
    font-size: 2.8rem;
    font-weight: 900;
    background: linear-gradient(135deg, #818cf8 0%, #c084fc 50%, #f472b6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 1.15rem;
    margin-bottom: 35px;
}
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<h1 class="main-title">🚀 VisionAI OpenCV Hub</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Powered by OpenCV, MediaPipe, & Streamlit</p>', unsafe_allow_html=True)

if not MP_AVAILABLE:
    st.error("⚠️ MediaPipe package is not installed. Please run pip install mediapipe opencv-python-headless in your terminal.")

# Sidebar Control Center
with st.sidebar:
    st.title("Control Center")
    selected_mode = st.radio(
        "Select Active Module",
        ["✨ Overview (All 3 Cards)", "🖱️ Card 1: Cursor Control (8 Tasks)", "✍️ Card 2: Air Writing OCR", "🧘 Card 3: Posture Detection"]
    )
    st.markdown("---")
    st.markdown("### 🛠️ Instructions")
    st.write("1. Run: streamlit run app.py")
    st.write("2. Open in Google Chrome.")
    st.write("3. Enable camera permissions.")

# Layout: 3 Header & 3 Cards Overview
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="vision-card">
        <div class="card-title">🖱️ 1. Cursor Control</div>
        <p style="color: #cbd5e1; font-size: 0.9rem;">
            Maps hand landmark coordinates via OpenCV & MediaPipe Hands for touchless cursor navigation.
        </p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 15px 0;">
        <p style="font-weight: 600; color: #a5b4fc; font-size: 0.85rem; margin-bottom: 8px;">8 Supported Tasks:</p>
        <div>
            <span class="task-badge">1. Move Cursor</span>
            <span class="task-badge">2. Left Click</span>
            <span class="task-badge">3. Right Click</span>
            <span class="task-badge">4. Double Click</span>
            <span class="task-badge">5. Scroll Mode</span>
            <span class="task-badge">6. Drag & Drop</span>
            <span class="task-badge">7. Screenshot</span>
            <span class="task-badge">8. Volume Control</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="vision-card">
        <div class="card-title">✍️ 2. Air Writing</div>
        <p style="color: #cbd5e1; font-size: 0.9rem;">
            Tracks index finger trajectory in real-time video frames to draw strokes and recognize characters.
        </p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 15px 0;">
        <p style="font-weight: 600; color: #a5b4fc; font-size: 0.85rem; margin-bottom: 8px;">Key Capabilities:</p>
        <div>
            <span class="task-badge">Finger Tracking</span>
            <span class="task-badge">Air Canvas</span>
            <span class="task-badge">Stroke Smoothing</span>
            <span class="task-badge">Character OCR</span>
            <span class="task-badge">Clear & Save</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="vision-card">
        <div class="card-title">🧘 3. Posture Monitor</div>
        <p style="color: #cbd5e1; font-size: 0.9rem;">
            Utilizes MediaPipe Pose estimation to analyze shoulder balance and spine inclination angles.
        </p>
        <hr style="border-color: rgba(255,255,255,0.1); margin: 15px 0;">
        <p style="font-weight: 600; color: #a5b4fc; font-size: 0.85rem; margin-bottom: 8px;">Key Capabilities:</p>
        <div>
            <span class="task-badge">Spine Alignment</span>
            <span class="task-badge">Shoulder Level</span>
            <span class="task-badge">Slouch Alert</span>
            <span class="task-badge">Angle Metrics</span>
            <span class="task-badge">Live Status</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Interactive Computer Vision Modules
if selected_mode == "🖱️ Card 1: Cursor Control (8 Tasks)":
    st.markdown("## 🖱️ Card 1: AI Hand Gesture Cursor Control")
    st.write("Capture a frame from your webcam to process hand landmarks and simulate mouse control gestures.")
    
    img_file = st.camera_input("Take a photo for Hand Tracking (Cursor Control)")
    if img_file is not None and MP_AVAILABLE:
        # Convert image buffer to OpenCV array
        bytes_data = img_file.getvalue()
        cv_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        
        # Process with MediaPipe Hands
        mp_hands = mp.solutions.hands
        mp_drawing = mp.solutions.drawing_utils
        
        with mp_hands.Hands(static_image_mode=True, max_num_hands=1, min_detection_confidence=0.7) as hands:
            rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_img)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(cv_img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    # Extract Index Finger Tip (Landmark 8) and Thumb Tip (Landmark 4)
                    h, w, _ = cv_img.shape
                    ix, iy = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)
                    tx, ty = int(hand_landmarks.landmark[4].x * w), int(hand_landmarks.landmark[4].y * h)
                    
                    cv2.circle(cv_img, (ix, iy), 10, (0, 255, 0), -1)
                    cv2.circle(cv_img, (tx, ty), 10, (255, 0, 0), -1)
                    
                    distance = np.sqrt((ix - tx)*2 + (iy - ty)*2)
                    click_status = "PINCH / CLICK DETECTED" if distance < 40 else "MOVING CURSOR"
                    
                    cv2.putText(cv_img, click_status, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            else:
                cv2.putText(cv_img, "No Hands Detected", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                
        st.image(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB), channels="RGB", caption="Processed Hand Tracking Frame")
        st.success("Hand landmark mapping and gesture check complete!")

elif selected_mode == "✍️ Card 2: Air Writing OCR":
    st.markdown("## ✍️ Card 2: Live Air Writing & Character Recognition")
    st.write(
        "Write in the air using your index finger. Raise your index finger and "
        "fold your middle finger to draw. Extend your middle finger to pause."
    )

    # Live webcam support is provided by Streamlit-WebRTC.
    try:
        from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
        import av
        import threading
        from collections import deque

        LIVE_WRITING_AVAILABLE = True
    except ImportError:
        LIVE_WRITING_AVAILABLE = False

    # The OCR model is optional. The live drawing canvas works without TensorFlow.
    @st.cache_resource
    def load_air_ocr_model():
        model_path = "air_ocr_model.keras"
        if not os.path.exists(model_path):
            return None
        try:
            from tensorflow import keras
            return keras.models.load_model(model_path)
        except Exception as exc:
            st.warning(f"OCR model could not be loaded: {exc}")
            return None

    def prepare_air_canvas_for_ocr(canvas):
        """Prepare a white-on-black drawing as a centered 28x28 grayscale image."""
        gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        binary = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)[1]
        coords = cv2.findNonZero(binary)

        if coords is None:
            return None

        x, y, width, height = cv2.boundingRect(coords)
        cropped = gray[y:y + height, x:x + width]

        if cropped.size == 0:
            return None

        scale = 20.0 / max(width, height)
        new_width = max(1, int(round(width * scale)))
        new_height = max(1, int(round(height * scale)))
        resized = cv2.resize(
            cropped, (new_width, new_height), interpolation=cv2.INTER_AREA
        )

        image_28 = np.zeros((28, 28), dtype=np.uint8)
        x_offset = (28 - new_width) // 2
        y_offset = (28 - new_height) // 2
        image_28[
            y_offset:y_offset + new_height,
            x_offset:x_offset + new_width
        ] = resized

        image_28 = image_28.astype("float32") / 255.0
        return image_28.reshape(1, 28, 28, 1)

    if not MP_AVAILABLE:
        st.error("MediaPipe is not installed. Install the packages listed in requirements.txt.")
    elif not LIVE_WRITING_AVAILABLE:
        st.error(
            "Live webcam writing needs Streamlit-WebRTC and PyAV. "
            "Install them with: pip install streamlit-webrtc av"
        )
    else:
        CANVAS_WIDTH = 640
        CANVAS_HEIGHT = 480

        class AirWritingProcessor(VideoProcessorBase):
            def _init_(self):
                self.lock = threading.Lock()
                self.hands = mp.solutions.hands.Hands(
                    static_image_mode=False,
                    max_num_hands=1,
                    model_complexity=1,
                    min_detection_confidence=0.65,
                    min_tracking_confidence=0.65,
                )
                self.canvas = np.zeros(
                    (CANVAS_HEIGHT, CANVAS_WIDTH, 3), dtype=np.uint8
                )
                self.point_history = deque(maxlen=5)
                self.last_status = "Show your hand"

            def clear_canvas(self):
                with self.lock:
                    self.canvas[:] = 0
                    self.point_history.clear()

            def get_canvas_copy(self):
                with self.lock:
                    return self.canvas.copy()

            def recv(self, frame):
                camera_image = frame.to_ndarray(format="bgr24")
                camera_image = cv2.flip(camera_image, 1)
                image_height, image_width = camera_image.shape[:2]

                rgb_image = cv2.cvtColor(camera_image, cv2.COLOR_BGR2RGB)
                results = self.hands.process(rgb_image)

                status = "No hand detected - show your hand"

                if results.multi_hand_landmarks:
                    hand_landmarks = results.multi_hand_landmarks[0]

                    mp.solutions.drawing_utils.draw_landmarks(
                        camera_image,
                        hand_landmarks,
                        mp.solutions.hands.HAND_CONNECTIONS,
                    )

                    landmarks = hand_landmarks.landmark
                    index_tip = landmarks[8]
                    index_pip = landmarks[6]
                    middle_tip = landmarks[12]
                    middle_pip = landmarks[10]

                    finger_x = int(index_tip.x * image_width)
                    finger_y = int(index_tip.y * image_height)

                    cv2.circle(
                        camera_image,
                        (finger_x, finger_y),
                        9,
                        (255, 0, 255),
                        -1,
                    )

                    # Draw gesture: index finger extended, middle finger folded.
                    index_is_up = index_tip.y < index_pip.y
                    middle_is_folded = middle_tip.y > middle_pip.y
                    is_drawing = index_is_up and middle_is_folded

                    if is_drawing:
                        canvas_x = int(finger_x * CANVAS_WIDTH / image_width)
                        canvas_y = int(finger_y * CANVAS_HEIGHT / image_height)
                        current_point = (canvas_x, canvas_y)
                        self.point_history.append(current_point)

                        # Smooth the path by averaging the recent fingertip positions.
                        points = list(self.point_history)
                        smooth_x = int(sum(p[0] for p in points) / len(points))
                        smooth_y = int(sum(p[1] for p in points) / len(points))
                        smooth_point = (smooth_x, smooth_y)

                        with self.lock:
                            if len(points) >= 2:
                                previous_points = points[:-1]
                                previous_x = int(
                                    sum(p[0] for p in previous_points)
                                    / len(previous_points)
                                )
                                previous_y = int(
                                    sum(p[1] for p in previous_points)
                                    / len(previous_points)
                                )
                                cv2.line(
                                    self.canvas,
                                    (previous_x, previous_y),
                                    smooth_point,
                                    (255, 255, 255),
                                    6,
                                    cv2.LINE_AA,
                                )

                        status = "WRITING - index up, middle finger folded"
                    else:
                        self.point_history.clear()
                        status = "PAUSED - fold middle finger to write"

                cv2.putText(
                    camera_image,
                    status,
                    (12, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    (0, 255, 255),
                    2,
                    cv2.LINE_AA,
                )

                with self.lock:
                    canvas_view = self.canvas.copy()

                canvas_view = cv2.resize(
                    canvas_view, (image_width, image_height)
                )
                combined = cv2.hconcat([camera_image, canvas_view])
                cv2.putText(
                    combined,
                    "AIR WRITING CANVAS",
                    (image_width + 12, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )

                return av.VideoFrame.from_ndarray(
                    combined, format="bgr24"
                )

        st.markdown(
            "*Gesture:* Keep your index finger raised and fold your middle "
            "finger to draw. Extend the middle finger to pause."
        )

        ocr_model = load_air_ocr_model()
        if ocr_model is None:
            st.info(
                "Live air writing is available. To enable A-Z recognition, "
                "train the optional OCR model using python train_ocr.py "
                "and place air_ocr_model.keras beside this app.py file."
            )
        else:
            st.success("A-Z OCR model loaded successfully.")

        webrtc_context = webrtc_streamer(
            key="visionai-air-writing",
            video_processor_factory=AirWritingProcessor,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )

        clear_col, recognize_col = st.columns(2)

        with clear_col:
            if st.button("🧹 Clear Writing Canvas", use_container_width=True):
                if webrtc_context.video_processor is not None:
                    webrtc_context.video_processor.clear_canvas()
                    st.success("Canvas cleared.")

        with recognize_col:
            recognize_button = st.button(
                "🔎 Recognize Character",
                use_container_width=True,
                disabled=(
                    ocr_model is None
                    or webrtc_context.video_processor is None
                ),
            )

        if recognize_button and webrtc_context.video_processor is not None:
            current_canvas = webrtc_context.video_processor.get_canvas_copy()
            model_input = prepare_air_canvas_for_ocr(current_canvas)

            if model_input is None:
                st.warning("The canvas is empty. Write a character first.")
            else:
                try:
                    probabilities = ocr_model.predict(model_input, verbose=0)[0]
                    predicted_index = int(np.argmax(probabilities))
                    predicted_character = chr(ord("A") + predicted_index)
                    confidence = float(probabilities[predicted_index]) * 100

                    st.success(f"Predicted character: {predicted_character}")
                    st.metric("Model confidence", f"{confidence:.1f}%")
                    st.caption(
                        "This is the model's predicted probability, not a "
                        "guaranteed recognition accuracy."
                    )
                except Exception as exc:
                    st.error(f"Character recognition failed: {exc}")

elif selected_mode == "🧘 Card 3: Posture Detection":
    st.markdown("## 🧘 Card 3: Real-Time Posture Detection")
    st.write("Capture your upper body to run MediaPipe Pose estimation and analyze spine/shoulder alignment.")
    
    img_file = st.camera_input("Capture frame for Posture Analysis")
    if img_file is not None and MP_AVAILABLE:
        bytes_data = img_file.getvalue()
        cv_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        
        mp_pose = mp.solutions.pose
        mp_drawing = mp.solutions.drawing_utils
        
        with mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.7) as pose:
            rgb_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_img)
            
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(cv_img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                
                # Calculate shoulder alignment
                landmarks = results.pose_landmarks.landmark
                h, w, _ = cv_img.shape
                left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
                right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
                
                ls_y, rs_y = left_shoulder.y * h, right_shoulder.y * h
                shoulder_diff = abs(ls_y - rs_y)
                
                status_text = "Good Posture (Balanced)" if shoulder_diff < 15 else "Slouching Detected (Adjust Spine)"
                color = (0, 255, 0) if shoulder_diff < 15 else (0, 0, 255)
                
                cv2.putText(cv_img, status_text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            else:
                cv2.putText(cv_img, "Pose Not Fully Visible", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
        st.image(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB), channels="RGB", caption="Posture Skeletal Overlay")
        st.success("Posture angle analysis complete!")

else:
    st.markdown("## 📌 System Overview")
    st.write("Select any specific module from the left sidebar to activate live OpenCV and MediaPipe computer vision processing.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size: 0.9rem;'>VisionAI Suite | OpenCV & MediaPipe Integration</p>",
    unsafe_allow_html=True
)