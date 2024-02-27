from ultralytics import YOLO

def predict_init(args):
    global model
    print("Predict on", args.model_dir + args.model)
    print(args)
    model = YOLO(args.model_dir + args.model, task='detect')
def predict(args,img):
    global model
    res = model.track(img, verbose=args.verbos, half=args.half, iou=args.iou, conf=args.conf, show=args.show, persist=True, tracker="bytetrack.yaml")
    #print(res)
    return res[0]
