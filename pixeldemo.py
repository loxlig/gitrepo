#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import time as tm

plt.style.use('dark_background')


class DoPixels(object):
    def __init__(self):
        self.w, self.h = 24, 24
        self.camera = np.zeros([self.h, self.w], dtype=np.int)

        # The following line must remain in order to initialize the
        # array with at least 1 element set > 0. 
        self.n_camera = self.camera[0][0] = 5

        arr_expand = 1
        self.images1 = np.array([self.camera] * arr_expand, dtype=np.int)
        self.fig = plt.figure(figsize=(6.0, 6.0), dpi=100)
        self.cmap = 'gray'
        plt.ylabel('columns')
        plt.xlabel('rows')
        self.im = plt.imshow(self.images1[0], cmap=self.cmap, origin='lower', zorder=2, alpha=0.8)
        plt.tight_layout()
        self.fig.show()
        self.pt = 1.0
        self.end = 1
        self.of = self.end * len(self.images1)
        self.images = []

        self.anarg = np.array([0], dtype=np.int)
        self.selfx = 1
        for z in np.arange(24).tolist():
            plt.plot((np.zeros([24, 1], dtype=np.int) + [z]).tolist(), marker='s', ms=16, color='None',
                     markeredgecolor='w', markeredgewidth=0.9, alpha=0.9, zorder=1)

        t1 = tm.time()    
        self.selfi = np.array([0, self.h], dtype=np.int)
        self.selfj = np.array([0, self.w], dtype=np.int)

        for r in np.arange(self.end).tolist():
            for self.images in self.images1[0:]:
                for self.selfi in np.arange(self.h).tolist():
                    for self.selfj in np.arange(self.w).tolist():
                        plt.pause(0.00000000000000000000001)
                        self.images[self.selfi][self.selfj] = 5
                        self.im.set_data(self.images)
                        self.images[self.images == 5] = 1
                        self.fig.canvas.draw()

            self.images[self.images == 1] = 0
            self.images[self.images == 5] = 1
            self.selfx += 1

        self.images[self.images == 5] = 1
        self.images[self.images == 0] = 1
        self.im.set_data(self.images)
        self.fig.canvas.draw()

        t2 = tm.time()
        tdiff = t2 - t1
        print('time to complete: ' + str(tdiff) + ' secs.')
        plt.show()


dopixels = DoPixels()
