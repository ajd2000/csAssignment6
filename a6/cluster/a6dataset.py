"""
Dataset for k-Means clustering

This file contains the class Dataset, which is the very first part of the assignment.
You cannot do anything in this assignment (except run the unit test) before this class
is finished.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""
import math
import random
import numpy


# For checking preconditions
import a6checks

# CLASSES FOR THE ASSIGNMENT
class Dataset(object):
    """
    A class representing a dataset for k-means clustering.

    The data is stored as a list of list of numbers (ints or floats).  Each component
    list is a data point.

    INSTANCE ATTRIBUTES:
        _dimension: the point dimension for this dataset
                    [int > 0. Value never changes after initialization]
        _contents:  the dataset contents
                    [a list of lists of numbers (float or int), possibly empty.
    EXTRA INVARIANTS:
        The number of columns in _contents is equal to _dimension.  That is, for every
        item _contents[i] in the list _contents, len(_contents[i]) == dimension.

    None of the attributes should be accessed directly outside of the class Dataset
    (e.g. in the methods of class Cluster or KMeans). Instead, this class has getter and
    setter style methods (with the appropriate preconditions) for modifying these values.
    """

    def __init__(self, dim, contents=None):
        """
        Initializes a database for the given point dimension.

        The optional parameter contents is the initial value of the attribute _contents.
        When assigning contents to the attribute _contents it COPIES the list contents.
        If contents is None, the initializer assigns _contents an empty list. The
        parameter contents is None by default.

        Parameter dim: The dimension of the dataset
        Precondition: dim is an int > 0

        Parameter contents: the dataset contents
        Precondition: contents is either None or it is a table of numbers (int or float).
        If contents is not None, then contents if not empty and the number of columns is
        equal to dim.
        """
        # MAKE SURE ALL ASSERTS ARE DONE
        assert(isinstance(dim, int) and dim > 0)
        assert(isinstance(contents, list) or contents == None)
        cContents = []
        if(not contents == None):
            for i in range(len(contents)):
                assert(len(contents[i]) == dim)
                cContents.append([])
                for j in range(len(contents[i])):
                    cContents[i].append(contents[i][j])

        self._dimension = dim
        self._contents = cContents



    def getDimension(self):
        """
        Returns the point dimension of this data set
        """
        return self._dimension

    def getSize(self):
        """
        Returns the number of elements in this data set.
        """
        # IMPLEMENT ME
        if(self._contents == None):
            return 0
        return len(self._contents)

    def getContents(self):
        """
        Returns the contents of this data set as a list.

        This method returns the attribute _contents directly.  Any changes made to this
        list will modify the data set.  If you want to access the data set, but want to
        protect yourself from modifying the data, use getPoint() instead.
        """
        # IMPLEMENT ME
        return self._contents

    def getPoint(self, i):
        """
        Returns a COPY of the point at index i in this data set.

        Often, we want to access a point in the data set, but we want a copy to make sure
        that we do not accidentally modify the data set.  That is the purpose of this
        method.

        If you actually want to modify the data set, use the method getContents().
        That returns the list storing the data set, and any changes to that
        list will alter the data set.
        While it is possible, to access the points of the data set via
        the method getContents(), that method

        Parameter i: the index position of the point
        Precondition: i is an int that refers to a valid position in 0..getSize()-1
        """
        # IMPLEMENT ME
        assert(isinstance(i,int))
        assert(i < self.getSize())
        copy = []
        for x in range(len(self._contents[i])):
            copy.append(self._contents[i][x])
        return copy

    def addPoint(self,point):
        """
        Adds a COPY of point at the end of _contents.

        This method does not add the point directly. It adds a copy of the point.

        Precondition: point is a list of numbers (int or float),  len(point) = _dimension."""
        # IMPLEMENT ME
        assert(isinstance(point, list))
        assert(len(point) == self.getDimension())
        copy = []
        for x in range(len(point)):
            assert(isinstance(x, int) or isinstance(x, float))
            copy.append(point[x])
        self._contents.append(copy)
