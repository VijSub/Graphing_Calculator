import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, Eq, solve


def plot_table_graph():
    # Prompt the user for the equation
    equation = input("Enter an equation in terms of x (e.g., 'x**2 + 2*x + 1'): ")

    try:
        # Create an array of x values within a specified range
        x_range = input("Enter the x range as 'start end' (e.g., '-10 10'): ").split()
        x_range = [float(x) for x in x_range]
        num_points = int(input("Enter the number of data points: "))

        x_values = np.linspace(x_range[0], x_range[1], num_points)

        # Evaluate the equation for each x value to get y values
        y_values = [eval(equation) for x in x_values]

        # Create a DataFrame to store the x and y values
        data = pd.DataFrame({'x': x_values, 'y': y_values})

        # Create a figure and axis for the plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # Add the title above the table
        plt.title(f'Table and Graph of {equation}')

        # Save the table of values as an image
        table_image = ax.table(cellText=data.values, colLabels=data.columns, loc='center')

        # Adjust the table appearance
        table_image.auto_set_font_size(False)
        table_image.set_fontsize(10)
        table_image.scale(1, 1.5)

        # Remove the x and y axis labels for the table
        ax.axis('off')

        # Plot the graph below the table
        ax = fig.add_subplot(2, 1, 2)
        ax.plot(data['x'], data['y'])
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid(True)

        # Show the plot (table and graph) with the title above the table
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def solve_system_of_equations():
    try:
        # Get user input for equations
        eq1_str = input("Enter the first equation (e.g., '2*x + 3*y = 10'): ")
        eq2_str = input("Enter the second equation (e.g., '3*x - 2*y = 5'): ")

        # Define symbolic variables
        x, y = sp.symbols('x y')

        # Split equations into left-hand side and right-hand side
        lhs1, rhs1 = eq1_str.split('=')
        lhs2, rhs2 = eq2_str.split('=')

        # Create equations
        eq1 = sp.Eq(sp.sympify(lhs1.strip()) - sp.sympify(rhs1.strip()), 0)
        eq2 = sp.Eq(sp.sympify(lhs2.strip()) - sp.sympify(rhs2.strip()), 0)

        # Solve the system of equations
        solution = sp.solve((eq1, eq2), (x, y))

        if solution:
            print("Solution:")
            for var, value in solution.items():
                print(f"{var}: {value}")
        else:
            print("No solution found.")

    except (sp.SympifyError, ValueError) as e:
        print(f"Error: {e}. Please enter valid equations.")


def plot_and_find_intersection():
    # Input equations as strings
    equation1 = input("Enter the first equation (e.g., '2*x + 1 = y'): ")
    equation2 = input("Enter the second equation (e.g., '-3*x + 5 = y'): ")

    # Define the variable symbols
    x, y = symbols('x y')

    # Parse the input equations using SymPy
    eq1 = Eq(eval(equation1.split('=')[0]), y)
    eq2 = Eq(eval(equation2.split('=')[0]), y)

    # Solve the system of equations for the intersection point
    intersection = solve((eq1, eq2), (x, y))

    if intersection:
        intersection_x = float(intersection[x])
        intersection_y = float(intersection[y])
        print(f"Intersection point: ({intersection_x:.2f}, {intersection_y:.2f})")

        # Create a range of x values for the plot
        x_values = np.linspace(intersection_x - 10, intersection_x + 10, 400)

        # Calculate y values for both equations
        y1 = eval(equation1.split('=')[0], {"x": x_values})
        y2 = eval(equation2.split('=')[0], {"x": x_values})

        # Plot the two equations
        plt.plot(x_values, y1, label=equation1)
        plt.plot(x_values, y2, label=equation2)

        # Plot the intersection point
        plt.scatter(intersection_x, intersection_y, color='red', label=f'Intersection ({intersection_x:.2f}, {intersection_y:.2f})')

        # Add labels and legend to the plot
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()

        # Show the plot
        plt.grid(True)
        plt.show()
    else:
        print("No intersection found.")

def plot_quadratic_roots_and_vertex():
    a = float(input("Enter coefficient 'a': "))
    b = float(input("Enter coefficient 'b': "))
    c = float(input("Enter coefficient 'c': "))
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is non-negative (real roots)
    if discriminant >= 0:
        # Calculate the two real roots
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)

        # Calculate the x-coordinate of the vertex
        vertex_x = -b / (2*a)

        # Calculate the y-coordinate of the vertex
        vertex_y = -discriminant / (4*a)

        # Create a range of x values for the plot
        x_values = np.linspace(min(root1, root2) - 1, max(root1, root2) + 1, 400)

        # Calculate the corresponding y values for the quadratic equation
        y_values = a * x_values**2 + b * x_values + c

        # Plot the quadratic equation
        plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')

        # Plot the roots
        plt.scatter([root1, root2], [0, 0], color='red', label=f'Roots: ({root1:.2f}, 0), ({root2:.2f}, 0)')

        # Plot the vertex
        plt.scatter(vertex_x, vertex_y, color='green', label=f'Vertex: ({vertex_x:.2f}, {vertex_y:.2f})')

        # Add labels and legend to the plot
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()

        # Show the plot
        plt.grid(True)
        plt.show()
    else:
        print("The quadratic equation has no real roots.")


def main_menu():
    while True:
        print("Menu:")
        print('1. Display the graph and a table of values for any "y=" equation input.')
        print("2. Solve a system of two equations without graphing")
        print("3. Graph two equations and plot the point of intersection")
        print("4. Given a, b and c in a quadratic equation, plot the roots and vertex")
        print("5. Exit")

        choice = input("Enter the number of your choice (1-5): ")

        if choice == "1":
            print('You chose display the graph and a table of values for any "y=" equation input.')
            plot_table_graph()
        elif choice == "2":
            print("You selected solve a system of two equations without graphing.")
            solve_system_of_equations()
        elif choice == "3":
            print("You selected graph two equations and plot the point of intersection.")
            plot_and_find_intersection()
        elif choice == "4":
            print("You selected, given a, b and c in a quadratic equation, plot the roots and vertex.")
            plot_quadratic_roots_and_vertex()
        elif choice == "5":
            print("Exiting the program.")
            break 
        else:
            print("Invalid choice. Please select a valid option (1-5).")


main_menu()