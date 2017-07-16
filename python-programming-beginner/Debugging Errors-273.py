## 2. Syntax Errors ##

def first_elts (input_lst):
elts = []
    for each in input_lst:
        elts.append(each0)
    retern elts

animals = [["dog","cat","rabbit"],["turtle","snake"],["sloth","penguin","bird"]]
first_animal = first_elts(animals)
print(first_animal)


## 4. TypeError and ValueError ##

forty_two = 42
forty_two + "42"

float("guardians")


## 5. IndexError and AttributeError ##

lives = [1,2,3]
lives[4]

f = open("story.txt")
f.split(" ")


## 6. Traceback ##

def summary_statistics(input_lst):
    num_japan_films = feature_counter(input_lst,6,"Japan",True)
    num_color_films = feature_counter(input_lst,2,"Color",True)
    num_films_in_english = feature_counter(input_lst,5,"English",True)
    summary_dict = {"japan_films" : num_japan_films, "color_films" : num_color_films, "films_in_english" : num_films_in_english}
    return summary_dict

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == Treu:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

summary = summary_statistics(movie_data)
print(summary)
