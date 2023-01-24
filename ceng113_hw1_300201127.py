"""

CHARACTER PALETTE
You can copy the necessary characters for drawing cards from here.

Horizontal lines:  │

Vertical lines:  ─

Corners of a card:  ┐  ┌  ┘  └

Intersections of two cards:

    if card1_height == card2_height:  ┬  ┴

    if card1_height < card2_height:  ┤

    if card1_height > card2_height:  ├

"""

print("This program will draw two cards next to each other.")
print("─" * 20)

print("Texts must not be empty.")
card1_text = input("Text of first card: ")
card2_text = input("Text of second card: ")
print("─" * 20)

##############################

# INSERT YOUR CODE HERE
# Assign proper values to card1_min_width and card2_min_width here.
# They are length of the corresponding text + 2.
# For example, if card1_text contains 5 characters, then card1_min_width must be 7.
card1_min_width = len(card1_text)+2
card2_min_width = len(card2_text)+2
# DO NOT EDIT THE CODE UNDER THIS LINE.
##############################

print("Width of first card must be at least " + str(card1_min_width) + ".")
card1_width = int(input("Width of first card: "))
print("Width of second card must be at least " + str(card2_min_width) + ".")
card2_width = int(input("Width of second card: "))
print("─" * 20)

print("Heights must be odd and at least 3.")
card1_height = int(input("Height of first card: "))
card2_height = int(input("Height of second card: "))
print("─" * 20)


##############################
# INSERT YOUR CODE HERE

# Assign the proper value to is_invalid.
# Check if there is at least one problem in the inputs.
# I added two conditions, add more to the line below.

is_invalid =  len(card1_text) == 0 or len(card2_text) == 0 or (card1_height % 2) == 0 or (card2_height % 2) == 0 or card1_width < card1_min_width or card2_min_width > card2_width 
# DO NOT EDIT THE CODE UNDER THIS LINE.
##############################

if is_invalid:
    print("ERROR: Invalid inputs.")

