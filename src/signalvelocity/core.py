# src/velocityplot/core.py
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

def ConvertRGB2sth(r, g, b):
    tmp_r = (r/255.0)
    tmp_g = (g/255.0)
    tmp_b = (b/255.0)

    return tmp_r, tmp_g, tmp_b

def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
        if isinstance(item, float):
            r1, g1, b1 = seq[i - 1]
            r2, g2, b2 = seq[i + 1]
            cdict['red'].append([item, r1, r2])
            cdict['green'].append([item, g1, g2])
            cdict['blue'].append([item, b1, b2])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)

def getXYVectors(Xdim, Ydim):
    """
    x, y are the matrix dimentions from checkDims function
    """
    X = []
    Y = []
    for yi in range(0,Ydim,1):
        for xi in range(0,Xdim,1):
            if xi > 5 and xi < Xdim-6:
                X.append(xi)
                Y.append((Ydim-yi)/5)
    return X, Y

def getV(Raw_Values_condition_1, Raw_Values_condition_2, Xdim, Ydim):
    Xdim, Ydim = checkDims(Raw_Values_condition_1, Raw_Values_condition_2)
    V = []
    for yi in range(0,Ydim,1):
        for xi in range(0,Xdim,1):
            if xi > 5 and xi < Xdim-6:
                v = Raw_Values_condition_2[yi][xi] - Raw_Values_condition_1[yi][xi]
                try:
                    if yi > 0:
                        vp = Raw_Values_condition_2[yi-1][xi] - Raw_Values_condition_1[yi-1][xi]
                        if abs(v) < abs(vp):
                            v = vp
                except:
                    pass
                V.append(v)
    return V

