import numpy as np
from matplotlib import pyplot as plt
import cv2
import ocr
import erc
import beautifier as bf

def get(str):
    str = "TestImages/" + str
    t = cv2.imread(str, 1)
    t2 = cv2.cvtColor(t, cv2.COLOR_BGR2GRAY)
    return t.copy(), t2.copy()

def stringer(l):
    st = ''
    for i in l:
        st = st + (i + ' ')
    st = st + '\n'
    return st

def generateSentence(di, shape):
    dj = dict()
    if di['regions'] == []:
        return
    else:
        dj['words'] = []
        for i in di["regions"][0]["lines"][0]["words"]:
            dj['words'].append(i['text'])
        dj['type'] = shape
    print dj
    return dj

def put(im):
    cv2.imshow("out", im)
    return cv2.waitKey(5) & 0xFF

#def daq(r, f, d, c, l):

def repository(repo, count):
    for i in range(1, count+1):
        repo[i]['no'] = None
        repo[i]['yes'] = None
        repo[i]['root'] = 0
        for j in range(1, count+1):
            if i == j: continue
            if repo[i]['type'] == 'input':
                repo[i]['root'] = 1
                if abs(repo[j]['cx'] - repo[i]['cx']) <= 10:
                    if repo[i]['no']== None:
                        repo[i]['no'] = j
            elif repo[i]['type'] == 'operation':
                if abs(repo[j]['cx'] - repo[i]['cx']) <= 10:
                    if repo[i]['no']== None:
                        repo[i]['no'] = j
            elif repo[i]['type'] == 'decision':
                if abs(repo[j]['cx'] - repo[i]['cx']) <= 10 and repo[j]['cy'] > repo[i]['cy']:
                    repo[i]['type'] = 'loop'
                    if repo[i]['no']== None:
                        repo[i]['no'] = j
                elif abs(repo[j]['cy'] - repo[i]['cy']) <= 10:
                    if repo[i]['no']== None:
                        repo[i]['no'] = j
                    else:
                        repo[i]['type'] = 'if'
                        repo[i]['yes'] = j
    bf.printer(repo)
    decs = 0
    fin = str('')

def getFinal(name):
    #Predefinition and Setup
    repo = {}
    count = 0
    im, grey = get(name)
    cp = im.copy()
    if im == None:
        return 1

    kernel = np.ones([1,1], np.uint8)
    no = 0

    #Start Processing
    #Image Rendering

    blurred = cv2.GaussianBlur(grey, (5, 5), 0)
    threshed = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    threshed = cv2.dilate(threshed, kernel, iterations = 1)
    threshi = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    #Identifying Contours

    image, contours, hier = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    st = 0
    contours = contours[::-1]
    first = 1

    #Isolating Relevant Contours & Classifiying relevant shapes

    for cnt in contours:
        epsilon = 0.02*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        a = cv2.contourArea(cnt)
        if a < 5300 or a > 24000:
            continue
        if st == 1:
            st = 0
        else:
            st = 1
            continue
        #fin = cv2.drawContours(cp, [cnt], 0, (0,0,255), 1

        fin = cv2.drawContours(cp, [cnt], 0, (0,0,255), 1)
        if put(fin) == ord('q'):
            break

        if len(approx)==4:
            #print approx
            no = 0
            shape = "decision"
            for i in range(1,4):
                if abs(approx[0,0,0]-approx[i,0,0]) <= 4:
                    no += 1
                if abs(approx[0,0,1]-approx[i,0,1]) <= 4:
                    no += 1
            if no == 2:
                shape = "operation"
        else:
            if first:
                shape = "input"
                first = 0
            else:
                shape = "output"

        print shape

        #Isolating Text for OCR

        x,y,w,h = cv2.boundingRect(cnt)
        chars = im[y:(y+h),x:(x+w),:]
        count += 1

        M = cv2.moments(cnt)

        #Displaying Sample Image for OCR

        cv2.imwrite(str("OutPutImages/" + str(count)) + ".jpg",chars)
        f = open("OutPutImages/" + str(count) + ".jpg", "rb")
        data = f.read()
        d = ocr.getter(data)

        #Generating Natural Language Sentence

        repo[count] = generateSentence(d, shape)
        repo[count]['cx'] = int(M['m10']/M['m00'])
        repo[count]['cy'] = int(M['m01']/M['m00'])
        put(chars)
        no += 1
        #fin = cv2.drawContours(cp, [approx], 0, (255,0,0), 1)

    #finalizing

    cv2.destroyAllWindows()
    print "Final Results:\n", repo

    #Generating Final code in Natural Language to send to NLP Section

    code = repository(repo, count) # THIS VARIABLE "code" CONTAINS THE FINAL CODE.
    print code
    return code

if __name__ == '__main__':
    getFinal("flow.jpg")
    getFinal("flow2.jpg")
    getFinal("flow3.jpg")
