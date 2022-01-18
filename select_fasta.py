#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Verification of fasta file sequences
"""

__author__ = 'Mohamed Ouertani'

import argparse
import os
import sys
from collections import Counter
import re
import argcomplete
from Bio import SeqIO
from adn import is_valid


def create_parser():

    """ Declares new parser and adds parser arguments """

    program_description = ''' Reading fasta file and checking sequences '''
    parser = argparse.ArgumentParser(add_help=True,
                                     description=program_description)
    parser.add_argument('-i', '--inputfile', default=sys.stdin,
                        help="required input file in fasta format",
                        type=argparse.FileType("r"), required=True)
    parser.add_argument('-o', '--outputfile', default=sys.stdout,
                        help="optional output file in text format",
                        type=argparse.FileType("w"))
    parser.add_argument('-n', '--nucnumber',
                        help="Total number of nuclotides for each sequence",
                        action="store_true")
    parser.add_argument('-p', '--position',
                        help="Index of each non nucleotide character",
                        action="store_true")
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    args = args.__dict__
    return args


def input_file_checker():

    """ Checks for right input file """

    args = create_parser()
    input_message = ""
    input_path = args["inputfile"].name.lower()
    extension = os.path.splitext(input_path)[1]
    # recover only the extension value from the splitext function

    if extension not in [".fasta", ".fa"]:
        input_message = "This is not a valid fasta file , try again !"
        return False, input_message
    return True, input_message


def output_file_checker():

    """ Checks for right output file """

    args = create_parser()
    output_message = ""
    output_path = args["outputfile"].name.lower()
    extension = os.path.splitext(output_path)[1]
    # recover only the extension value from the splitext function

    if args["outputfile"] != sys.stdout:
        if extension == ".txt":
            return True, output_message
        if extension != ".txt":
            output_message = "output file should be .txt, try again !"
            os.system("rm %s" % args["outputfile"].name)
            return False, output_message
    return False, output_message


def sequence_checker():

    """ Checks fasta file sequences """

    args = create_parser()
    recs = SeqIO.parse(args['inputfile'].name, 'fasta')
    for record in recs:
        if args["nucnumber"]:
            print("%s has %s nucleotides." % (record.id, len(record.seq)))
        if not is_valid(record.seq):
            print(record.id, " is NOT a valid sequence.")
            if args["position"]:
                counts = Counter(record.seq)
                # count all occurences of any character found in the sequence
                for i in counts:
                    if i.upper() not in ["A", "C", "G", "T"]:
                        res = [j.start() for j in re.finditer(i, str(record.seq))]
                        # find all positions of the non nucleotide character
                        print("%s is found %s time(s) at position(s) %s"
                              % (i, counts.get(i), res))
            print("\n")
        else:
            print(record.id, " is a valid sequence.\n")


def output_file_writer():

    """ Writes output in specified output file """

    args = create_parser()
    original_stdout = sys.stdout
    sys.stdout = args["outputfile"]
    # redirecting output to specified output file
    print("Results for file %s :\n" % args["inputfile"].name)
    sequence_checker()
    sys.stdout = original_stdout
    print("Results are available in file : ", args["outputfile"].name)


def main():

    """ Main function for reading fasta file and checking sequence format """

    print("\nThis tool checks fasta file sequences\n")

    args = create_parser()
    input_check, input_message = input_file_checker()
    output_check, output_message = output_file_checker()

    if input_check is False:
        return print(input_message)
    if output_check is False and args["outputfile"] != sys.stdout:
        return print(output_message)
    if output_check is True:
        return output_file_writer()
    return sequence_checker()


if __name__ == "__main__":
    main()
