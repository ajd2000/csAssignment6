"""
Primary algorithm for k-Means clustering

This file contains the Algorithm class for performing k-means clustering.  While it is
the last part of the assignment, it is the heart of the clustering algorithm.  You
need this class to view the complete visualizer.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6checks
import a6dataset
import a6cluster


class Algorithm(object):
    """
    A class to manage and run the k-means algorithm.

    INSTANCE ATTRIBUTES:
        _dataset [Dataset]: the dataset which this is a clustering of
        _clusters [list of Cluster]: the clusters in this clustering (not empty)
    """

    # Part A
    def __init__(self, dset, k, seeds=None):
        """
        Initializes the algorithm for the dataset ds, using k clusters.

        If the optional argument seeds is supplied, it will be a list of indices into the
        dataset that specifies which points should be the initial cluster centroids.
        Otherwise, the clusters are initialized by randomly selecting k different points
        from the database to be the cluster centroids.

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter k: the number of clusters
        Precondition: k is an int, 0 < k <= dset.getSize()

        Paramter seeds: the initial cluster indices (OPTIONAL)
        Precondition seeds is None, or a list of k valid indices into dset.
        """
        # IMPLEMENT ME
        assert(isinstance(dset, a6dataset.Dataset))
        assert(isinstance(k, int))
        assert(k > 0 and k < dset.getSize())
        self._dataset = dset
        if(seeds == None):
            seeds = random.sample(dset.getContents(), k)
        else:
            assert(isinstance(seeds, list))
            assert(len(seeds) == k)
            temp = []
            for x in seeds:
                assert(isinstance(x, int))
                assert(x >= 0 and x < self._dataset.getSize())
                temp.append(self._dataset.getContents()[x])
            seeds = temp
        self._clusters = []
        for i in range(len(seeds)):
            temp = a6cluster.Cluster(self._dataset, seeds[i])
            self._clusters.append(temp)
        assert(isinstance(self._clusters, list))
        for x in self._clusters:
            assert(isinstance(x, a6cluster.Cluster))

    def getClusters(self):
        """
        Returns the list of clusters in this object.

        This method returns the attribute _clusters directly.  Any changes made to this
        list will modify the set of clusters.
        """
        # IMPLEMENT ME
        return self._clusters

    # Part B
    def _nearest(self, point):
        """
        Returns the cluster nearest to point

        This method uses the distance method of each Cluster to compute the distance
        between point and the cluster centroid. It returns the Cluster that is closest.

        Ties are broken in favor of clusters occurring earlier self._clusters.

        Parameter point: The point to compare.
        Precondition: point is a list of numbers (int or float), with the same dimension
        as the dataset.
        """
        # IMPLEMENT ME
        assert(isinstance(point, list))
        assert(len(point) == self._dataset.getDimension())
        for x in point:
            assert(isinstance(x, float) or isinstance(x, int))
        close = None
        for z in self._clusters:
            if(close == None):
                close = z
            if(z.distance(point) < close.distance(point)):
                close = z
        return close

    def _partition(self):
        """
        Repartitions the dataset so each point is in exactly one Cluster.
        """
        # First, clear each cluster of its points.  Then, for each point in the
        # dataset, find the nearest cluster and add the point to that cluster.

        # IMPLEMENT ME
        for x in self._clusters:
            x.clear()
        for i in range(self._dataset.getSize()):
            self._nearest(self._dataset.getContents()[i]).addIndex(i)

    # Part C
    def _update(self):
        """
        Returns true if all centroids are unchanged after an update; False otherwise.

        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It then returns the appropriate value.
        """
        # IMPLEMENT ME
        pass

    def step(self):
        """
        Returns True if the algorithm converges after one step; False otherwise.

        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns the appropriate value.
        """
        # In a cycle, we partition the points and then update the means.
        # IMPLEMENT ME
        pass

    # Part D
    def run(self, maxstep):
        """
        Continues clustering until either it converges or maxstep steps
        (which ever comes first).

        This method calls step() repeatedly, up to maxstep times, until the
        algorithm converges. It stops after maxstep iterations even if the
        algorithm has not converged.

        Parameter maxstep: the maximum number of steps to try
        Precondition: maxstep is an int >= 0
        """
        # You do not need a while loop for this.  Just write a for-loop, and exit
        # the for-loop (with a return) if you finish early.

        # IMPLEMENT ME
        pass
