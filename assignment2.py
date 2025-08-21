# 1.Find the sum of elements in a list.
import collections
from itertools import product
from operator import countOf

# lst = [8,2,9,3,7]
# print(sum(lst))
# 2.Write a Python program to find the largest and smallest element in a list.
# lst = [8,2,9,3,7]
# print(max(lst))
# print(min(lst))
# 3. Create a list of characters. Write a program to reverse the order of the elements in the list without using built-in functions. Use indexing method.
# lst1=["red","violet","blue","green","orange","purple"]
# print(sorted(lst1))
# 4. Write a Python program to find the index of an element in a list.
# lst1=["red","violet","blue","green","orange","purple"]
# ind=lst1.index("blue")
# print(ind)
# 5. Write a program to add item 7000 after 6000 in the following Python List.
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
# 6. You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
# list1 = [5, 10, 15, 20, 25, 50, 20]
# ind=list1.index(20)
# list1[ind]=200
# print(list1)
# 7. Create a list of numbers. Write a program to find the range (difference between the largest and smallest element) of the list.
# num=[1,2,3,4,5,6,7,8,9]
# range=max(num)-min(num)
# print(range)
# 8. Write a Python program to find the frequency of each element in a list and store it in a dictionary.
# numbers=[1,2,3,4,5,6,7,8,9]
# frequency=collections.Counter(numbers)
# dict=dict(frequency)
# print(dict)
# print(frequency)
# 9. Create a list of numbers. Write a program to insert a new element at a specific position in the list.
# list1=[1,2,3,4,5,6,7,8,9]
# list1.insert(1,100)
# print(list1)
# 10. Write a Python program to remove duplicates from a list.
# list1=[1,2,3,4,5,4,2,6,8,1,8,3,7,7]
# duplicates=set(list1)
# print(duplicates)
# 11.Remove empty strings from the list of strings without using any loops.
# char=["apple","","banana","orange","",'']
# empty=list(filter(None,char))
# print(empty)
# 12. Write a Python program to find the common elements between two lists.
# list1=[1,2,3,4,5,6,7,8,9]
# list2=[2,3,4,7,5,22,12,11]
# list3= list(set(list1) & set(list2))
# print(list3)
# 13. Write a Python program to find the common elements between two lists without using loops.
# 14. Write a Python program to find the second smallest element in a list.
# list1=[1,2,3,4,5,6,7,8,9]
# print(min(list1))
# 15. Write a Python program to check if a list is empty.
# list1=[]
# if len(list1)==0:
#     print("my list is empty")
# else:
#     print("my list is not empty")
# 16. Write a Python program to find the sum of elements at odd indices in a list.
# list1=[1,2,3,4,5,6,7,8,9]
# odd_indices=sum(list1[1::2])
# print(odd_indices)
# 17. Write a Python program to find the common elements among three lists.
# list_a = [1, 2, 3, 4, 5]
# list_b = [3, 4, 5, 6, 7]
# list_c = [5, 6, 7, 8, 9,4]
# list4=set(list_a) & set(list_b) & set(list_c)
# print(list4)
# 18.Write a Python program to find the k smallest elements in a list.
# mylist = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,0]
# k=5
# num=sorted(mylist)
# sort=num[:k]
# print(sort)
# 19.Write a Python program to find the largest product of two distinct elements in a list.
# list1=[1,2,3,4,5,6,7,8,9]

# string assignment:
# 1.Write a program that takes two numbers as input and prints their sum.
# num1=int(input("enter a first number:"))
# num2=int(input("enter a second number:"))
# sum=num1+num2
# print(f"the sum of {num1} and {num2} is :{sum}")
# 2. Write a program that takes a string as input and prints its length.
# string=input("enter a string:")
# range=len(string)
# print(f"the length of the string is :{range}")
# 3. Write a program that takes a sentence and then prints the number of words in that sentence.
# sentence=input("enter a sentence:")
# words=sentence.split()
# print(f"the length of  words in the sentence is :{len(words)}")
# 4. Write a program that takes a string as input and counts the number of uppercase letters in the string.
# string=input("enter a string:")
# uppercase=0
# for char in string:
#     if char.isupper():
#         uppercase+=1
# print(f"the length of uppercase letters in the string is :{(uppercase)}")
# x=input("enter a stirng")
# upper=0
# for i in x:
#     if i.isupper():
#         upper+=1
# print(upper)
# 5. Write a program that takes a sentence and then converts all the characters to uppercase.
# sentence="iam python fullstack developer"
# print(sentence.upper())
# 6. Write a program that takes a string as input and replaces all occurrences of the letter ‘a’ with the letter ‘e’.
# string = input("Enter a string: ")
# string2 =string.replace('a', 'e')
# print("replace all occurence of the letter a with the letter e string:", string2)
# 7. Create a program that checks if two given strings are anagrams of each other.
# word1="laugh"
# word2="caugh"
# if word1 in word2:
#     print(word1)


#8. Create a program that checks if a given string is a palindrome.
# def check_string (main_string,substring):
#     if substring in main_string:
#         return "yes,the substring is present in the main string"
#     else:
#         return "no,the substring is not present in the main string"

# ex:2
# word=input("Enter a word: ")
# newword=word[::-1]
# if newword==word:
#     print("give word is palindrome")
# else:
#     print("give word is not palindrome")
# main_string = input("Enter the main string: ")
# substring = input("Enter the substring: ")
# print(check_string(main_string, substring))
# 9. Create a program that checks if a substring is present in a given string.
# string="mindx solutions"
# sub_string="mindx"
# if sub_string in string:
#     print("sub_string is present")
# else:
#     print("sub_string is not present")
# 10. Write a program that reverses the order of words in a given sentence.
# sentence=["python", "is a free and open source", "it is a platform independent."]
# sentence.reverse()
# print(sentence)
# 11. Implement a Caesar cipher encryption and decryption program. the key (shift) value of this message is 3.
# The formula of encryption is: En (x) = (x + n) mod 26.
# 12. Write a program that counts the number of vowels in a given string.
# vowels="vowels"
# print(vowels.count("e"))
# 13. Create a program that converts a given sentence into Pig Latin (move the first letter of each word to the end and add “ay”).
# sentence="mindx solutions"
# words=sentence.split(" ")
# newsentence=" "
# for i in words:
#     newsentence+=(i[1:]+i[:1]+"ay")
# print(newsentence)
# 14. Write a program that capitalizes the first letter of each sentence in a given paragraph.
# string="python is a free and open source"
# print(string.title())
# 15. Write a program that finds the longest word in a given sentence.
# name="mindx solutions"
# words=name.split()
# output=max(words,key=(len))
# print(output)
# 16. Write a program that reverses the order of words in a given sentence.
# sentence=["iam", "a python", "fullstack", "developer"]
# sentence.reverse()
# print(sentence)
# 17. Given a list of strings, write a program to find all pairs of strings that are palindromes.
# string=['car','race','rat','tar']
# rev=[]
# for i in string:
#     if i[::-1] in string:
#         if i not in rev:
#             rev.append(i[::-1])
#     print(i)
# 18. Given three strings, write a program to check if the third string can be formed by interleaving the characters of the first two strings.
# s1="blue"
# s2="berry"
# s3="cherry"
# if sorted(s3) ==sorted(s1+s2):
#     print("s3 is interleaving to s1 and s2")
# else:
#     print("s3 is not interleaving to s1 and s2")
# 19. Write a program to find all permutations of a smaller string within a larger string.















