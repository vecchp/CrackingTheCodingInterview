from collections import namedtuple
from random import sample
from operator import attrgetter


def is_greater(a, b):
    if a is None:
        return True
    l = a.length < b.length
    w = a.width < b.width
    h = a.height < b.height
    return l and w and h


def stacks(boxes, cur=None, lst=None):
    if cur is None:
        cur = []
    if lst is None:
        lst = []

    can_add = True
    for i, b in enumerate(boxes):
        if not cur or is_greater(b, cur[-1]):
            can_add = False
            stacks(boxes[i + 1:], cur + [b], lst)

    if can_add:
        lst.append(cur)

    return lst


def createStack(boxes, bottom_idx, stackmap=None):

    if bottom_idx < len(boxes) and stackmap[bottom_idx] > 0:
        return stackmap[bottom_idx]

    bottom = boxes[bottom_idx]
    max_height = 0

    for i in range(bottom_idx + 1, len(boxes)):
        if is_greater(boxes[i], bottom):
            height = createStack(boxes, i, stackmap)
            max_height = max(height, max_height)

    max_height += bottom.height
    stackmap[bottom_idx] = max_height
    return max_height


def creatStackDriver(boxes):
    max_height = 0
    stack_map = [0]*len(boxes)
    for i in range(0, len(boxes)):
        height = createStack(boxes, i, stack_map)
        max_height = max(height, max_height)
    return max_heigh


def main():
    Box = namedtuple('Box', ['length', 'width', 'height'])
    boxes = (Box(*sample(range(10), 3)) for _ in range(0, 30))
    boxes = sorted(boxes, key=attrgetter('height'), reverse=True)
    s = stacks(boxes)

    max_height = 0
    for entry in s:
        cur_sum = 0
        for box in entry:
            cur_sum += box.height
        if cur_sum > max_height:
            max_height = cur_sum
    print(max_height)
    print(creatStackDriver(boxes))


if __name__ == '__main__':
    main()
