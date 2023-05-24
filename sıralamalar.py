import time
import winsound


class Sortings:
    def __init__(self):
        self.comparison_count = 0  # Karşılaştırma sayısını takip etmek için değişken

    def insertion_sort(self, data, drawData, timeTick):
        self.comparison_count = 0  # Karşılaştırma sayısını sıfırla
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                self.comparison_count += 1  # Karşılaştırma sayısını artır
                data[j + 1] = data[j]
                j -= 1
                drawData(data, ['green' if x == j + 1 else 'white' for x in range(len(data))])
                time.sleep(timeTick)
            data[j + 1] = key
            drawData(data, ['green' if x == j + 1 else 'white' for x in range(len(data))])
            time.sleep(timeTick)
        self.complete_sorting()  # Sıralama tamamlandığında sonuçları göster

    def bubble_sort(self, data, drawData, timeTick):
        self.comparison_count = 0  # Karşılaştırma sayısını sıfırla
        for _ in range(len(data) - 1):
            for j in range(len(data) - 1):
                self.comparison_count += 1  # Karşılaştırma sayısını artır
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    drawData(data, ['green' if x == j or x == j + 1 else 'white' for x in range(len(data))])
                    time.sleep(timeTick)
        self.complete_sorting()  # Sıralama tamamlandığında sonuçları göster

    def selection_sort(self, data, drawData, timeTick):
        self.comparison_count = 0  # Karşılaştırma sayısını sıfırla
        for i in range(len(data) - 1):
            min_idx = i
            for j in range(i + 1, len(data)):
                self.comparison_count += 1  # Karşılaştırma sayısını artır
                if data[min_idx] > data[j]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            drawData(data, ['green' if x == min_idx or x == i else 'red' for x in range(len(data))])
            time.sleep(timeTick)
        self.complete_sorting()  # Sıralama tamamlandığında sonuçları göster

    def partition(self, data, left, right, drawData, timeTick):
        border = left
        pivot = data[right]

        drawData(data, self.get_color_array(len(data), left, right, border, border))
        time.sleep(timeTick)

        for j in range(left, right):
            if data[j] < pivot:
                self.comparison_count += 1  # Karşılaştırma sayısını artır
                drawData(data, self.get_color_array(
                    len(data), left, right, border, j, True))
                time.sleep(timeTick)

                data[border], data[j] = data[j], data[border]
                border += 1

            drawData(data, self.get_color_array(len(data), left, right, border, j))
            time.sleep(timeTick)

        # pivot ile border değerini takas et
        drawData(data, self.get_color_array(len(data), left, right, border, right, True))
        time.sleep(timeTick)

        data[border], data[right] = data[right], data[border]

        return border

    def quick_sort(self, data, left, right, drawData, timeTick):
        if left < right:
            partitionIdx = self.partition(data, left, right, drawData, timeTick)
            self.quick_sort(data, left, partitionIdx - 1, drawData, timeTick)
            self.quick_sort(data, partitionIdx + 1, right, drawData, timeTick)

    def merge_sort(self, data, drawData, timeTick):
        self.comparison_count = 0  # Karşılaştırma sayısını sıfırla
        self.merge_sort_alg(data, 0, len(data) - 1, drawData, timeTick)
        self.complete_sorting()  # Sıralama tamamlandığında sonuçları göster

    def merge_sort_alg(self, data, left, right, drawData, timeTick):
        if left < right:
            middle = (left + right) // 2
            self.merge_sort_alg(data, left, middle, drawData, timeTick)
            self.merge_sort_alg(data, middle + 1, right, drawData, timeTick)
            self.merge(data, left, middle, right, drawData, timeTick)

    def merge(self, data, left, middle, right, drawData, timeTick):
        drawData(data, self.get_color_array_merge(len(data), left, middle, right))
        time.sleep(timeTick)

        leftPart = data[left:middle + 1]
        rightPart = data[middle + 1:right + 1]

        leftIdx = rightIdx = 0

        for dataIdx in range(left, right + 1):
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                self.comparison_count += 1  # Karşılaştırma sayısını artır
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

    def get_color_array(self, data_len, left, right, border, currIdx, isSwapping=False):
        colorArray = []
        for i in range(data_len):
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

            if isSwapping:
                if i == border or i == currIdx:
                    colorArray[i] = 'green'

        return colorArray

    def get_color_array_merge(self, length, left, middle, right):
        colorArray = []

        for i in range(length):
            if i >= left and i <= right:
                if i >= left and i <= middle:
                    colorArray.append("yellow")
                else:
                    colorArray.append("pink")
            else:
                colorArray.append("white")

        return colorArray

    def complete_sorting(self):
        for i in range(2):
            winsound.Beep(2500, 300)
            time.sleep(0.05)
        print("Karşılaştırma Sayısı:", self.comparison_count)