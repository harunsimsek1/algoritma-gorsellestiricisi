import time
import winsound


class Sortings:
    
    # Diğer sıralama metotları burada tanımlanmış olsun

    # EKLEME SIRALAMASI (INSERTION SORT)
    def insertion_sort(self, data, drawData, timeTick):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
                drawData(data, ['green' if x == j+1 else 'white' for x in range(len(data))])
                time.sleep(timeTick)
            data[j + 1] = key
            drawData(data, ['green' if x == j+1 else 'white' for x in range(len(data))])
            time.sleep(timeTick)
        for i in range(2):
            winsound.Beep(2500, 300)
            time.sleep(0.05)
        drawData(data, ['green' for x in range(len(data))])

    
    
    # BUBBLE SORT
    def bubble_sort(self,data, drawData, timeTick):
        for _ in range(len(data)-1):
            for j in range(len(data)-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    drawData(data, ['green' if x == j or x == j+1 else 'white' for x in range(len(data))] )
                    time.sleep(timeTick)
        for i in range(2):
            winsound.Beep(2500, 300)
            time.sleep(0.05)
        drawData(data, ['green' for x in range(len(data))])

    # SELECTION SORT
    def selection_sort(self,data, drawData, timeTick):
        for i in range(len(data)-1):

            min_idx = i
            for j in range(i+1, len(data)):
                if data[min_idx] > data[j]: 
                    min_idx = j
                    
            data[i], data[min_idx] = data[min_idx], data[i]
            drawData(data, ['green' if x == min_idx or x == i else 'red' for x in range(len(data))] )
            time.sleep(timeTick)
        for i in range(2):
            winsound.Beep(2500, 300)
            time.sleep(0.05)
        drawData(data, ['green' for x in range(len(data))])

    

    # QUICK SORT
    def partition(self,data, left, right, drawData, timeTick):
        border = left
        pivot = data[right]

        drawData(data, self.getColorArray(len(data), left, right, border, border))
        time.sleep(timeTick)

        for j in range(left, right):
            if data[j] < pivot:
                drawData(data, self.getColorArray(
                    len(data), left, right, border, j, True))
                time.sleep(timeTick)

                data[border], data[j] = data[j], data[border]
                border += 1

            drawData(data, self.getColorArray(len(data), left, right, border, j))
            time.sleep(timeTick)

        #swap pivot with border value
        drawData(data, self.getColorArray(len(data), left, right, border, right, True))
        time.sleep(timeTick)

        data[border], data[right] = data[right], data[border]

        return border


    def quick_sort(self,data, left, right, drawData, timeTick):
        if left < right:
            partitionIdx = self.partition(data, left, right, drawData, timeTick)

            #LEFT PARTITION
            self.quick_sort(data, left, partitionIdx-1, drawData, timeTick)

            #RIGHT PARTITION
            self.quick_sort(data, partitionIdx+1, right, drawData, timeTick)


    def getColorArray(self,dataLen, left, right, border, currIdx, isSwaping=False):
        colorArray = []
        for i in range(dataLen):
            #base coloring
            if i >= left and i <= right:
                colorArray.append('gray')
            else:
                colorArray.append('white')

            if i == right:
                colorArray[i] = 'blue'
            elif i == border:
                colorArray[i] = 'red'
            elif i == currIdx:
                colorArray[i] = 'yellow'

            if isSwaping:
                if i == border or i == currIdx:
                    colorArray[i] = 'green'

        return colorArray

    # MERGE SORT
    def merge_sort(self,data, drawData, timeTick):
        self.merge_sort_alg(data, 0, len(data)-1, drawData, timeTick)
        for i in range(2):
            winsound.Beep(2500, 300)
        time.sleep(0.05)


    def merge_sort_alg(self,data, left, right, drawData, timeTick):
        if left < right:
            middle = (left + right) // 2
            self.merge_sort_alg(data, left, middle, drawData, timeTick)
            self.merge_sort_alg(data, middle+1, right, drawData, timeTick)
            self.merge(data, left, middle, right, drawData, timeTick)


    def merge(self,data, left, middle, right, drawData, timeTick):
        drawData(data, self.getColorArrayMerge(len(data), left, middle, right))
        time.sleep(timeTick)

        leftPart = data[left:middle+1]
        rightPart = data[middle+1: right+1]

        leftIdx = rightIdx = 0

        for dataIdx in range(left, right+1):
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                if leftPart[leftIdx] <= rightPart[rightIdx]:
                    data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                else:
                    data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1

            elif leftIdx < len(leftPart):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        drawData(data, ["green" if x >= left and x <=
                        right else "white" for x in range(len(data))])
        time.sleep(timeTick)


    def getColorArrayMerge(self,leght, left, middle, right):
        colorArray = []

        for i in range(leght):
            if i >= left and i <= right:
                if i >= left and i <= middle:
                    colorArray.append("yellow")
                else:
                    colorArray.append("pink")
            else:
                colorArray.append("white")

        return colorArray
    
   