def getH(Raw_Values_condition_1, Raw_Values_condition_2, Xdim, Ydim):
    Xdim, Ydim = checkDims(Raw_Values_condition_1, Raw_Values_condition_2)
    H = []
    
    n0_l0 = 0.5
    n1_l0 = 2
    n2_l0 = 4
    n3_l0 = 8
    n4_l0 = 16
    n5_l0 = 32
    
    n0_l1 = 1.5
    n1_l1 = 4
    n2_l1 = 8
    n3_l1 = 16
    n4_l1 = 32
    n5_l1 = 64
    
    n0_l2 = 16
    n1_l2 = 32
    n2_l2 = 64
    n3_l2 = 128
    n4_l2 = 256
    n5_l2 = 512
    
    for yi in range(0,Ydim,1):
        for xi in range(0,Xdim,1):
            if xi > 5 and xi < Xdim-6:
                if yi > 1:
                    H.append(abs(np.sum(Raw_Values_condition_2[yi][xi+0]/n0_l0+
                                         Raw_Values_condition_2[yi-1][xi+0]/n0_l1+
                                         Raw_Values_condition_2[yi-2][xi+0]/n0_l2+
                                         Raw_Values_condition_2[yi][xi+1]/n1_l0+
                                         Raw_Values_condition_2[yi-1][xi+1]/n1_l1+
                                         Raw_Values_condition_2[yi-2][xi+1]/n1_l2+
                                         Raw_Values_condition_2[yi][xi+2]/n2_l0+
                                         Raw_Values_condition_2[yi-1][xi+2]/n2_l1+
                                         Raw_Values_condition_2[yi-2][xi+2]/n2_l2+
                                         Raw_Values_condition_2[yi][xi+3]/n3_l0+
                                         Raw_Values_condition_2[yi-1][xi+3]/n3_l1+
                                         Raw_Values_condition_2[yi-2][xi+3]/n3_l2+
                                         Raw_Values_condition_2[yi][xi+4]/n4_l0+
                                         Raw_Values_condition_2[yi-1][xi+4]/n4_l1+
                                         Raw_Values_condition_2[yi-2][xi+4]/n4_l2+
                                         Raw_Values_condition_2[yi][xi+5]/n5_l0+
                                         Raw_Values_condition_2[yi-1][xi+5]/n5_l1+
                                         Raw_Values_condition_2[yi-2][xi+5]/n5_l2) - 
                                 
                                 np.sum(Raw_Values_condition_1[yi][xi+0]/n0_l0+
                                         Raw_Values_condition_1[yi-1][xi+0]/n0_l1+
                                         Raw_Values_condition_1[yi-2][xi+0]/n0_l2+
                                         Raw_Values_condition_1[yi][xi+1]/n1_l0+
                                         Raw_Values_condition_1[yi-1][xi+1]/n1_l1+
                                         Raw_Values_condition_1[yi-2][xi+1]/n1_l2+
                                         Raw_Values_condition_1[yi][xi+2]/n2_l0+
                                         Raw_Values_condition_1[yi-1][xi+2]/n2_l1+
                                         Raw_Values_condition_1[yi-2][xi+2]/n2_l2+
                                         Raw_Values_condition_1[yi][xi+3]/n3_l0+
                                         Raw_Values_condition_1[yi-1][xi+3]/n3_l1+
                                         Raw_Values_condition_1[yi-2][xi+3]/n3_l2+
                                         Raw_Values_condition_1[yi][xi+4]/n4_l0+
                                         Raw_Values_condition_1[yi-1][xi+4]/n4_l1+
                                         Raw_Values_condition_1[yi-2][xi+4]/n4_l2+
                                         Raw_Values_condition_1[yi][xi+5]/n5_l0+
                                         Raw_Values_condition_1[yi-1][xi+5]/n5_l1+
                                         Raw_Values_condition_1[yi-2][xi+5]/n5_l2) ) - 
                             
                             
                             abs(np.sum(Raw_Values_condition_2[yi][xi-0]/n0_l0+
                                         Raw_Values_condition_2[yi-1][xi-0]/n0_l1+
                                         Raw_Values_condition_2[yi-2][xi-0]/n0_l2+
                                         Raw_Values_condition_2[yi][xi-1]/n1_l0+
                                         Raw_Values_condition_2[yi-1][xi-1]/n1_l1+
                                         Raw_Values_condition_2[yi-2][xi-1]/n1_l2+
                                         Raw_Values_condition_2[yi][xi-2]/n2_l0+
                                         Raw_Values_condition_2[yi-1][xi-2]/n2_l1+
                                         Raw_Values_condition_2[yi-2][xi-2]/n2_l1+
                                         Raw_Values_condition_2[yi][xi-3]/n3_l0+
                                         Raw_Values_condition_2[yi-1][xi-3]/n3_l1+
                                         Raw_Values_condition_2[yi-2][xi-3]/n3_l2+
                                         Raw_Values_condition_2[yi][xi-4]/n4_l0+
                                         Raw_Values_condition_2[yi-1][xi-4]/n4_l1+
                                         Raw_Values_condition_2[yi-2][xi-4]/n4_l2+
                                         Raw_Values_condition_2[yi][xi-5]/n5_l0+
                                         Raw_Values_condition_2[yi-1][xi-5]/n5_l1+
                                         Raw_Values_condition_2[yi-2][xi-5]/n5_l2) - 
                                 
                                 np.sum(Raw_Values_condition_1[yi][xi-0]/n0_l0+
                                         Raw_Values_condition_1[yi-1][xi-0]/n0_l1+
                                         Raw_Values_condition_1[yi-2][xi-0]/n0_l2+
                                         Raw_Values_condition_1[yi][xi-1]/n1_l0+
                                         Raw_Values_condition_1[yi-1][xi-1]/n1_l1+
                                         Raw_Values_condition_1[yi-2][xi-1]/n1_l2+
                                         Raw_Values_condition_1[yi][xi-2]/n2_l0+
                                         Raw_Values_condition_1[yi-1][xi-2]/n2_l1+
                                         Raw_Values_condition_1[yi-2][xi-2]/n2_l2+
                                         Raw_Values_condition_1[yi][xi-3]/n3_l0+
                                         Raw_Values_condition_1[yi-1][xi-3]/n3_l1+
                                         Raw_Values_condition_1[yi-2][xi-3]/n3_l2+
                                         Raw_Values_condition_1[yi][xi-4]/n4_l0+
                                         Raw_Values_condition_1[yi-1][xi-4]/n4_l1+
                                         Raw_Values_condition_1[yi-2][xi-4]/n4_l2+
                                         Raw_Values_condition_1[yi][xi-5]/n5_l0+
                                         Raw_Values_condition_1[yi-1][xi-5]/n5_l1+
                                         Raw_Values_condition_1[yi-2][xi-5]/n5_l2 ) ) )
                elif yi > 0:
                    H.append(abs(np.sum(Raw_Values_condition_2[yi][xi+0]/n0_l0+
                                         Raw_Values_condition_2[yi-1][xi+0]/n0_l1+
                                         Raw_Values_condition_2[yi][xi+1]/n1_l0+
                                         Raw_Values_condition_2[yi-1][xi+1]/n1_l1+
                                         Raw_Values_condition_2[yi][xi+2]/n2_l0+
                                         Raw_Values_condition_2[yi-1][xi+2]/n2_l1+
                                         Raw_Values_condition_2[yi][xi+3]/n3_l0+
                                         Raw_Values_condition_2[yi-1][xi+3]/n3_l1+
                                         Raw_Values_condition_2[yi][xi+4]/n4_l0+
                                         Raw_Values_condition_2[yi-1][xi+4]/n4_l1+
                                         Raw_Values_condition_2[yi][xi+5]/n5_l0+
                                         Raw_Values_condition_2[yi-1][xi+5]/n5_l1 ) - 
                                 
                                 np.sum(Raw_Values_condition_1[yi][xi+0]/n0_l0+
                                         Raw_Values_condition_1[yi-1][xi+0]/n0_l1+
                                         Raw_Values_condition_1[yi][xi+1]/n1_l0+
                                         Raw_Values_condition_1[yi-1][xi+1]/n1_l1+
                                         Raw_Values_condition_1[yi][xi+2]/n2_l0+
                                         Raw_Values_condition_1[yi-1][xi+2]/n2_l1+
                                         Raw_Values_condition_1[yi][xi+3]/n3_l0+
                                         Raw_Values_condition_1[yi-1][xi+3]/n3_l1+
                                         Raw_Values_condition_1[yi][xi+4]/n4_l0+
                                         Raw_Values_condition_1[yi-1][xi+4]/n4_l1+
                                         Raw_Values_condition_1[yi][xi+5]/n5_l0+
                                         Raw_Values_condition_1[yi-1][xi+5]/n5_l1) ) - 
                             
                             
                             abs(np.sum(Raw_Values_condition_2[yi][xi-0]/n0_l0+
                                         Raw_Values_condition_2[yi-1][xi-0]/n0_l1+
                                         Raw_Values_condition_2[yi][xi-1]/n1_l0+
                                         Raw_Values_condition_2[yi-1][xi-1]/n1_l1+
                                         Raw_Values_condition_2[yi][xi-2]/n2_l0+
                                         Raw_Values_condition_2[yi-1][xi-2]/n2_l1+
                                         Raw_Values_condition_2[yi][xi-3]/n3_l0+
                                         Raw_Values_condition_2[yi-1][xi-3]/n3_l1+
                                         Raw_Values_condition_2[yi][xi-4]/n4_l0+
                                         Raw_Values_condition_2[yi-1][xi-4]/n4_l1+
                                         Raw_Values_condition_2[yi][xi-5]/n5_l0+
                                         Raw_Values_condition_2[yi-1][xi-5]/n5_l1) - 
                                 
                                 np.sum(Raw_Values_condition_1[yi][xi-0]/n0_l0+
                                         Raw_Values_condition_1[yi-1][xi-0]/n0_l1+
                                         Raw_Values_condition_1[yi][xi-1]/n1_l0+
                                         Raw_Values_condition_1[yi-1][xi-1]/n1_l1+
                                         Raw_Values_condition_1[yi][xi-2]/n2_l0+
                                         Raw_Values_condition_1[yi-1][xi-2]/n2_l1+
                                         Raw_Values_condition_1[yi][xi-3]/n3_l0+
                                         Raw_Values_condition_1[yi-1][xi-3]/n3_l1+
                                         Raw_Values_condition_1[yi][xi-4]/n4_l0+
                                         Raw_Values_condition_1[yi-1][xi-4]/n4_l1+
                                         Raw_Values_condition_1[yi][xi-5]/n5_l0+
                                         Raw_Values_condition_1[yi-1][xi-5]/n5_l1) ) )
                else:
                    H.append(abs(np.sum(Raw_Values_condition_2[yi][xi+0]/n0_l0+
                                         Raw_Values_condition_2[yi][xi+1]/n1_l0+
                                         Raw_Values_condition_2[yi][xi+2]/n2_l0+
                                         Raw_Values_condition_2[yi][xi+3]/n3_l0+
                                         Raw_Values_condition_2[yi][xi+4]/n4_l0+
                                         Raw_Values_condition_2[yi][xi+5]/n5_l0) -
                                 
                                 np.sum(Raw_Values_condition_1[yi][xi+0]/n0_l0+
                                         Raw_Values_condition_1[yi][xi+1]/n1_l0+
                                         Raw_Values_condition_1[yi][xi+2]/n2_l0+
                                         Raw_Values_condition_1[yi][xi+3]/n3_l0+
                                         Raw_Values_condition_1[yi][xi+4]/n4_l0+
                                         Raw_Values_condition_1[yi][xi+5]/n5_l0 ) ) -
                             
                             abs(np.sum(Raw_Values_condition_2[yi][xi-0]/n0_l0+
                                         Raw_Values_condition_2[yi][xi-1]/n1_l0+
                                         Raw_Values_condition_2[yi][xi-2]/n2_l0+
                                         Raw_Values_condition_2[yi][xi-3]/n3_l0+
                                         Raw_Values_condition_2[yi][xi-4]/n4_l0+
                                         Raw_Values_condition_2[yi][xi-5]/n5_l0) -
                                 
                                 np.sum(Raw_Values_condition_1[yi][xi-0]/n0_l0+
                                         Raw_Values_condition_1[yi][xi-1]/n1_l0+
                                         Raw_Values_condition_1[yi][xi-2]/n2_l0+
                                         Raw_Values_condition_1[yi][xi-3]/n3_l0+
                                         Raw_Values_condition_1[yi][xi-4]/n4_l0+
                                         Raw_Values_condition_1[yi][xi-5]/n5_l0) ) )
    return H

