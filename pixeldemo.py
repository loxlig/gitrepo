#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import time as tm

plt.style.use('dark_background')


class DoPixels(object):
    def __init__(self):
        self.w, self.h = 24, 24 
        self.camera = np.zeros([self.h, self.w], dtype=np.int).tolist()
        arr_expand = 1
        self.images1 = np.array([self.camera] * arr_expand, dtype=np.int)
        # Initialize "pixel" values to 5
        self.images1[0][0] = 5
        self.fig = plt.figure(figsize=(10.68, 10.68), dpi=100)
        self.cmap = 'gray'
        plt.ylabel('columns')
        plt.xlabel('rows')
        self.im = ''
        self.pt, self.end, self.of = 0, 0, 0
        self.selfi, self.selfj, self.images = np.array([]), np.array([]), np.array([])
        
    def run(self):
        ax = plt.gca()
        [ax.plot((np.zeros([self.w, 1], dtype=np.int) + [z]).tolist(), marker='s', ms=30, color='None',
                 markeredgecolor='w', markeredgewidth=0.9, alpha=0.9, zorder=1) for z in np.arange(self.w).tolist()]

        self.im = plt.imshow(self.images1[0].tolist(), cmap=self.cmap, origin='upper', zorder=2, alpha=0.8)
        plt.tight_layout()
        self.end = 10
        self.of = self.end * len(self.images1)
        self.selfi = np.array([0, self.h], dtype=np.int).tolist()
        self.selfj = np.array([0, self.w], dtype=np.int).tolist()
        self.plotit()

    def plotit(self):
        t1 = tm.time()
        for self.end in np.arange(self.end).tolist():
            for self.images in self.images1[0:]:
                for self.selfi in np.arange(self.h).tolist():
                    plt.pause(1e-2)
                    for self.selfj in np.arange(self.w).tolist():
                        self.images[self.selfi][self.selfj] = 5
                        self.im.set_data(self.images)
                        self.images[self.images == 5] = 1

            self.images[self.images == 1] = 0
            self.images[self.images == 5] = 1

        self.images[self.images == 5] = 1
        self.images[self.images == 0] = 1
        self.im.set_data(self.images)

        t2 = tm.time()
        tdiff = t2 - t1
        print('time to complete: ' + str(tdiff) + ' secs.')
        plt.draw()
        plt.show()


if __name__ == "__main__":
    dopixels = DoPixels()
    dopixels.run()
