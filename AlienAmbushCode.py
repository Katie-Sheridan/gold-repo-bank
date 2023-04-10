#create a code that runs arcade game

#list the alien colors

character = ['green', 'yellow', 'red', 'blue', 'purple']
aliens_colors = ['green', 'yellow', 'red']
score = 0 

# define the point values
if 'green' in aliens_colors:
    print('Player1 earned 5 points')
    print (score + 5 )
elif 'yellow' in aliens_colors:
    print('Player1 earned 10 points')
    print(score + 10)
elif 'red' in aliens_colors:
    print('Player1 earnd 15 points')
    print(score + 15)
elif 'blue' in character:
    print('Warning! You hit a friendly spaceship!') 
    print (score)

final_score = 15 

print(final_score)
if final_score > 10:
    print('Congratulations! New High Score!')
elif final_score == 0:
    print ('Game over')