def parseBED(infileName):
    """
    The input file should have only one line with one region of interest.
    I am not checking for that though. I just take the first row and go.
    """
    infile = open(infileName)
    for row in infile:
        tmp = row.strip().split("\t")
        return tmp[0], int(tmp[1]), int(tmp[2])

def getBinsFromRegion(regionBedFile, binSize, outfilePrefix):
    chrom_f, start_f, end_f = parseBED(regionBedFile)
    refBins = []
    for i in range(1, math.ceil((end_f-start_f)/binSize)+1, 1):
        key = (chrom_f, str(end_f-(binSize*i)), str(end_f-(binSize*(i-1))))
#         key = (chrom_f, start_f*i, start_f+((int((end_f-start_f)/binSize)+1-i)*binSize))
        refBins.append(key)
    refBins.reverse()
    outfile = open("{}.binSize_{}.bed".format(outfilePrefix, binSize),'w')
    for b in refBins:
        outfile.write("{}\n".format('\t'.join(str(x) for x in b)))
    outfile.close()
    return refBins



def combineVectors(bdg1_vector_dict, bdg1_vector_order, bdg2_vector_dict, bdg2_vector_order, refBins):
    bdg1_vectorCombined_raw = []
    bdg2_vectorCombined_raw = []
    for key in refBins:
        if key in bdg1_vector_dict:
            bdg1_vectorCombined_raw.append(bdg1_vector_dict[key])
        else:
            bdg1_vectorCombined_raw.append(0)
        if key in bdg2_vector_dict:
            bdg2_vectorCombined_raw.append(bdg2_vector_dict[key])
        else:
            bdg2_vectorCombined_raw.append(0)
    
    return bdg1_vectorCombined_raw, bdg2_vectorCombined_raw, np.max(bdg1_vectorCombined_raw + bdg2_vectorCombined_raw)

