"""
Driver: Jordan Lin
Navigator: None
Assignment: Homework 3 - Enron
Date: 4_18_24
"""

import re
import sys
import argparse

def main(path):
    """Create an instance of Server path using the path that was passed in and save that to a variable

    Args:
        path (str): the path of the text file that will be parsed

    Returns:
        int: the length of the emails attribute of that instance
    """
    server = Server(path)
    return len(getattr(server, 'emails'))

class Server():
    """Stores the data for all emails found in the dataset

    Attributes:
        emails (list of Email objects): a list of Email objects where each object corresponds to one email
    """

    def __init__(self, path):
        """
        Opens file specified by the path for reading and sets the emails attribute to a list containg Email 
        objects. Each email instance should correspond to each individual email found in the text file

        Args:
            path (str): the path to the file that we are gong to read
        """

        file = open(path)
        text = file.read()
        emailList = text.split("End Email\"\n") #list of emails strings
        emailList.pop() 
        self.emails = []
        for x in emailList:
            tempList = x.splitlines()
            message_id = tempList[0][13:]
            date = tempList[1][6:]
            subject = tempList[4][9:]
            sender = tempList[2][6:]
            receiver = tempList[3][4:]
            body = ""
            for i in range(16, len(tempList)):
                body += tempList[i]
            self.emails.append(Email(message_id, date, subject, sender, receiver, body))

class Email():
    """Stores the data related to individual email messages

    Attributes:
        message_id (str): the message-id that is unique to each email message
        date (str): the date associated with each email message.
        subject (str): the subject of each email message
        sender: (str): the sender of each email message
        receiver (str): the receiver of each email message
        body (str): the body of each email message
    """
    def __init__(self, message_id, date, subject, sender, receiver, body):
        """Sets the parameters to the corresponding attributes

        Args:
            message_id (str): the message-id that is unique to each email message
            date (str): the date associated with each email message.
            subject (str): the subject of each email message
            sender (str): the sender of each email message
            receiver (str): the receiver of each email message
            body (str): the body of each email message
        """
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender
        self.receiver = receiver
        self.body = body

def parse_args(args_list):
    """Create an instance of ArgumentParser and the path to the text file as an argument

    Args:
        args_list (list): a list of strings containing the command-line arguments for the program

    Returns:
        ArgumentParser: the ArgumentParser object created
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args(args_list)
    return args

#pass in path extracted from command line to main
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.path)