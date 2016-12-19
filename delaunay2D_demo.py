#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
Simple delaunay2D demo with mathplotlib
Written by Jose M. Espadero < http://github.com/jmespadero/pyDelaunay2D >
"""
import numpy as np
from delaunay2D import Delaunay2D

if __name__ == '__main__':

    ###########################################################
    # Generate 'numSeeds' random seeds in a square of size 'radius'
    numSeeds = 24
    radius = 100
    seeds = radius * np.random.random((numSeeds, 2))
    print("seeds:\n", seeds)
    print("BBox Min:", np.amin(seeds, axis=0),
          "Bbox Max: ", np.amax(seeds, axis=0))

    """
    Compute our Delaunay triangulation of seeds.
    """
    # It is recommended to build a frame taylored for our data
    # dt = D.Delaunay2D() # Default frame
    center = np.mean(seeds, axis=0)
    dt = Delaunay2D(center, 50 * radius)
    
    # Insert all seeds one by one
    for s in seeds:
        dt.AddPoint(s)

    # Dump number of DT triangles
    print (len(dt.exportTriangles()), "Delaunay triangles")
       
    """
    Show how to plot triangular grids.
    """
    import matplotlib.pyplot as plt
    import matplotlib.tri
    import matplotlib.collections

    # Create a plot with matplotlib.pyplot
    fig, ax = plt.subplots()
    ax.margins(0.1)
    ax.set_aspect('equal')

    # Plot our Delaunay triangulation (plot in blue)
    dt_x, dt_y, dt_tris = dt.exportDT()
    ax.triplot(matplotlib.tri.Triangulation(dt_x, dt_y, dt_tris), 'bo--')

    # DEBUG: Use matplotlib to create a Delaunay triangulation (plot in green)
    # DEBUG: It should be equal to our result in dt_tris (plot in blue)
    # DEBUG: If boundary is diferent, try to increase the value of your margin
    # ax.triplot(matplotlib.tri.Triangulation(dt_x, dt_y), 'g--')

    # Plot the circumcircles (circles in black)
    # for c, r in dt.exportCircles():
    #     ax.add_artist(plt.Circle(c, r, color='k', fill=False, ls='dotted'))

    # Plot voronoi diagram edges (in red)
    # ve = dt.exportVoronoiEdges()
    # ax.add_collection(matplotlib.collections.LineCollection(ve, colors='r'))

    # Plot voronoi regions (in red)
    # Dump number of DT triangles
    # vc, vr = dt.exportVoronoiRegions()
    # Plot voronoi vertex
    # plt.scatter([v[0] for v in vc], [v[1] for v in vc], marker='.')
    # for i, v in enumerate(vc):
    #     plt.annotate(i, xy=(v[0], v[1]))
    
    # Plot voronoi regions
    # for r in vr:
    #     if vr[r]:
    #         polygon = [(vc[i][0], vc[i][1]) for i in vr[r]]
    #         plt.fill(*zip(*polygon), alpha=0.2)
    #         # plot a label for the region
    
    # DEBUG: plot the extended triangulation (plot in red)
    # edt_x, edt_y, edt_tris = dt.exportExtendedDT()
    # print("Extended dt_tris:", len(edt_tris), "triangles")
    # ax.triplot(matplotlib.tri.Triangulation(edt_x, edt_y, edt_tris), 'ro-.')

    # Dump plot to file
    # plt.savefig('output-delaunay2D.png', dpi=96)
    # plt.savefig('output-delaunay2D.svg', dpi=96)

    plt.show()

    """
    Demo of a step-by-step triangulation plot
    """

    """
    # Build a new DT frame
    dt2 = Delaunay2D(center, 50 * radius)    
    for i,s in enumerate(seeds):
        print("Inserting seed", s)
        dt2.AddPoint(s)
        if i > 1:
            fig, ax = plt.subplots()
            ax.margins(0.1)
            ax.set_aspect('equal')
            dt_x, dt_y, dt_tris = dt2.exportDT()
            ax.triplot(matplotlib.tri.Triangulation(dt_x, dt_y, dt_tris))
            plt.show()
    """