def importBDG(infileName):
    infile = open(infileName, 'r')
    vector_dict = {}
    vector_order = []
    for row in infile:
        tmp = row.strip().split("\t")
        key = (tmp[0], tmp[1], tmp[2])
        vector_dict[key] = float(tmp[3])
        vector_order.append(key)
    infile.close()
    return vector_dict, vector_order

def checkDims(Raw_Values_condition_1, Raw_Values_condition_2):
    x1 = len(Raw_Values_condition_1[0])
    y1 = len(Raw_Values_condition_1)
    
    x2 = len(Raw_Values_condition_2[0])
    y2 = len(Raw_Values_condition_2)
    
    if x1 == x2 and y1 == y2:
        print("###\tINFO: input matrixes dimentions match: X = {}; Y = {}".format(x1, y1))
        return x1, y1
    else:
        print("###\tERROR: input matrixes dimentions do not match: X1 = {}; Y1 = {}; X2 = {}; Y2 = {}".format(x1, y1), x2, y2)
        return False, False

def convertRaw2Layers(vectorCombined_raw, layers, maxEnrich):
    vectorCombined_processed = []
    for layer in range(0, layers, 1):
        vectorCombined_processed.append([])
    step = maxEnrich/float(layers)
    print(step)
    for position in vectorCombined_raw:
        layersVector = []
        enrichment = position
        for layer in range(0, layers, 1):
            check = step - enrichment
            if check <= 0:
                fill = 1
                enrichment -= step
            elif check == step:
                fill = 0
                enrichment = 0
            else:
                fill = enrichment/step
                enrichment = 0
            layersVector.append(fill)
        layersVector.reverse()
        for layer, enrichment in zip(range(0, layers, 1), layersVector):
            vectorCombined_processed[layer].append(enrichment)
    return vectorCombined_processed
    
