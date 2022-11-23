from flask import Flask, render_template,Response
from camera import Video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame +
                b'\r\n\r\n')

@app.route('/video')
def video():
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)

# from flask import Flask, render_template, Response
# from emotion import Emotions
# app = Flask(__name__)
# @app.route('/')
# def index():
#     # rendering webpage
#     return render_template('index.html')
# def gen(emotion):
#     while True:
#         #get emotion frame
#         frame = emotion.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
# @app.route('/emotionml')
# def emotionml():
#     return Response(gen(Emotions()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
# if __name__ == '__main__':
#     # defining server ip address and port
#     app.run( debug=True)