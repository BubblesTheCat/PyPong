
_**PyPong**_

#  Welcome!

Welcome to the bowels of the simple standalone game that is
PyPong. I made it within two days, and it's not fancy. It is just
bouncing a ball back and forth until you mess up and the game kicks you out.
But that's not the point, the point is to show that I can make something real 
using design processes, my superficial knowledge of python and a little bit of research.
The only python library that it uses is pygame.

# The Making Of: Please Don't Read All Of This, I Value Your Time
For the most part, creating this was simple and the majority of issues that I faced were simple mistakes like writing X instead of Y,
or forgetting to make sure that a variable stayed a positive variable. 

The only point where I felt really stuck was when I was designing the enemy paddle brain; I started by trying to apply 
trigonometry and must have spent an hour trying to get that to work, and eventually I managed to.  
Although, it had this ugly shaking motion because its rudimentary "if y > target: y -=, else y+=" motion system kept 
overcorrecting itself. It didn't help that all the soloutions that I could see seemed like bodges, and not very good ones at that e.g rounding both
sides and using an == statement to check if the paddle was on roughly the same level as the ball or using an inequality 
to find out whether the paddle was in roughly the right place. I promptly spent about half an hour messing around with
the equations I had built. Long after it had become clear that my tinkering would not be sufficient, I implemented a
"speed" variable to try and prevent the paddle overcorrecting so agressively by preventing it ever needing to correct at all.
This seemed like a good idea at the time, but all it really meant was more fiddling with maths. After another hour
I finally saw that pythagoras did not have my answer, simplifying the problem into a kind of ratio to work out that
the iterations of the game loop between the ball hitting the paddle was equal to the speed of the multiplied by its distance(,
and no, it doesn't look good that it took me two and a half hours to work out that a basic physics engine uses basic 
physics but this was two and a half of my hours, so I'm leaving it in). I then built the equation for where the ball would land
off of the previous one, incorporating the T = S * D  equation again, but this time using the common time variable (IterationsBetweenBallAndPaddle)
and the ball's unique Y motion variable offset by where the ball is now add 60 pixels so that the paddle got the ball in the
middle instead of the edge. Then, I worked out the distance for the paddle to travel and spent 15 minutes chasing my tale trying
to understand why the paddle went towards the ball and then ran away from it when it got close enough to make me think it
 was working (something that was hard not to take personally) All I had to do to mitigate that was to make sure it 
stayed positive with yet another if statement. After this, I made the paddle speed equation from the common distance it
shared with the Y momentum of the ball and the common time it shared with the X and Y momentums of the ball. All that was
left was to use the now overstretched if else structure to move the paddle. As a bonus I didn't have to fix the jittering
issue because the speed variable moved the paddle perfectly into position. The last problem I faced was the fact that 
the Paddle now behaved exactly as if it was just attatched to the BallY variable, in response to this, I put the whole
script into a statement that checks for if the Ball is within 500 pixels of it so the paddle is now effectively shortsighted.
If you want, you can go into line 76 and swap different values in place of the 500 and watch as the paddle completely mirrors the ball
or just sits there until the very last minute. Although beware, if the paddle gets too short sighted it tends to grab the ball
in protest and if the ball gets past the paddle it will cause a zero division error that crashes the game because the ball
X pos becomes equal to 1400 which when subtracted from 1400 makes zero which is then divided to get the iterations, but
instead it just throws out an error.


sound effects:
https://pixabay.com/sound-effects/search/record%20scratch/

game loop by Gunnar Martinez: 
(https://blog.devgenius.io/a-step-by-step-guide-to-creating-a-python-game-with-pygame-a-step-by-step-guide-to-creating-a-4c89f81fe7e0)