def plotVelocity(input1, input2, binSize, outfilePrefix, regionsBedFile, layers = 5, width = 0.03, scale = 4, yMax = 2.5):
    refBins = getBinsFromRegion(regionsBedFile, binSize, outfilePrefix)
    bdg1_vector_dict, bdg1_vector_order = importBDG(input1)
    
    bdg2_vector_dict, bdg2_vector_order = importBDG(input2)
    bdg1_vectorCombined_raw, bdg2_vectorCombined_raw, maxEnrich = combineVectors(bdg1_vector_dict, bdg1_vector_order, bdg2_vector_dict, bdg2_vector_order, refBins)

    bdg1_vectorCombined = convertRaw2Layers(bdg1_vectorCombined_raw, layers, np.ceil(maxEnrich))
    bdg2_vectorCombined = convertRaw2Layers(bdg2_vectorCombined_raw, layers, np.ceil(maxEnrich))

    Xdim, Ydim = checkDims(bdg1_vectorCombined, bdg2_vectorCombined)
    X, Y = getXYVectors(Xdim, Ydim)
    V = getV(bdg1_vectorCombined, bdg2_vectorCombined, Xdim, Ydim)
    H = getH(bdg1_vectorCombined, bdg2_vectorCombined, Xdim, Ydim)

    Reds_r_mine = make_colormap([ConvertRGB2sth(0,0,255), ConvertRGB2sth(0,0,255), 0.35, ConvertRGB2sth(0,0,255), ConvertRGB2sth(255,255,255), 0.5, ConvertRGB2sth(255,255,255), ConvertRGB2sth(255,0,0), 0.65, ConvertRGB2sth(255,0,0), ConvertRGB2sth(255,0,0)])

    plt.clf()
    fig, ax1 = plt.subplots(figsize=(10, 4))
    Q = ax1.quiver(X, Y, H, V, V, width=width, pivot='mid',scale=scale , units='inches', cmap=Reds_r_mine)
    
    Q.set_clim(-1, 1)

    ax1.set_ylim([-0,yMax])
    
    plt.title(outfilePrefix)
    fig.savefig("{}.VelocityPlot.pdf".format(outfilePrefix), dpi=300, bbox_inches='tight')
    
    print(V)
