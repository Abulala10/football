import matplotlib.pyplot as plt
import datetime
import pandas as pd
from matplotlib.dates import date2num
greetings = " __ { Football Program } __ "


class Football:

    def __init__(self, welcome):
        try:
            global df, copy_df
            self.welcome = welcome
            print(self.welcome)  # object of class Football
            self.directory = 'D:\dataSets\\netflixFigures\\'
        except Exception as e:
            print("Error in Constructor :", e)

    def readFile(self, football_df):
        try:
            printFile = input("Do you want to read File : (yes/no) ")
            if printFile.__eq__("yes"):
                try:
                    if football_df is not None:  # if file is empty error is printed
                        print(football_df)
                except FileNotFoundError or FileExistsError as fnfe:
                    print("Error in Func readFile(parameters) : 1", fnfe)
                    exit()
            elif printFile.__eq__("no"):
                try:
                    if football_df is not None:
                        pass
                except FileNotFoundError or FileExistsError as file:
                    print("Error in Func readFile(parameters) : 2", file)
                    exit()
        except Exception as e:
            print("Error in Func readFile(parameters) : 3", e)
            exit()

    def FCB(self, data_frame, fcbarcelona, player_age):
        global value
        try:
            colors = ['red', 'indigo', 'purple']
            getTeam = fcbarcelona == "FC Barcelona"
            age = player_age >= 30
            player_30 = data_frame[["Name", "Club", "Age", "Position", "Overall"]].where(getTeam & age).dropna()
            # if getTeam and age is true then it will proceed
            fig, ax = plt.subplots()
            ax.barh(player_30["Name"], player_30["Overall"], color=colors)  # simple horizontal plotting
            ax.set_ylabel("Player Names")
            ax.set_xlabel("Overall Rating of Player")
            ax.minorticks_on()
            ax.set_title("Fcb players overall ratings with age greater than [29]")
            for index, value in enumerate(player_30["Overall"]): # displays values near or on the bars
                ax.text(value, index, str(value))  # plt.text(parameters) used to display values on the bars
            if save.casefold().__eq__("yes"):
                name = input("Enter name for chart that shows overall rating of fcb players : ")
                plt.savefig(self.directory + name + '.png')
                print("File Saved at location :" + self.directory + name + ".png")
        except Exception as e:
            print('Error in Func FCB(parameters) : 1', e)
            exit()

        # Wage of players with age greater than [29]

        try:
            fig, ax1 = plt.subplots()
            player_wage = data_frame[["Name", "Club", "Age", "Position", "Wage"]].where(getTeam & age).dropna()
            ax1.set_title("Wage of players with age greater than [29]")
            ax1.set_xlabel("Player Names")
            ax1.set_ylabel("Wage of Players")
            ax1.bar(player_wage["Name"], player_wage["Wage"], color=colors)
            if save.casefold().__eq__("yes"):
                name = input("Enter name : For chart that displays wage of players > ")
                plt.savefig(self.directory + name + '.png')
                print("File Saved at location :" + self.directory + name + ".png")
        except Exception as e:
            print('Error in Func readFile(parameters) : 2', e)
            exit()

        try:
            plt.show()
        except Exception as e:
            print("Error in Func readFile(parameters) : 4", e)
            exit()

    def attributes(self,  potential, data_frame):
        try:
            breadth = 0.6
            labels = ['LongPassing', "BallControl", "Finishing", "Dribbling", "Jersey Number"]
            overall_88 = data_frame["Overall"] >= 88
            fcb = data_frame["Club"] == "FC Barcelona"
            fcb_best_players = data_frame[["Dribbling", "Name", "Finishing", "BallControl", "Jersey Number",
                                           "LongPassing"]].where(fcb & overall_88).dropna()
            fig, ax = plt.subplots()
            #  ax.bar(all 3 plots) These plots make 3 plots on a single charts.
            #  Each bar consists of fcb_best_players[[international reputation, age, overall]].
            ax.plot(fcb_best_players["Name"], fcb_best_players["LongPassing"]+breadth, color='red')
            ax.plot(fcb_best_players["Name"], fcb_best_players["BallControl"], color='blue')
            ax.plot(fcb_best_players["Name"], fcb_best_players["Finishing"]-breadth, color='green')
            ax.plot(fcb_best_players["Name"], fcb_best_players["Dribbling"], color='purple')
            ax.plot(fcb_best_players["Name"], fcb_best_players["Jersey Number"]+breadth, color='black')
            # fcb_best_players["Name"] on the x axis and other's on y axis
            ax.minorticks_on() # minor_ticks as in the small hyphens between numbers or names on the x and y axis
            ax.set_ylabel("[Attributes]\n\n[Long Passing] [Ball Control] [Finishing] [Dribbling] [Jersey Number]")
            ax.set_xlabel("Player names of FCB")
            ax.legend(labels, loc='upper right')  # loc [inbuilt function used to place the legend]
            if save.casefold().__eq__("yes"):
                name = input("Enter chart name that displays the attributes of fcb players > ")
                plt.savefig(self.directory + name + ".png")
                print("File Saved at location :" + self.directory + name + ".png")
            plt.show()
            #  Just as the above plots we can show the age height overall and international reputation of the
            #  top 5 players of fcb.
        except Exception as e:
            print(e)


cmd = Football(greetings)
if __name__ == "__main__":

    global df, copy_df, value, save
    try:
        df = pd.read_csv("D:\dataSets\kaggle\\FootballDataset\data.csv")
        copy_df = df.copy()
        del copy_df["Unnamed: 0"]  # deletes unnamed column in the file
        cmd.readFile(copy_df)
        save = input("Do you want to save the charts ? (yes/no) ")
        cmd.FCB(copy_df, copy_df["Club"], copy_df["Age"])
        cmd.attributes(copy_df["Potential"], copy_df)
        end = datetime.datetime.strftime(datetime.datetime.now(), "%H-%M-%S")

    except Exception as e:
        print("Main :", e)
        exit()