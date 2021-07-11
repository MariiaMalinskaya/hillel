# true filereader

import os
import re
import codecs
import shutil
#import *script*


### dicts with regexes


scan = os.listdir('/')
positive_files_extension = 0
negative_files_extension = 0
for obj in scan:
	if obj.split('.')[-1] == 'java':  
		positive_files_extension +=1

	else:
		negative_files_extension +=1 

tested_files = 0
negative_obj = 0
passed_obj = 0
file_that_should_be_cought = 0
file_more_than_1kb = 0 
right_files = 0 
false_positive = 0 

scan = os.listdir('/')
for obj in enumerate(scan):
	tested_files +=1
	data = codecs.open(obj[1], 'r', 'latin-1').read()
	result = isSourceCode(data, java_dict)
	if result == [0]:
		negative_obj +=1
		if obj[1].split('.')[-1] == 'java':
			file_that_should_be_cought +=1
			file_size = os.path.getsize(obj[1])
			if file_size > 1024:
				file_more_than_1kb +=1
				print  obj,'FN!'
	else:
		passed_obj +=1
		result_string = str(result)
		if obj[1].split('.')[-1] == 'java':
			right_files += 1
			# print obj, right_files
		else:
			false_positive +=1
			print obj,'mistake!'
		# print obj, result_string
print 'how much files in %s' %tested_files
print 'positive obj %s' %positive_files_extension
print 'negative obj %s' %negative_files_extension
print 'files more 1Kb %s' %file_more_than_1kb
FP = passed_obj - right_files
FN = (file_that_should_be_cought * 100)/tested_files
procentage_FP = FP * 100/tested_files
# print 'passed objs %s' %passed_obj
print '[1] files %s' % passed_obj,'right caught %s' % right_files, 'FP %s' %FP
print '[0] files %s' % negative_obj, 'FN %s' %file_that_should_be_cought
print 'FP %s percent' % procentage_FP 
print 'FN %s persent' %FN 

positive_procentage = (right_files*100)/positive_files_extension
print 'positive procentage %s' %positive_procentage
# negative_procentage = negative_obj*100/swift_files
# print 'posivite files %s procent from %s'%(positive_procentage, obj_counter)
# print 'negative files %s procent from %s'%(neagtive_procentage, obj_counter)
		# result_end = re.match("[1, (u'This text was identified as Swift source code. (\d{1,3}) unmistakable Swift lines were detected. In total, (\d{1,3}\.\d{1,2}) percent of (\d{1,5}) non-empty lines in the file were detected to be valid Swift lines.', 0, 0, False)]",result_string)
		# try:
		# 	amount_of_line = result_end.group(1)
		# 	percent_of_line = result_end.group(2)
		# 	file_lines  =result_end.group(3)
		# except AttributeError as ae:
  #           print str(ae), "\skipping line:", result_string
		# print obj, result_end.group(1),result_end.group(2),result_end.group(3)
# print 'file in a folder %s'%(obj_counter)
# print 'caught files %s '%(right_files)
# print 'not java files %s '%(negative_files)
# print 'procentage of caught files %s'%(positive_procentage)
# print 'how much files should be caught more %s'%(g)
# print 'java files that are not caught %s'%(file_that_should_be_cought)
# print 'files more than 1Kb %s' %(file_more_than_1kb)









