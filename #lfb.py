#lfb

# firstly, we take the inputs from user 


text = input("text: ")
width = int(input("width: "))
height = int(input("height:"))
border_charts = input("border charts: ")

# we will print width times border_chart for first and last line

up_and_down_lines = border_charts * width

# there is a line for printing user's text
# we should write manually a border_charts in the first and last characters
# then we need spaces, width - 2(we add 2 character manually left and right corners so we should use -2)
# but also we write a text message so we will use -(the lenght of text) with len() function
# half of spaces should stay in left and the other half in the right side

how_many_spaces_in_text_line_r_and_l = int((width - 2 - len(text))/2)
text_line = border_charts + " " * how_many_spaces_in_text_line_r_and_l + text + " " * how_many_spaces_in_text_line_r_and_l + border_charts

# for the lines between text and first line(or last line)
# we have to write a border_charts, 
# width-2(we used -2 because of writing the first and last character manually) times spaces 
# and a border_charts again 
# but we need the half of spaces upside of text_line and the other half should be downside of textline

half_of_other_borders = border_charts + " " * (width-2) + border_charts + "\n"
how_many_times_new_line = int(((height - 3)/2))

# Because of using \n there was 2 more new lines which are empty so it's like

"""
*********
*       *

*   t   *

*       *
*********
"""

# you can see the 3rd and 5th lines are completely empty
# for fixing this i will delete 1 line which has \n and i will add a line manually
# for example:
#   if we want 10 lines 
#   ("*" + " " * 30 + "*" + "\n") * 10    ->  this code create 10 lines and a new empty line because of "\n"
# so i will change 10 to 9 (10 - 1). and i will add exactly the same expression to end of this line
# it will seems like that
# ("*" + " " * 30 + "*" + "\n") * (9) + "*" + " " * 30 + "*"
# i will define a new variable which is same with the other but this one does not have \n 

half_of_other_borders_without_escape = border_charts + " " * (width-2) + border_charts 

print(up_and_down_lines)
print((half_of_other_borders) * (how_many_times_new_line-1) + half_of_other_borders_without_escape)
print(text_line)
print((half_of_other_borders) * (how_many_times_new_line-1) + half_of_other_borders_without_escape)
print(up_and_down_lines)

#yay it works on my machine :D