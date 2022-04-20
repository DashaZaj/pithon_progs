import cv2


def reverse(path):
    cap = cv2.VideoCapture(path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    rat, frame = cap.read()
    h, w, c = frame.shape

    out = cv2.VideoWriter('output.mp4', fourcc, fps, (w, h))
    frames = [frame]
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
        else:
            break
    for i in range(len(frames)-1, -1, -1):
        out.write(frames[i])
    cap.release()
    out.release()
    cv2.destroyAllWindows()


reverse('videoplayback.mp4')
