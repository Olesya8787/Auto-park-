#Auto-park

# DB ->
#       named as auto =>
#                       [ scheme of auto :
#                           {
#                              "label" : ... ,
#                              "price" : ... ,
#                              "wheels" : ... ,
#                              "color" : ... ,
#                              "number" : "random value"
#                           }
#                        ]

# Amount of auto > 10
# color : red , green , black , yellow , blue
# label : more than 5
# price : from 2000 till 200 000
# number and number length > 12
# Form category dictionary :
# dynamic
# cheap (2000 - 20000) , expensive(100000 - 200000) , medium - (20000 - 100000) - class car
# def sort_car_by_price (arr)
# return {
#   cheap : [],
#   medium : [],
#   expensive : []
# }
# print( cars that we have : for poor , rich , and medium-lvl persons )
# input -> sort : color -> choose on of : blue , green , ... ;  price , label

import random 

def show_named_as_auto(named_as_auto):
    for key,values  in named_as_auto.items():
        print(key,values) 

def filter_car_by_price(car_array):
    cheap_car = []
    medium_car = []
    expensive_car = []
    for car_item  in car_array :
              
        if car_item['price'] >= 2000 and car_item['price'] < 20000 :
           cheap_car.append(car_item)
              
        elif car_item['price'] >= 20000 and car_item['price'] < 100000 :
            medium_car.append(car_item)
                
        elif car_item['price'] >= 100000 and car_item['price'] <= 200000 :
            expensive_car.append(car_item)   
    return {
        "cheap" : cheap_car,
        "medium" : medium_car,
        "expensive" : expensive_car
    }

def filter_car_by_color(car_array):  
    color_car = set()
    
    for item in car_array :
        color_car.add(item['color'])
    color_car_array = list(color_car)
    for index in range(len(color_car_array)):
        print(index, ":",color_car_array[index])
    color_index = input("Choose a color car: ")    
    print(color_car_array[int(color_index)]) 
    for item in car_array : 
        if item["color"] == color_car_array[int(color_index)]:
                print (item)                       

def prepare_data(named_as_auto):
    data_car = []
    for key,values  in named_as_auto.items():
        for item  in  values:
            data_car.append({**item, "label":key, "wheels" : 4, "number": random.randint(100000000000,999999999999)})    
    return data_car
                 
named_as_auto = {
    "Ford" :[
        {
            "price" : 10000,
            "wheels" : "",
            "color" : "black",
            "number" : "random value"

        },
        {
            "price" : 15000,
            "wheels" : "",
            "color" : "red",
            "number" : "random value"

        },
    ],
    "Audi" :[
        {
            "price" : 30000,
            "wheels" : "",
            "color" : "yellow",
            "number" : "random value"

        },
        {
            "price" : 50000,
            "wheels" : "",
            "color" : "blue",
            "number" : "random value"

        },
    ],
    "Porsche" :[
        {
            "price" : 110000,
            "wheels" : "",
            "color" : "green",
            "number" : "random value"

        },
        {
            "price" : 40000,
            "wheels" : "",
            "color" : "blue",
            "number" : "random value"
        }    

    ],
    "Infiniti" :[
         {
            "price" : 150000,
            "wheels" : "",
            "color" : "black",
            "number" : "random value"

        },
        {
            "price" : 90000,
            "wheels" : "",
            "color" : "yellow",
            "number" : "random value"
        },    
    ],
    "Hyundai" :[
        {
            "price" : 5000,
            "wheels" : "",
            "color" : "green",
            "number" : "random value"

        },
        {
            "price" : 20000,
            "wheels" : "",
            "color" : "red",
            "number" : "random value"
        },    
    ],
    "Lexus" :[
         {
            "price" : 130000,
            "wheels" : "",
            "color" : "black",
            "number" : "random value"

        },
        {
            "price" : 80000,
            "wheels" : "",
            "color" : "blue",
            "number" : "random value"
        },    
    ]
} 
prepared_data_array = prepare_data(named_as_auto)

is_running = True

while is_running :
    choose_action = input("""
        1) Show all cars
        2) Show cars filtered by colors
        3) Show cars by price categories 
        4) Exit
    Answer : """.lower()    
    ) 

    if choose_action == "1" :
        show_named_as_auto(named_as_auto)

    elif choose_action == "2":
        filter_car_by_color(prepared_data_array)

    elif choose_action == "3":
        for key ,values in  filter_car_by_price(prepared_data_array).items():
            print(key) 
            for item_car in values: 
                print(item_car)     

    elif choose_action == "4" :    
        is_running = False  