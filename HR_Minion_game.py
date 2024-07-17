"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.
"""

def minion_game(string):
    # #string = string.upper()
    # # your code goes here
    # #dic = {} #dictionary to store the strings
    # size = len(string)
    # S_res, K_res = 0, 0
    # Stuart, Kevin = {}, {} # initialize scores
    # for i in range(0,size):
    #     for j in range(i+1,size+1):
    #         cur_str = string[i:j]
    #         #print(cur_str)
    #         if cur_str[0] in ['A','E','I','O','U']:
    #             K_res += 1
    #             # Kevin[cur_str] = Kevin.get(cur_str, 0) + 1
    #         else:
    #             S_res += 1
    #             # Stuart[cur_str] = Stuart.get(cur_str, 0) + 1
    # #print(Kevin)
    # #print(Stuart)

    # # for value in Kevin.values():
    # #     K_res += value
    # # for value in Stuart.values():
    # #     S_res += value
    # if S_res > K_res:
    #     print(f'Stuart {S_res}')
    # elif K_res > S_res:
    #     print(f'Kevin {K_res}')
    # else:
    #     print("Draw")

    # The above method works fine but takes O(n^2), because it calculated all substirngs.
    # we do not need to check substrings, because we only need the final score.
    K_res, S_res = 0, 0
    size = len(string)
    for i in range(0,size):
        if string[i] in ['A','E','I','O','U']:
            K_res += size-i #bcoz we only need to know which substring starts with vowel. so we dont need to know what characters are in the substring.
        else:
            S_res += size-i
    if K_res > S_res:
        print(f'Kevin {K_res}')
    elif S_res > K_res:
        print(f'Stuart {S_res}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)