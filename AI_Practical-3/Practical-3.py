#T101 RAJDEEP M PARAB
# AIM: Implement A* Search Algorithm for Mumbai Suburban Map Problem.
dict_hn = {
    'Churchgate': 18,
    'Marine Lines': 17,
    'Charni Road': 16,
    'Grant Road': 15,
    'Mumbai Central': 14,
    'Mahalaxmi': 13,
    'Lower Parel': 11,
    'Prabhadevi': 10,
    'Dadar': 9,
    'Matunga Road': 8,
    'Mahim': 7,
    'Bandra': 6,
    'Khar Road': 5,
    'Santacruz': 4,
    'Vile Parle': 2,
    'Andheri': 0
}
dict_gn = dict(
    Churchgate=dict(
        **{'Marine Lines': 1.5}
    ),
    **{
        'Marine Lines': {
            'Churchgate': 1.5,
            'Charni Road': 1.2
        }
    },
    **{
        'Charni Road': {
            'Marine Lines': 1.2,
            'Grant Road': 1.4
        }
    },
    **{
        'Grant Road': {
            'Charni Road': 1.4,
            'Mumbai Central': 1.3
        }
    },
    **{
        'Mumbai Central': {
            'Grant Road': 1.3,
            'Mahalaxmi': 1.6
        }
    },
    **{
        'Mahalaxmi': {
            'Mumbai Central': 1.6,
            'Lower Parel': 1.5
        }
    },
    **{
        'Lower Parel': {
            'Mahalaxmi': 1.5,
            'Prabhadevi': 1.3
        }
    },
    **{
        'Prabhadevi': {
            'Lower Parel': 1.3,
            'Dadar': 1.2
        }
    },
    **{
        'Dadar': {
            'Prabhadevi': 1.2,
            'Matunga Road': 1.4
        }
    },
    **{
        'Matunga Road': {
            'Dadar': 1.4,
            'Mahim': 1.3
        }
    },
    **{
        'Mahim': {
            'Matunga Road': 1.3,
            'Bandra': 2.0
        }
    },
    **{
        'Bandra': {
            'Mahim': 2.0,
            'Khar Road': 1.4
        }
    },
    **{
        'Khar Road': {
            'Bandra': 1.4,
            'Santacruz': 1.3
        }
    },
    **{
        'Santacruz': {
            'Khar Road': 1.3,
            'Vile Parle': 1.8
        }
    },
    **{
        'Vile Parle': {
            'Santacruz': 1.8,
            'Andheri': 2.0
        }
    },
    **{
        'Andheri': {
            'Vile Parle': 2.0
        }
    }
)
import queue as Q
start = 'Churchgate'
goal = 'Andheri'
result = ''
def get_fn(citystr):
    cities = citystr.split(" , ")
    hn = gn = 0
    for ctr in range(0, len(cities) - 1):
        gn = gn + dict_gn[cities[ctr]][cities[ctr + 1]]
    hn = dict_hn[cities[len(cities) - 1]]
    return (hn + gn)
def expand(cityq):
    global result
    tot, citystr, thiscity = cityq.get()
    if thiscity == goal:
        result = citystr + " : : " + str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put(
            (
                get_fn(citystr + " , " + cty),
                citystr + " , " + cty,
                cty
            )
        )
    expand(cityq)
def main():
    cityq = Q.PriorityQueue()
    thiscity = start
    cityq.put(
        (
            get_fn(start),
            start,
            thiscity
        )
    )
    expand(cityq)
    print("The A* path with the total is: ")
    print(result)


main()
