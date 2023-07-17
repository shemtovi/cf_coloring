import matplotlib.pyplot as plt

max_color_per_level = [-1]
real_color_arr = [[]]
max_level=0
next_color = 0

class point:
    def __init__(self, level ,color, prev, next):
        self.level= level
        self.color= color
        self.prev = prev
        self.next = next

def main():
    global terminete
    head= None
    pointsCounter = 0 #points counter
    index = 0
    while index != -1:
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
            index = print_plot(curr,pointsCounter)
            

def print_plot(head, pointsCounter):
    plt.close()
    # Set up the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1)

    # Data for the first scatter graph
    x = [num for num in range(1, pointsCounter + 1)]
    y = linked_list_to_list(head)
    z = get_colors_list(head)
    unique_colors = []
    for color in set(z):
        unique_colors.append(color)

    cmap = plt.cm.get_cmap('tab20', len(unique_colors))

    # Plot the first scatter graph on the first subplot
    sc1 = ax1.scatter(x, y, c=z, cmap=cmap)
    ax1.grid(axis='y', linestyle='--')
    # Configure x-axis and y-axis ticks on the first graph
    ax1.set_xticks(range(0, max(x) + 2))
    ax1.set_yticks(range(0, max(y) + 2))
    ax1.set_xlabel('Index')
    ax1.set_ylabel('Level')
    ax1.set_title('Level Graph Algorithm 1')

    # Add a colorbar legend for the first scatter graph
    cbar1 = plt.colorbar(sc1, ax=ax1)
    cbar1.set_ticks(range(len(unique_colors)))
    cbar1.set_ticklabels(unique_colors)
    cbar1.set_label('Color')


    y2 = [1 for num in range(1, pointsCounter + 1)]  # Modify this based on your second graph's y-values

    # Plot the second scatter graph on the second subplot
    ax2.scatter(x, y2, c=z, cmap=cmap)
    ax2.grid(axis='y', linestyle='--')
    ax2.set_xticks(range(0, max(x) + 2))
    ax2.set_yticks(range(1, 2))
    ax2.set_xlabel('Index')
    ax2.set_title('Conflict-Free uniq maximum Graph 2')

    x_click=[]
    def on_click(event):
            # Check if the click is within the plot area
            if event.inaxes == ax2:
                x_click.append(event.xdata)
    # Connect the onclick event handler to the figure
    def on_close(event):
        global terminate
        terminate = True
        x_click.append(-1)
    # Connect the close event handler function
    fig.canvas.mpl_connect('button_press_event', on_click)
    fig.canvas.mpl_connect('close_event', on_close)

    # Adjust the spacing between subplots
    plt.tight_layout()
    # Display the graphs
    plt.show(block=False)
    #return x_click
    while not x_click:
        plt.waitforbuttonpress()
    return int(x_click[0])

def get_colors_list(head):
    arr = []
    curr = head
    while(curr != None):
        arr.append(real_color_arr[curr.level][curr.color])
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
    global real_color_arr
    rightList = seesRightLevels(next)
    leftList = seesLeftLevels(prev)
    level = min(findMin(rightList),findMin(leftList))
    if level>max_level:
        max_level = level
        max_color_per_level.append(-1)
        real_color_arr.append([])
    return level

def getColor(level,prev, next):
    global next_color
    global max_color_per_level
    global real_color_arr
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
                real_color_arr[level].append(next_color)
                next_color = next_color + 1
            return color  
    if color> max_color_per_level[level]:
        max_color_per_level[level]= color
        real_color_arr[level].append(next_color)
        next_color = next_color + 1
    return color


def seesLeftColor(curr ,level):
    arr= []
    currMaxColor = -1
    while (curr!=None and curr.level <= level):
        if curr.level ==  level and curr.color > currMaxColor:
            arr.append(curr.color)
            currMaxColor = curr.color
        curr = curr.prev
    return arr

    
def seesRightColor(curr, level):       
    arr= []
    currMaxColor = -1
    while (curr!=None and curr.level <= level):
        if curr.level ==  level and curr.color > currMaxColor:
            arr.append(curr.color)
            currMaxColor = curr.color
        curr = curr.next
    return arr

def seesRightLevels(curr):
    arr= []
    currMaxLevel = 0
    while (curr!=None):
        if curr.level>  currMaxLevel:
            arr.append(curr.level)
            currMaxLevel = curr.level
        curr = curr.next
    return arr

def seesLeftLevels(curr):
    arr= []
    currMaxLevel = 0
    while (curr!=None):
        if curr.level>  currMaxLevel:
            arr.append(curr.level)
            currMaxLevel = curr.level
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