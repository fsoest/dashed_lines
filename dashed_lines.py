from base import dec_to_dms, dms_to_dec
import numpy as np
from mpl_toolkits.basemap import Basemap
from argparse import ArgumentParser


def main(lat1, lon1, lat2, lon2, n, txt):
    lat1_dec = dms_to_dec(lat1)
    lon1_dec = dms_to_dec(lon1)
    lat2_dec = dms_to_dec(lat2)
    lon2_dec = dms_to_dec(lon2)

    def bm(a, b, inverse=True):
        return a, b

    x1, y1 = bm(lon1_dec, lat1_dec)
    x2, y2 = bm(lon2_dec, lat2_dec)
    c1 = np.array([x1, y1])
    c2 = np.array([x2, y2])
    delta = (c2 - c1) / (2 * n)

    for i in range(n):
        lower = c1 + 2 * i * delta
        upper = c1 + (2 * i + 1) * delta
        l1, l2 = bm(lower[0], lower[1], inverse=True)
        u1, u2 = bm(upper[0], upper[1], inverse=True)
        print(dec_to_dms(l2), dec_to_dms(l1), dec_to_dms(u2), dec_to_dms(u1), txt)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('lat1', type=str, help='Latitude of first point')
    parser.add_argument('lon1', type=str, help='Longitude of first point')
    parser.add_argument('lat2', type=str, help='Latitude of first point')
    parser.add_argument('lon2', type=str, help='Longitude of first point')
    parser.add_argument('n', type=int, help='Number of dashes')
    parser.add_argument('txt', type=str, help='Color definition')
    args = parser.parse_args()
    main(args.lat1, args.lon1, args.lat2, args.lon2, args.n, args.txt)