else:

    if card1_height == card2_height:

        ##############################
        import math
        upside_line = "┌" + (card1_width-2) * "─" + "┬" + (card2_width-2) * "─" + "┐"
        line_of_spaces_times = int((card1_height - 3)/2)
        line_of_spaces = "│" + (card1_width-2) * " " + "│" + (card2_width-2) * " " + "│" + "\n"
        text_line_spaces_card1_left = (card1_width - len(card1_text) - 2)//2
        text_line_spaces_card1_right = math.ceil((card1_width - len(card1_text) - 2)/2)
        text_line_spaces_card2_left = (card2_width - len(card2_text) - 2)//2
        text_line_spaces_card2_right = math.ceil((card2_width - len(card2_text) - 2)/2)
        text_line1 = "│" + text_line_spaces_card1_left * " " + card1_text + text_line_spaces_card1_right * " " + "│"
        text_line2 =  text_line_spaces_card2_left * " " + card2_text + text_line_spaces_card2_right * " " + "│"
        bottom_line ="└" + (card1_width-2) * "─" + "┴" + (card2_width-2) * "─" + "┘"

        print(upside_line)
        print((line_of_spaces * line_of_spaces_times)+(text_line1)+(text_line2))
        print((line_of_spaces * line_of_spaces_times)+(bottom_line))
        
    
        pass


    elif card1_height > card2_height:

        ##############################
        # INSERT YOUR CODE HERE
        
        
        
        #-------------------------------------
        line_of_spaces_times = int((card1_height - 3)/2)
        line_of_spaces = "│" + (card1_width-2) * " " + "│" + (card2_width-2) * " " + "│" + "\n"
        #--------------------------------------------
        import math
        upside_line_2 = "┌" + (card1_width-2) * "─" + "┐"
        bottom_line_2 ="└" + (card1_width-2) * "─" + "┘"
        line_of_spaces_2 = "│" + (card1_width-2) * " " + "│" + "\n"
        line_of_spaces_times_2 = int((card1_height - 2 - card2_height)/2)
        card2_shape_line_upside = "│" + (card1_width-2) * " " + "├" + "─" * (card2_width-2) + "┐"
        space_lines = "│" + (card1_width-2) * " " + "│" + " " * (card2_width-2) + "│" + "\n"
        space_lines_times = int((card2_height - 3)/2)
         
        #text line didn't change----------------------------------------------------------------------------------
        text_line_spaces_card1_left = (card1_width - len(card1_text) - 2)//2
        text_line_spaces_card1_right = math.ceil((card1_width - len(card1_text) - 2)/2)
        text_line_spaces_card2_left = (card2_width - len(card2_text) - 2)//2
        text_line_spaces_card2_right = math.ceil((card2_width - len(card2_text) - 2)/2)
        text_line1 = "│" + text_line_spaces_card1_left * " " + card1_text + text_line_spaces_card1_right * " " + "│"
        text_line2 =  text_line_spaces_card2_left * " " + card2_text + text_line_spaces_card2_right * " " + "│"
         #---------------------------------------------------------------------------------------------------------
        
        card2_shape_line_downside = "│" + (card1_width-2) * " " + "├" + "─" * (card2_width-2) + "┘"


        print(upside_line_2)
        print((line_of_spaces_2 * line_of_spaces_times_2) +(card2_shape_line_upside))
        print((space_lines * space_lines_times) + (text_line1) + (text_line2))
        print((space_lines * space_lines_times) + (card2_shape_line_downside))
        print((line_of_spaces_2 * line_of_spaces_times_2)+ (bottom_line_2))
        
        
        
        
        # Case 2
        # You can add as many new lines as you need.
        pass



        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################


    else:

        ##############################
        # INSERT YOUR CODE HERE
        import math
        
        case3_upside_line = " " * (card1_width - 1) + "┌" + "─" * (card2_width - 2) + "┐"
        line_of_spaces_3 =  " " * (card1_width - 1) + "│" + " " * (card2_width - 2) + "│" + "\n"
        line_of_spaces_times_3 = int((card2_height - card1_height - 2)/2)
        card1_Shape_line_upside = "┌" + "─" * (card1_width - 2) + "┤" + " " * (card2_width - 2) + "│" 
        space_lines_3 = "│" + " " * (card1_width - 2) + "│" + " " * (card2_width - 2) + "│" + "\n"
        space_lines_3_times = int((card1_height - 3)/2)
        card1_Shape_line_downside = "└" + "─" * (card1_width - 2) + "┤" + " " * (card2_width - 2) + "│" 
        case3_downside_line =  " " * (card1_width - 1) + "└" + "─" * (card2_width - 2) + "┘"
         
         
         #text line didn't change----------------------------------------------------------------------------------
        text_line_spaces_card1_left = (card1_width - len(card1_text) - 2)//2
        text_line_spaces_card1_right = math.ceil((card1_width - len(card1_text) - 2)/2)
        text_line_spaces_card2_left = (card2_width - len(card2_text) - 2)//2
        text_line_spaces_card2_right = math.ceil((card2_width - len(card2_text) - 2)/2)
        text_line1 = "│" + text_line_spaces_card1_left * " " + card1_text + text_line_spaces_card1_right * " " + "│"
        text_line2 =  text_line_spaces_card2_left * " " + card2_text + text_line_spaces_card2_right * " " + "│"
         #---------------------------------------------------------------------------------------------------------

        
        print(case3_upside_line)
        print((line_of_spaces_3 * line_of_spaces_times_3) + (card1_Shape_line_upside))
        print((space_lines_3 * space_lines_3_times) + (text_line1) + (text_line2))
        print((space_lines_3 * space_lines_3_times) + (card1_Shape_line_downside))
        print((line_of_spaces_3 * line_of_spaces_times_3) + case3_downside_line)
        
        
        
        # Case 3
        # You can add as many new lines as you need.
        pass



        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################
