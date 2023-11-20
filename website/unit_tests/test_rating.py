import sys
sys.path.append('../functions')
import rating

def test_calulate_rating():

    token = 'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2'

    ratings = [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                 {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                 {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                 {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                 {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                 {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                 {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                 {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                 {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                 {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':True} ] 

    assert rating.calculate_rating( token, ratings ) == 50

def test_count_thumb_up():

    ratings = [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                 {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                 {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                 {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                 {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':True},
                 {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                 {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                 {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                 {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                 {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':True} ] 

    assert rating.count_thumb_up( ratings ) == 6

def test_toggle_thumb_up():

    token = 'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2'

    ratings = [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                 {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                 {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                 {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                 {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                 {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                 {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                 {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                 {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                 {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':False} ]
    
    rating.toggle_thumb_up( token, ratings ) # toggle on
    assert ratings == [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                         {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                         {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                         {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                         {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                         {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                         {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                         {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                         {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                         {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':True} ]
    
    rating.toggle_thumb_up( token, ratings ) # toggle off
    assert ratings == [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                         {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                         {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                         {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                         {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                         {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                         {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                         {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                         {'buMzV7i8QoijEWcVHDfkFjY71pYn':True} ]
    
    rating.toggle_thumb_up( token, ratings ) # toggle on
    assert ratings == [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                         {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                         {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                         {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                         {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                         {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                         {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                         {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                         {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                         {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':True} ]
    
def test_toggle_thumb_down():

    token = 'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2'

    ratings = [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                 {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                 {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                 {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                 {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                 {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                 {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                 {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                 {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                 {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':True} ]
    
    rating.toggle_thumb_down( token, ratings ) # toggle on
    assert ratings == [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                         {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                         {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                         {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                         {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                         {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                         {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                         {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                         {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                         {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':False} ]
    
    rating.toggle_thumb_down( token, ratings ) # toggle off
    assert ratings == [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                         {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                         {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                         {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                         {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                         {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                         {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                         {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                         {'buMzV7i8QoijEWcVHDfkFjY71pYn':True} ]
    
    rating.toggle_thumb_down( token, ratings ) # toggle on
    assert ratings == [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                         {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                         {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                         {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                         {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                         {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                         {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                         {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                         {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                         {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':False} ]

def test_check_thumb():

    token1 = 'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2'
    token2 = 'iFCvpOVxbCjGp8ofqUCpNtjLTtj4'
    token3 = 'RQFk9dPQ7bfuQJtfkvgg0bCp7Va3'

    ratings = [  {'mghTqIwPW6wJKPh8MgfrP5QofM8y':False},
                 {'soO5Twv64ZnCpnn09BGJ0IegX0uu':False},
                 {'UJwCYfnQ22axSIjpFI2VuxP1iOrX':False},
                 {'0ngxJcWNTl4hn54AtKVxpxgLhXQ8':False},
                 {'iFCvpOVxbCjGp8ofqUCpNtjLTtj4':False},
                 {'LbArobu4r6KPdVzLQTADF3XgW4qX':True},
                 {'fMazzuxFUgmawsPsLsUVkBClX9xw':True},
                 {'OizZUFsjkpdR5IuPmLVpFRM4As7F':True},
                 {'buMzV7i8QoijEWcVHDfkFjY71pYn':True},
                 {'RQFk9dPQ7bfuQJtfkvgg0bCp7Va2':True} ]
    
    assert rating.check_thumb( token1, ratings ) == True
    assert rating.check_thumb( token2, ratings ) == False
    assert rating.check_thumb( token3, ratings ) == False