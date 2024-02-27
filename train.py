from ultralytics import YOLO
from args_ import *
import argparse


def train(args):
    data_path = "/dataset/firstset/data.yaml"
    model = YOLO("runs/detect/train6/weights/last.pt")
    model.train(data=args.dir + data_path, resume=True)
    #model.train(data=args.dir + data_path, epochs=150, patience=20, batch=20, workers=8, val=True)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args = arg_init(args)
    train(args)
