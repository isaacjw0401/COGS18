"""A collection of function for doing my project."""

import pandas as pd

def add_house(df):
    """Adds to DataFrame, the details of a property.
    
    Parameters
    ----------
    df: DataFrame that reads csv file named 'property' through pandas. Allows the linkage for actions below to successfully carry out.
    
    Returns
    -------
    No Return (Updates the dataframe with details of the inputted property details; not necessarily a typical return function).
    """
    
    #assigns to each object, the input to the question asked (in strings) to gather information and add a property to 'property' DataFrame.
    #The .loc[len(df.index)] allows data value retrieval from index of the DataFrame 'property' (df), and sequential use of .to_csv converts     the given series object (df.loc[len(df.index)]into a comma separated format, hence ultimately, adding the new input to the DataFrame.
    name = input("write the name of owner:\n")
    year = int(input("write the built year:\n"))
    size = int(input("write the size(sqft):\n"))
    zip = input("write the zip code:\n")
    price = int(input("write the price you want($):\n"))
    df.loc[len(df.index)] = [name, year, size, price, zip]
    df.to_csv('property.csv', index = False)

    
    

def drop_house(df):
    """Deletes information (a row) in DataFrame, the details of a property.
    
    Parameters
    ----------
    df: DataFrame that reads csv file named 'property' through pandas. Allows the linkage for actions below to successfully carry out.
    
    Returns
    -------
    No Return (Updates the dataframe by deleting a property of details of the inputted property details; not necessarily a typical return function).
    """
    
    
    #the locating concept of a data within DataFrame is same as add_house, then within the provided lists, we specify a certain list to delete. This '.drop' drops that and updates the list.
    print(df.to_string())
    inp = int(input("write the number to drop:\n"))
    df = df.drop(index = inp)
    df.to_csv('property.csv', index = False)

    
    

def find_house(df):
    """Filters from DataFrame 'property' with inputted conditions to return filtered search results.
    
    Parameters
    ----------
    df: DataFrame that reads csv file named 'property' through pandas. Allows the linkage for actions below to successfully carry out.
    
    Returns
    -------
    Returns searched dataframe (df_copy1, df_copy2_2, df_copy3_2) depending on the user's input and accordingly processed steps. 
    """
    
    #Conditional to gather user's input information set as b, which executes when 0 and exits when 1. 0 yields several options to filter the DataFrame by, which then branches down to choice1 (per 'while' loop), varying in code contents depending on input 1,2,3, or 4.
    arb_cond1 = 0
    while arb_cond1 == 0:
        choice1 = input("Select options that you want to find based on\n"
                        "1. Built year \n"
                        "2. Size \n"
                        "3. Price \n"
                        "4. exit \n")
        
        # If 1 was chosen, it asks for a certain input in int; year format, which then sorts the copied version of the DataFrame (since it has to be modified) in ascending order for better user experience, filters/converts the data so that only the properties with the year category being same or over the input year shows up.
        
        if choice1 == "1":
            year = int(input("Write the least built year of the properties you want\n"))
            df_copy1 = df.sort_values("BuiltYear", ascending = True)
            df_copy1 = df_copy1.loc[df_copy1["BuiltYear"] >= year]
            print(df_copy1)
            return df_copy1

            
        # If 2 was chosen, it works the same way as 1, but for the category of property size, and in range of minimum and maximum (equal to or higher than minimum size input, and equal to or lower than maximum size input). 
        elif choice1 == "2":
            msize = int(input("Write the minimum size of the properties you want\n"))
            maxsize = int(input("Write the maximum size of the properties you want\n"))
            df_copy2 = df.sort_values("Size", ascending = True)
            df_copy2_1 = df_copy2.loc[df_copy2["Size"] >= msize]
            df_copy2_2 = df_copy2_1.loc[df_copy2_1["Size"] <= maxsize]
            print(df_copy2_2)
            return df_copy2_2
            
        # If 3 was chosen, it works the same way as 2, but for the category of price. The minimum and maximum range filtering is the same.
        elif choice1 == "3":
            mprice = int(input("Write the minimum price of the properties you want\n"))
            maxprice = int(input("Write the maximum price of the properties you want\n"))
            df_copy3 = df.sort_values("Price", ascending = True)
            df_copy3_1 = df_copy3.loc[df_copy3["Price"] >= mprice]
            df_copy3_2 = df_copy3_1.loc[df_copy3_1["Price"] <= maxprice]
            print(df_copy3_2)
            return df_copy3_2

        # If 4 was chosen, this leads to b equating to 1, which ends the while loop to return to the menu "page." In case other numbers were chosen, any other number besides 1,2,3, or 4 results in asking for the number selection again, allowing a correct reselection.
        elif choice1 == "4":
            arb_cond1 = 1
        else:
            print("select number from 1, 2, 3, 4")
            return "select number from 1,2,3,4"

# While loop responsible for initial root menu selection branching


def initialize(df):
    """Initializes the system, giving user options to choose from to proceed to either manipulate DataFrame (add/drop) or search (find).
    
    Parameters
    ----------
    df: DataFrame that reads csv file named 'property' through pandas. Allows the linkage for actions below to successfully carry out.
    
    Returns
    -------
    No Return (Shows user the options to carry out an action, which initiates other functions listed above (add_house, drop_house, find_house)).
    """
    
    #Sets a conditional for while loop and its exit later on.
    arb_cond2 = 0
    while arb_cond2 == 0:
        
        #Choices are given to the user to choose from, which varies by the operation the user wishes to carry out; the functions that allow such operation is then run. If 4, or 'exit' is chosen, it breaks the loop while any other nonviable numbers lead to reselection page.
        choice = input("Select from 1, 2, 3, 4 \n"
        "1. add house \n"
        "2. find house \n"
        "3. drop house \n"
        "4. exit \n")
        
        if choice == "1":
            add_house(df)
        elif choice == "2":
            find_house(df)
        elif choice == "3":
            drop_house(df)
        elif choice == "4":
            arb_cond2 = 1
        else:
            print("select number from 1, 2, 3, 4")