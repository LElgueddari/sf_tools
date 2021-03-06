# -*- coding: utf-8 -*-

"""NUMPY ADJUSTMENT ROUTINES

This module contains methods for adjusting the default output for certain
Numpy functions.

:Author: Samuel Farrens <samuel.farrens@gmail.com>

:Version: 1.1

:Date: 03/04/2017

"""

from __future__ import division
import numpy as np


def rotate(data):
    """Rotate

    This method rotates an input numpy array by 180 degrees.

    Parameters
    ----------
    data : np.ndarray
        Input data array (at least 2D)

    Returns
    -------
    np.ndarray rotated data

    Notes
    -----
    Adjustment to numpy.rot90()

    Examples
    --------
    >>> from sf_tools.base.np_adjust import rotate
    >>> x = np.arange(9).reshape((3, 3))
    >>> x
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
    >>> rotate(x)
    array([[8, 7, 6],
           [5, 4, 3],
           [2, 1, 0]])

    """

    return np.rot90(data, 2)


def rotate_stack(data):
    """Rotate stack

    This method rotates each array in a stack of arrays by 180 degrees.

    Parameters
    ----------
    data : np.ndarray
        Input data array (at least 3D)

    Returns
    -------
    np.ndarray rotated data

    Examples
    --------
    >>> from sf_tools.base.np_adjust import rotate_stack
    >>> x = np.arange(18).reshape((2, 3, 3))
    >>> x
    array([[[ 0,  1,  2],
            [ 3,  4,  5],
            [ 6,  7,  8]],
           [[ 9, 10, 11],
            [12, 13, 14],
            [15, 16, 17
    >>> rotate_stack(x)
    array([[[ 8,  7,  6],
            [ 5,  4,  3],
            [ 2,  1,  0]],
           [[17, 16, 15],
            [14, 13, 12],
            [11, 10,  9]]])

    """

    return np.array([rotate(x) for x in data])


def pad2d(data, padding):
    """Pad array

    This method pads an input numpy array with zeros in all directions.

    Parameters
    ----------
    data : np.ndarray
        Input data array (at least 2D)
    shape : tuple
        Amount of padding in x and y directions, respectively

    Returns
    -------
    np.ndarray padded data

    Notes
    -----
    Adjustment to numpy.pad()

    Examples
    --------
    >>> from sf_tools.base.np_adjust import pad2d
    >>> x = np.arange(9).reshape((3, 3))
    >>> x
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
    >>> pad2d(x, (1, 1))
    array([[0, 0, 0, 0, 0],
           [0, 0, 1, 2, 0],
           [0, 3, 4, 5, 0],
           [0, 6, 7, 8, 0],
           [0, 0, 0, 0, 0]])

    """

    data = np.array(data)
    shape = np.array(data.shape)

    if shape.ndim == 1:
        shape = np.repeat(shape, 2)

    return np.pad(data, ((shape[0], shape[0]), (shape[1], shape[1])),
                  'constant')


def x_bins(vals):
    """X-range bins

    This method sets the bin values for a histogram.

    Parameters
    ----------
    vals : np.ndarray
        X-range bins from np.histogram()[1]

    Returns
    -------
    np.ndarray corrected x-range bin data

    Notes
    -----
    Adjustment to numpy.histogram()

    Examples
    --------
    >>> from sf_tools.base.np_adjust import x_bins
    >>> data = np.array([1, 2, 1, 3, 1, 1])
    >>> hist, bins = np.histogram(data)
    >>> hist
    array([4, 0, 0, 0, 0, 1, 0, 0, 0, 1])
    >>> bins
    array([ 1. ,  1.2,  1.4,  1.6,  1.8,  2. ,  2.2,  2.4,  2.6,  2.8,  3. ])
    >>> x_bins(bins)
    array([ 1.1,  1.3,  1.5,  1.7,  1.9,  2.1,  2.3,  2.5,  2.7,  2.9])

    """

    return (vals[:-1] + vals[1:]) / 2.0


def x_bins_step(vals):
    """X-range bins (step function)

    This method sets the bin values for a histogram plotted as a step funciton.

    Parameters
    ----------
    vals : np.ndarray
        X-range bins from np.histogram()[1]

    Returns
    -------
    np.ndarray corrected x-range bin data

    Notes
    -----
    Adjustment to numpy.histogram()

    Examples
    --------
    >>> from sf_tools.base.np_adjust import x_bins
    >>> data = np.array([1, 2, 1, 3, 1, 1])
    >>> hist, bins = np.histogram(data)
    >>> hist
    array([4, 0, 0, 0, 0, 1, 0, 0, 0, 1])
    >>> bins
    array([ 1. ,  1.2,  1.4,  1.6,  1.8,  2. ,  2.2,  2.4,  2.6,  2.8,  3. ])
    >>> x_bins_step(bins)
    array([ 1.2,  1.4,  1.6,  1.8,  2. ,  2.2,  2.4,  2.6,  2.8,  3. ])

    """

    return x_bins(vals) + (vals[1] - vals[0]) / 2.0


def ftr(data):
    """Fancy transpose right

    Apply fancy_transpose() to data with roll=1

    Parameters
    ----------
    data : np.ndarray
        Input data array

    Returns
    -------
    np.ndarray transposed data

    """

    return fancy_transpose(data)


def ftl(data):
    """Fancy transpose left

    Apply fancy_transpose() to data with roll=-1

    Parameters
    ----------
    data : np.ndarray
        Input data array

    Returns
    -------
    np.ndarray transposed data

    """

    return fancy_transpose(data, -1)


def fancy_transpose(data, roll=1):
    """Fancy transpose

    This method transposes a multidimensional matrix.

    Parameters
    ----------
    data : np.ndarray
        Input data array
    roll : int
        Roll direction and amount. Default (roll=1)

    Returns
    -------
    np.ndarray transposed data

    Notes
    -----
    Adjustment to numpy.transpose

    Examples
    --------
    >>> from sf_tools.base.np_adjust import fancy_transpose
    >>> x = np.arange(27).reshape(3, 3, 3)
    >>> x
    array([[[ 0,  1,  2],
            [ 3,  4,  5],
            [ 6,  7,  8]],
           [[ 9, 10, 11],
            [12, 13, 14],
            [15, 16, 17]],
           [[18, 19, 20],
            [21, 22, 23],
            [24, 25, 26]]])
    >>> fancy_transpose(x)
    array([[[ 0,  3,  6],
            [ 9, 12, 15],
            [18, 21, 24]],
           [[ 1,  4,  7],
            [10, 13, 16],
            [19, 22, 25]],
           [[ 2,  5,  8],
            [11, 14, 17],
            [20, 23, 26]]])
    >>> fancy_transpose(x, roll=-1)
    array([[[ 0,  9, 18],
            [ 1, 10, 19],
            [ 2, 11, 20]],
           [[ 3, 12, 21],
            [ 4, 13, 22],
            [ 5, 14, 23]],
           [[ 6, 15, 24],
            [ 7, 16, 25],
            [ 8, 17, 26]]])

    """

    axis_roll = np.roll(np.arange(data.ndim), roll)

    return np.transpose(data, axes=axis_roll)
