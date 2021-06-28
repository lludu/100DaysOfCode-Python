# from turtle import Turtle, Screen

# #make a timmy object from the turtle class blueprint
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkOrchid")
# timmy.speed(1)
# timmy.forward(100)


# # bobby = Turtle()
# # bobby.shape("turtle")
# # bobby.color("blue")

# #screen object from turtle module
# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()


from prettytable import PrettyTable

#create a new object called table from the class Pretty Table
table = PrettyTable()

#add columns to table
table.add_column("Pokemon Name",["Pikachu", "Bulbasaur", "Charmander", "Squirtle"])
table.add_column("Type",["Electric", "Grass", "Fire", "Water"])
#change attribute of table object
table.align = "l"
print(table)
