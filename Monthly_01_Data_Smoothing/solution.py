def smooth(y, halfWindowSize=70):
    smoothedData = []
    for x in range(halfWindowSize, len(y)-halfWindowSize):
        total = 0
        for i in range(-halfWindowSize, halfWindowSize):
            total += y[x+i]
            average = total / (halfWindowSize * 2)
        smoothedData.append(average)
    return smoothedData
