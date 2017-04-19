from net.common import *




## regression -------------------------------------------------------
##<todo> refine this normalisation later ... e.g. use log(scale)
def box3d_transform0(et_boxes3d, gt_boxes3d):

    et_centers =   np.sum(et_boxes3d,axis=1, keepdims=True)/8
    et_scales  =   np.sum((et_boxes3d-et_centers)**2, axis=2, keepdims=True)**0.5
    deltas = (et_boxes3d-gt_boxes3d)/et_scales
    return deltas


def box3d_transform_inv0(et_boxes3d, deltas):

    et_centers =  np.sum(et_boxes3d,axis=1, keepdims=True)/8
    et_scales  =  10#*np.sum((et_boxes3d-et_centers)**2, axis=2, keepdims=True)**0.5
    boxes3d = -deltas*et_scales+et_boxes3d

    return boxes3d

def box3d_transform(et_boxes3d, gt_boxes3d):

    num=len(et_boxes3d)
    deltas=np.zeros((num,8,3),dtype=np.float32)
    for n in range(num):
        e=et_boxes3d[n]
        center = np.sum(e,axis=0, keepdims=True)/8
        scale = (np.sum((e-center)**2)/8)**0.5

        g=gt_boxes3d[n]
        deltas[n]= (g-e)/scale
    return deltas


def box3d_transform_inv(et_boxes3d, deltas):

    num=len(et_boxes3d)
    boxes3d=np.zeros((num,8,3),dtype=np.float32)
    for n in range(num):
        e=et_boxes3d[n]
        center = np.sum(e,axis=0, keepdims=True)/8
        scale = (np.sum((e-center)**2)/8)**0.5

        d=deltas[n]
        boxes3d[n]= e+scale*d

    return boxes3d


##<todo> refine this regularisation later
def regularise_box3d(boxes3d):

    num = len(boxes3d)
    reg_boxes3d =np.zeros((num,8,3),dtype=np.float32)
    for n in range(num):
        b=boxes3d[n]

        dis=0
        corners = np.zeros((4,3),dtype=np.float32)
        for k in range(0,4):
            #http://docs.enthought.com/mayavi/mayavi/auto/mlab_helper_functions.html
            i,j=k,k+4
            dis +=np.sum((b[i]-b[j])**2) **0.5
            corners[k] = (b[i]+b[j])/2

        dis = dis/4
        b = reg_boxes3d[n]
        for k in range(0,4):
            i,j=k,k+4
            b[i]=corners[k]-dis/2*np.array([0,0,1])
            b[j]=corners[k]+dis/2*np.array([0,0,1])

    return reg_boxes3d