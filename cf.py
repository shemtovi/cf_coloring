import sys
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

max_color_per_level = [-1]
max_level=0

class point:
    def __init__(self, level ,color, prev, next):
        self.level= level
        self.color= color
        self.prev = prev
        self.next = next

def main():
    head= None
    pointsCounter = 0 #points counter
    while True:
        index = int(input("please insert index between 0 and {}\n".format(pointsCounter)))
        if index<0 or index> pointsCounter:
            print("please insert a valid index\n")
        else:
            
            prev= None
            next = None
            if(index == 0):
                next = head
            else:
                j=1
                prev = head
                while (j<index):
                    prev = prev.next
                    j=j+1
                if prev != None:
                    next = prev.next
            level = getLevel(prev,next)
            color = getColor(level,prev,next)
            newPoint = point(level,color,prev,next)
            if prev != None: prev.next = newPoint
            if next != None: next.prev = newPoint
            if index == 0:
                head = newPoint
            pointsCounter=pointsCounter+1    
            curr = head
            while(curr!=None): # print for debug
                print("current point is: level-{}, color-{}".format(curr.level, curr.color))
                curr = curr.next
            print_2plot(head, pointsCounter)

def print_plot(head, pointsCounter):
    plt.close()
    x = [num for num in range(1, pointsCounter + 1)]
    y = linked_list_to_list(head)
    z = get_colors_list(head)
    # Set unique colors for each color value
    unique_colors = list(set(z))

    # Generate a color map based on the number of unique colors
    cmap = plt.cm.get_cmap('viridis', len(unique_colors))

    # Create the scatter plot
    plt.scatter(x, y, c=z, cmap=cmap)

    # Add a colorbar legend
    cbar = plt.colorbar()
    cbar.set_ticks(unique_colors)
    cbar.set_label('Color')
    # Plotting the dots
    # plt.scatter(x, y)
    # Adding labels and title
    plt.grid(axis='y', linestyle='--')
    plt.xticks(range(0, max(x) + 2))
    plt.yticks(range(0, max(y) + 2))
    plt.xlabel('Index')
    plt.ylabel('Level')
    plt.title('Coloring-Free Graph')
    # Display the graph
    plt.show(block=False)
    

def print_2plot(head, pointsCounter):
    plt.close()
    x1 = [num for num in range(1, pointsCounter + 1)]
    y1 = linked_list_to_list(head)
    z1 = get_colors_list(head)
    unique_colors = list(set(z1))

    # Generate a color map based on the number of unique colors
    cmap = plt.cm.get_cmap('viridis', len(unique_colors))

    y2 = [1 for num in range(1, pointsCounter + 1)]

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Plot first graph on the first subplot
    ax1.scatter(x1, y1, c=z1, cmap=cmap)
    ax1.set_xlabel('X1')
    ax1.set_ylabel('Y1')
    ax1.set_title('Graph 1')

    # Plot second graph on the second subplot
    ax1.scatter(x1, y2, c=z1, cmap=cmap)
    ax2.set_xlabel('X2')
    ax2.set_ylabel('Y2')
    ax2.set_title('Graph 2')

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Display the figure with both graphs
    plt.show()    

def get_colors_list(head):
    global max_color_per_level
    global max_level
    adding_list = [0]
    index = 0
    #for i in range(1,len(max_color_per_level)-1):
    for num in max_color_per_level: 
        adding_list.append(num + adding_list[index] +1)
        index = index + 1
    arr = []
    curr = head
    while(curr != None):
        arr.append(curr.color + adding_list[curr.level])
        curr = curr.next
    return arr    


def linked_list_to_list(head):
    result = []
    current = head
    while current is not None:
        result.append(current.level)
        current = current.next
    return result

def getLevel(prev, next):
    global max_color_per_level
    global max_level
    rightList = seesRight(next)
    leftList = seesLeft(prev)
    level = min(findMin(rightList),findMin(leftList))
    if level>max_level:
        max_level = level
        max_color_per_level.append(-1)
    return level

def getColor(level,prev, next):
    global max_color_per_level
    rightListLevel = seesRightColor(next, level)
    leftListLevel = seesLeftColor(prev, level)
    rightSet = set()
    leftLeft = set()
    maxColor = -1
    for color in rightListLevel:
        if color > maxColor: rightSet.add(color)
    maxColor = -1    
    for color in leftListLevel:
        if color > maxColor: leftLeft.add(color)
    merged_set = rightSet.union(leftLeft) 
    color = 0
    while color < len(merged_set):
        if color in merged_set: 
            color = color + 1
        else: 
            if color> max_color_per_level[level]:
                max_color_per_level[level]= color
            return color  
    if color> max_color_per_level[level]:
        max_color_per_level[level]= color
    return color


def seesLeftColor(curr ,level):
    arr= []
    while (curr!=None and curr.level <= level):
        if curr.level ==  level:
            arr.append(curr.color)
        curr = curr.prev
    return arr

    
def seesRightColor(curr, level):       
    arr= []
    while (curr!=None and curr.level <= level):
        if curr.level ==  level:
            arr.append(curr.color)
        curr = curr.next
    return arr

def seesRight(curr):
    arr= []
    currMax = 0
    while (curr!=None):
        if curr.level>  currMax:
            arr.append(curr.level)
            currMax = curr.level
        curr = curr.next
    return arr

def seesLeft(curr):
    arr= []
    currMax = 0
    while (curr!=None):
        if curr.level>  currMax:
            arr.append(curr.level)
            currMax = curr.level
        curr = curr.prev
    return arr

def findMin(list):
    level = 1
    i=0
    for num in list:
        if num != level:
            return level
        else: 
            level= level+1
    return level

if __name__ == "__main__":
    main()