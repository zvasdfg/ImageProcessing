import numpy as np

def euclidean2D_to_homogeneus(x):
    """
    Convert a 2D point in euclidean space to a projective space
    Parameters
    ----------
    x : np.Array
        Point in 2D euclidean space
    Returns
    -------
    x : np.Array
        Point in projective space
    """ 
    assert  (2 == len(x)), 'The argument is not a 2D Point'
    x = np.append(x,1)
    return x

def homogeneus_to_euclidean2D(x):
    """
    Convert a 2D point in projective space to euclidean space
    Parameters
    ----------
    x : np.Array
        Point in projective space
    Returns
    -------
    x : np.Array
        Point in 2D euclidean space
    """ 
    assert  (3 == len(x)), 'The argument is not a 3D Point'
    assert  (0 != x[2])  , 'x is a point in the infinite, it doesnt '
    x=x/x[2]
    x = np.delete(x,2)
    return x