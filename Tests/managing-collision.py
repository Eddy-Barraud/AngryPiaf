# Add a new collision type
COLLTYPE_GOAL = 3

# Define collision callback function, will be called when X touches Y 
def goal_reached(space, arbiter):
    print "you reached the goal!"
    return True

# Setup the collision callback function
h = space.add_collision_handler(COLLTYPE_BALL, COLLTYPE_GOAL)
h.begin = goal_reached

# Create and add the "goal" 
goal_body = pymunk.Body()
goal_body.position = 100,100
goal = pymunk.Circle(goal_body, 50)
goal.collision_type = COLLTYPE_GOAL
space.add(goal)