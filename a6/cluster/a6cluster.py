"""
Cluster class for k-Means clustering

This file contains the class cluster, which is the second part of the assignment.  With
this class done, the visualization can display the centroid of a single cluster.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import math
import random
import numpy


# For accessing the previous parts of the assignment
import a6checks
import a6dataset


class Cluster(object):
    """
    A class representing a cluster, a subset of the points in a dataset.

    A cluster is represented as a list of integers that give the indices in the dataset
    of the points contained in the cluster.  For instance, a cluster consisting of the
    points with indices 0, 4, and 5 in the dataset's data array would be represented by
    the index list [0,4,5].

    A cluster instance also contains a centroid that is used as part of the k-means
    algorithm.  This centroid is an n-D point (where n is the dimension of the dataset),
    represented as a list of n numbers, not as an index into the dataset. (This is because
    the centroid is generally not a point in the dataset, but rather is usually in between
    the data points.)

    INSTANCE ATTRIBUTES:
        _dataset [Dataset]: the dataset this cluster is a subset of
        _indices [list of int]: the indices of this cluster's points in the dataset
        _centroid [list of numbers]: the centroid of this cluster
    EXTRA INVARIANTS:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """

    # Part A
    def __init__(self, dset, centroid):
        """
        Initializes a new empty cluster whose centroid is a copy of <centroid>

        Parameter dset: the dataset
        Precondition: dset is an instance of Dataset

        Parameter centroid: the cluster centroid
        Precondition: centroid is a list of ds.getDimension() numbers
        """
        # IMPLEMENT ME
        assert(isinstance(dset, a6dataset.Dataset))
        assert(isinstance(centroid,list))
        assert(len(centroid) == dset.getDimension())
        self._centroid = centroid
        self._dataset = dset
        self._indices = []

    def getCentroid(self):
        """
        Returns the centroid of this cluster.

        This getter method is to protect access to the centroid.
        """
        # IMPLEMENT ME
        copy = []
        for i in range(len(self._centroid)):
            copy.append(self._centroid[i])
        return copy

    def getIndices(self):
        """
        Returns the indices of points in this cluster

        This method returns the attribute _indices directly.  Any changes made to this
        list will modify the cluster.
        """
        # IMPLEMENT ME
        return self._indices

    def addIndex(self, index):
        """
        Adds the given dataset index to this cluster.

        If the index is already in this cluster, this method leaves the
        cluster unchanged.

        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize()-1.
        """
        # IMPLEMENT ME
        assert(isinstance(index, int))
        assert(index >= 0 and index < self._dataset.getSize())
        if(index not in self._indices):
            self._indices.append(index)

    def clear(self):
        """
        Removes all points from this cluster, but leave the centroid unchanged.
        """
        # IMPLEMENT ME
        for x in range(len(self._indices)):
            self._indices.remove(self._indices[0])

    def getContents(self):
        """
        Returns a new list containing copies of the points in this cluster.

        The result is a list of list of numbers.  It has to be computed from the indices.
        """
        result = []
        for i in self._indices:
            temp = self._dataset.getContents()
            result.append(temp[i])
        return result

    # Part B
    def distance(self, point):
        """
        Returns the euclidean distance from point to this cluster's centroid.

        Parameter point: The point to be measured
        Precondition: point is a list of numbers (int or float), with the same dimension
        as the centroid.
        """
        # IMPLEMENT ME
        result = 0
        for i in range(self._dataset.getDimension()):
            result += (point[i] - self._centroid[i])**2
        return math.sqrt(result)

    def getRadius(self):
        """
        Returns the maximum distance from any point in this cluster, to the centroid.

        This method loops over the contents to find the maximum distance from
        the centroid.  If there are no points in this cluster, it returns 0.
        """
        # IMPLEMENT ME
        max = 0
        for i in range(len(self.getContents())):
            if (self.distance(self.getContents()[i])> max):
                max = self.distance(self.getContents()[i])
        return max

    def update(self):
        """
        Returns True if the centroid remains the same after recomputation; False otherwise.

        This method recomputes the _centroid attribute of this cluster. The new _centroid
        attribute is the average of the points of _contents (To average a point, average
        each coordinate separately).

        Whether the centroid "remained the same" after recomputation is determined by
        numpy.allclose.  The return value should be interpreted as an indication of whether
        the starting centroid was a "stable" position or not.

        If there are no points in the cluster, the centroid. does not change.
        """
        # IMPLEMENT ME
        if(len(self._indices) == 0):
            return True
        else:
            recomp = []
            for x in range(self._dataset.getDimension()):
                temp = 0
                for i in range(len(self.getContents())):
                    temp += self.getContents()[i][x]
                div = len(self.getContents())
                recomp.append(temp/div)
            if numpy.allclose(self._centroid,recomp) == False:
                self._centroid = recomp
                return False
            else:
                return True

    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """
        Returns a String representation of the centroid of this cluster.
        """
        return str(self._centroid)

    def __repr__(self):
        """
        Returns an unambiguous representation of this cluster.
        """
        return str(self.__class__) + str(self)
