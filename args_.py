import os


def arg_init(args):
    dirpath = os.path.dirname(os.path.realpath(__file__))
    args.add_argument("--dir", type=str, default=dirpath, help="root dir path")
    args.add_argument(
        "--save_dir", type=str, default=dirpath + "/predict", help="save dir"
    )
    args.add_argument(
        "--model_dir", type=str, default=dirpath + "/model", help="model dir"
    )
    args.add_argument(
        "--smooth", type=float, default=0.1, help="delay after mouse movements"
    )
    args.add_argument(
        "--mouse_speed_factor", type=float, default=0.4, help="multiplies mouse speed, below 1 makes movements realistic"
    )
    args.add_argument(
        "--show", type=bool, default=False, help="popout with boxes"
    )
    args.add_argument(
        "--movement_limit", type=float, default=120, help="limit to stop snaps beyond a certain distance"
    )
    args.add_argument("--model", type=str,
                      default="/best.engine", help="model path")
    args.add_argument("--iou", type=float,
                      default=0.5, help="predict iou")
    args.add_argument("--classes",
                      type=int,
                      default=[1,2],
                      help="classes to be detected, can be expanded but needs to be an array. "
                           "For example, the default weight has: "
                           "0 represents 'Teammate',"
                           "1 represents 'Enemy', "
                           "2 represents 'Hitmark'..."
                           "Change default accordingly if your dataset changes")
    args.add_argument("--conf", type=float,
                      default=0.5, help="predict conf")
    args.add_argument("--crop_size", type=float,
                      default=1/3,
                      help="the portion to detect from the screen(=crop_window_height/screen_height)"
                           "(It's always a rectangle)(from 0 to 1)")
    args.add_argument("--wait", type=float, default=0, help="wait time")
    args.add_argument("--verbos", type=bool, default=False, help="predict verbos")
    args.add_argument("--target_index", type=int,
                      default=1, help="target index")
    args.add_argument("--half", type=bool, default=True,
                      help="use half to predict")



    # PID args
    args.add_argument("--pid", type=bool, default=True, help="use pid")
    args.add_argument("--Kp", type=float, default=0.8, help="Kp")
    args.add_argument("--Ki", type=float, default=0.05, help="Ki")
    args.add_argument("--Kd", type=float, default=0.1, help="Kd")

    args = args.parse_args(args=[])
    return args
