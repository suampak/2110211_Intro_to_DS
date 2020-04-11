import heapq

def huffman_code(counts):
    ret = {}
    heap = []
    for ch in counts:
        ret[ch] = []
        heapq.heappush(heap,(counts[ch],[ch]))

    while len(heap) >= 2:
        count1, char1 = heapq.heappop(heap)
        count2, char2 = heapq.heappop(heap)
        for ch in char1:
            ret[ch].append(0)
        for ch in char2:
            ret[ch].append(1)
        heapq.heappush(heap,(count1+count2,char1+char2))

    for ch in ret:
        ret[ch].reverse()

    return ret

if __name__ == '__main__':
    counts = {'a':40, 'b':21, 'c':15, 'd':14, 'e':8, 'f':2}
    print huffman_code(counts)