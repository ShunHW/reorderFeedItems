class FeedItem:
    def __init__(self,itemId,title,pics,author,category):
        self.itemID = itemId
        self.title = title
        self.pics = pics
        self.author = author
        self.category = category

def reorderFreedItem(inputItems):
    queue = []
    queue.append(inputItems.pop(0))
    count = 0
    while len(queue) < 10:
        flag = 0
        # 同时满足2.2 2.3
        for i in range(len(inputItems)):
            if inputItems[i].author != queue[-1].author:
                if inputItems[i].category == queue[-1].category:
                    count += 1
                    if count >= 2:
                        continue
                else:
                    count = 0
                queue.append(inputItems.pop(i))
                flag = 1
                break
        # 只满足2.2
        if flag == 0:
            for i in range(len(inputItems)):
                if inputItems[i].author != queue[-1].author:
                    if inputItems[i].category != queue[-1].category:
                        count = 0
                    queue.append(inputItems.pop(i))
                    flag = 1
                    break
        # 满足不了2.2 2.3
        if flag == 0:
            n = len(queue)
            queue += inputItems[:10-n]
    return queue

if __name__ == '__main__':
    input = []
    input.append(FeedItem(None,None,None,'a', 1))
    input.append(FeedItem(None,None,None,'a', 2))
    input.append(FeedItem(None,None,None,'b', 1))
    input.append(FeedItem(None,None,None,'c', 2))
    input.append(FeedItem(None,None,None,'d', 2))
    input.append(FeedItem(None,None,None,'d', 3))
    input.append(FeedItem(None,None,None,'a', 1))
    input.append(FeedItem(None,None,None,'b', 1))
    input.append(FeedItem(None,None,None,'v', 2))
    input.append(FeedItem(None,None,None,'a', 2))
    input.append(FeedItem(None,None,None,'a', 2))
    input.append(FeedItem(None,None,None,'d', 2))
    output = reorderFreedItem(input)
    for i in output:
        print(i.author,i.category)