import matplotlib.pyplot as plt
import seaborn as sns
import copy

################################################################################################ Preprocessing


with open("datapoints.txt", "r") as file:
    TRAINING_ROWS = [row.strip("\n").split(", ") for row in file.readlines()[1:]]

TRAINING_POINTS = []
for training_row in TRAINING_ROWS:
    formated_training_rows = [int(value) if value.isdigit() else float(value) for value in training_row ]
    TRAINING_POINTS.append(formated_training_rows)


TRAINING_WIDTH = [r[0] for r in TRAINING_POINTS]
TRAINING_HEIGHT = [r[1] for r in TRAINING_POINTS]
TRAINING_LABEL = [r[2] for r in TRAINING_POINTS]

TRAINING_COLUMNS = {'Width':TRAINING_WIDTH, 'Height':TRAINING_HEIGHT, 'Label':TRAINING_LABEL}

##########################################


with open("testpoints.txt", "r") as file:
    TEST_ROWS = [row[4:].strip("\n").split(", ") for row in file.readlines()[1:]]
    
TEST_ROWS = [i[:1] + [i[1][:-1]] for i in TEST_ROWS]

TEST_WIDTH = [float(v[0]) for v in TEST_ROWS]
TEST_HEIGHT = [float(v[1]) for v in TEST_ROWS]


TEST_POINTS = []
for test_row in TEST_ROWS:
    formated_testing_rows = [ [float(value) for value in test_row ] ]
    TEST_POINTS.append(formated_testing_rows)


################################################################################################ Function
    
def graph(TRAINING_COLUMNS):

    sns.relplot(data=TRAINING_COLUMNS, x='Width', y='Height', hue='Label', hue_order=[0,1])
    plt.show()

#https://stackoverflow.com/questions/14885895/color-a-scatter-plot-by-column-values


##########################################


def calculate_distance(TEST_WIDTH, TEST_HEIGHT, TRAINING_COLUMNS, TRAINING_POINTS):

    DISTANCES = []
    for p1, p2 in zip(TEST_WIDTH, TEST_HEIGHT):

        distance_list = [ ( (p1-qx)**2  + (p2-qy)**2 )**(1/2) for qx, qy in zip(TRAINING_COLUMNS['Width'], TRAINING_COLUMNS['Height']) ]

        DISTANCES.append(distance_list)


    DISTANCES_COPY = copy.deepcopy(DISTANCES)
    CLOSEST_NEIGHBOUR = []

    for i in DISTANCES_COPY:
        i.sort()
        CLOSEST_NEIGHBOUR.append(i[:10])


    NEIGHBOURS = [] #index till 10 närmsta grannarna för alla 4 testdata rader 
    for idx, l in enumerate(CLOSEST_NEIGHBOUR):
        
        neighbours_list = [DISTANCES[idx].index(v) for v in l ]
        
        NEIGHBOURS.append(neighbours_list)


    NEIGHBOURS_IDX = []
    for nl in NEIGHBOURS:
        neighbours_idx_list = [TRAINING_POINTS[n] for n in nl] 
        NEIGHBOURS_IDX.append(neighbours_idx_list)


    classifying(NEIGHBOURS_IDX, TEST_POINTS)


##########################################

def classifying(NEIGHBOURS_IDX, TEST_POINTS):

    for idx, i in enumerate(NEIGHBOURS_IDX):
        neighbour_pikachu = 0
        for ii in i:
            neighbour_pikachu += ii.count(1)

        if neighbour_pikachu >= 5:
            print(f"Sample with (width, height) ({str(TEST_POINTS[idx][0])[1:-1]}) classified as Pikachu")
        else:
            print(f"Sample with (width, height) ({str(TEST_POINTS[idx][0])[1:-1]}) classified as Pichu")


##########################################


def add_test_points():

    width = input("Enter width: ")
    height = input("Enter height: ")

    with open("testpoints.txt") as file:
        nr_of_rows = len(file.readlines())


    new_test_points = f"{nr_of_rows}. ({width}, {height})" + '\n'

    with open("testpoints.txt", "a") as file:
        file.write(new_test_points)


##########################################

#Ta med felhanteringen
#som tar hand om negativa tal och icke-numeriska inputs. 
# Se till att ha användarvänliga felmeddelanden

print("###Pichu or Pikachu?###")
print("[1] Plot datapoints")
print("[2] Pichu or Pickahu?")
print("[3] Add datapoints")
print("What would you like to do?")

    
while True:
    choice = int(input("Pick number from 1-3"))
    if choice == 1:
        graph(TRAINING_COLUMNS)
    elif choice == 2:
        calculate_distance(TEST_WIDTH, TEST_HEIGHT, TRAINING_COLUMNS, TRAINING_POINTS)
    elif choice == 3:
        add_test_points()

    


