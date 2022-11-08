import random
from full_disks import build_url, get_image
from nasa_sdo import get_sdo_image
from sentinel import fetch_image
from utils import make_border
import sys

sources = [
    "goes-16",
    "goes-17",
    "goes-18",
    "himawari",
    "meteosat-9",
    "meteosat-11",
    "sentinel",
    "sdo",
]
random_sources = [
    "goes-16",
    "goes-17",
    "goes-18",
    "himawari",
    "meteosat-9",
    "meteosat-11",
    "sdo",
]

sizes = [678, 1356,2227, 5424, 10848]

def get_Sat_Image(args):
    if (
            args.width is not None or args.height is not None
        ) and args.source != "sentinel":
            smaller = min([args.width if args.width is not None else sys.maxsize, args.height if args.height is not None else sys.maxsize])

            for i in range(0, len(sizes)):
                if smaller < sizes[i]:
                    break

            args.zoomLevel = i

    if args.source is None:
        args.source = random.choice(random_sources)

    if args.source == "sdo":
        bg = get_sdo_image(args)

    elif args.source == "sentinel":
        bg = fetch_image(args)

    else:
        base_url = build_url(args)
        bg = get_image(args, base_url)

    if args.width is not None and args.height is not None:
        bg = make_border(bg, args.width, args.height)

    elif args.width is not None:
        bg = make_border(bg, args.width, bg.size[1])

    elif args.height is not None:
        bg = make_border(bg, bg.size[0], args.height)
    
    return bg