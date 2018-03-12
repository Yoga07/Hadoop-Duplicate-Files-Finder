# Hadoop-Duplicate-Files-Finder
A Python script to count and list the files and duplicate files statistics in an Hadoop Distributed File System Directory. This script also works for files having different names but the same content.

This is a recursive script, hence it is capable of running through the inner branches of the given directory.

Usage:python dir_dedup.py <HDFS DIRECTORY TO BE CHECKED>
  
  
Output Format:[<NAMES AND DIRECTORIES OF FILES IN LIST FORMAT(multiple items if duplicates are present)>],<COUNT OF THE DUPLICATES OF SAME FILE>  
