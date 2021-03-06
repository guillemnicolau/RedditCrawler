#!/usr/bin/env python
################################################
#    Title: Reddit Crawler                     #
#    Author: Guillem Nicolau Alomar Sitjes     #
#    Date: September 1st, 2017                 #
#    Code version: 0.1                         #
#    Availability: Public                      #
################################################
import sqlite3
import errno
import os.path


class Database:

    def __init__(self, db_file_name):
        """
        This method creates the Database object and calls the database
        initializer.
        :param db_file_name: name and location of the database file
        """
        self.connection = Database.initialize_db(db_file_name)

    @staticmethod
    def initialize_db(db_file_name):
        """
        This method checks if the file exists, and if not, tries to create the
        folder containing it, and a blank file in that path. After that, returns
        a SQLite database instance linked to that file. 'check_same_thread
        parameter needs to be set to False to avoid problems between petitions.
        :param db_file_name: name and location of the database file
        :return: database connection
        """
        if not os.path.exists(os.path.dirname(db_file_name)):
            try:
                os.makedirs(os.path.dirname(db_file_name))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        if not os.path.isfile(db_file_name):
            db_file = open(db_file_name, 'w')
        else:
            db_file = open(db_file_name, 'r')
        db_file.close()
        return sqlite3.connect(db_file_name, check_same_thread=False)
