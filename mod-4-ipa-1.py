'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_graph = {
                        "@bongolpoc":{"first_name":"Joselito",
                                      "last_name":"Olpoc",
                                      "following":[
                                      ]
                        },
                        "@joaquin":  {"first_name":"Joaquin",
                                      "last_name":"Gonzales",
                                      "following":[
                                          "@chums","@jobenilagan"
                                      ]
                        },
                        "@chums" : {"first_name":"Matthew",
                                    "last_name":"Uy",
                                    "following":[
                                        "@bongolpoc","@miketan","@rudyang","@joeilagan"
                                    ]
                        },
                        "@jobenilagan":{"first_name":"Joben",
                                       "last_name":"Ilagan",
                                       "following":[
                                        "@eeebeee","@joeilagan","@chums","@joaquin"
                                       ]
                        },
                        "@joeilagan":{"first_name":"Joe",
                                      "last_name":"Ilagan",
                                      "following":[
                                        "@eeebeee","@jobenilagan","@chums"
                                      ]
                        },
                        "@eeebeee":  {"first_name":"Elizabeth",
                                      "last_name":"Ilagan",
                                      "following":[
                                        "@jobenilagan","@joeilagan"
                                      ]
                        },
                    }
  
    from_member_following = social_graph[from_member]["following"]
    to_member_following = social_graph[to_member]["following"]
        
    for v in from_member_following:
        if v == to_member:
            for w in to_member_following:
                if w == from_member:
                        return "friends"
                else:
                    continue
            return "follower"
        else:
            break

    for w in to_member_following:
        if w == from_member:
            return "followed by"
        else:
            return "no relationship"
    
    


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    board1 = [
            ['X','X','O'],
            ['O','X','O'],
            ['O','','X'],
            ]

            board2 = [
            ['X','X','O'],
            ['O','X','O'],
            ['','O','X'],
            ]

            board3 = [
            ['O','X','O'],
            ['','O','X'],
            ['X','X','O'],
            ]

            board4 = [
            ['X','X','X'],
            ['O','X','O'],
            ['O','','O'],
            ]

            board5 = [
            ['X','X','O'],
            ['O','X','O'],
            ['X','','O'],
            ]

            board6 = [
            ['X','X','O'],
            ['O','X','O'],
            ['X','',''],
            ]

            board7 = [
            ['X','X','O',''],
            ['O','X','O','O'],
            ['X','','','O'],
            ['O','X','','']
            ]
    def tic_tac_toe(board):
        horizontal_check = [x for x in board]
        vertical_check = [x for x in zip(*board)]
        updown_diagonal_check = [board[i][i] for i,v in enumerate(board)]
        downup_diagonal_check = [board[len(board)-1-i][i] for i,v in enumerate(board)]
    
        for j,m in enumerate(horizontal_check):
            if all([s=="X" for s in m]):
                return "X"
            elif all([s=="O" for s in m]):
                return "O"
            else:
                break

        for l,n in enumerate(vertical_check):
            if all([s=="X" for s in n]):
                return "X"
            elif all([s=="O" for s in n]):
                return "O"
            else:
                break
                      
        if all([s=="X" for s in updown_diagonal_check]):
              return "X"
        elif all([s=="O" for s in updown_diagonal_check]):
              return "O"
        elif all([s=="X" for s in downup_diagonal_check]):
              return "X"
        elif all([s=="O" for s in downup_diagonal_check]):
              return "O"
        else:
              return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
    }

    legs = {
        ('a1', 'a2'): {
            'travel_time_mins': 10
        },
        ('a2', 'b1'): {
            'travel_time_mins': 10230
        },
        ('b1', 'a1'): {
            'travel_time_mins': 1
        }
    }
    
    destination_routes = route_map.keys()
    a = [x for x in destination_routes]
    b = [y for y,z in a]
    c = [z for y,z in a]
    total_mins = 0
    
    for d in b:
        e = b.index(d)
        if d == first_stop:
            while(True):
                if c[e] != second_stop:
                    travel_time = int(route_map[b[e],c[e]]['travel_time_mins'])
                    total_mins += travel_time
                    if e == len(b) - 1:
                        e = 0
                    elif e < len(b):
                        e += 1
                    continue
                elif c[e] == second_stop:
                    last_stop_mins = int(route_map[b[e],c[e]]['travel_time_mins'])
                    return total_mins + last_stop_mins