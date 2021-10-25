highway_num = int(input())

#if statement to designate highway_num (200 as not valid)
if highway_num == 200:
 print(highway_num,'is not a valid interstate highway number.')
 
#if statement to designate highway_num (0 as not valid)
if highway_num == 0:
  print(highway_num,'is not a valid interstate highway number.')
  
#if statement to designate highway_num (>=1000 as not valid)
if highway_num >= 1000:
  print(highway_num,'is not a valid interstate highway number.')

#if statement to distinguish primary highway_number 1-99
if highway_num >= 1 and highway_num <= 99:
 primary = 'is primary,'
 
#if statement to distinguish even highway_number going east/west
 if (highway_num % 2) == 0:
  print('I-' + str(highway_num), primary, 'going east/west.')

#else statement to distinguish odd highway_num
 else:
  print('I-' + str(highway_num), primary, 'going north/south.')

#1st if statement to distinguish auxiliary highway_num (100-199)
if highway_num >= 100 and highway_num <= 199:
 auxiliary = 'is auxiliary,'

#if statement to distinguish even highway_num
 if (highway_num % 2) == 0:
  print('I-' + str(highway_num), auxiliary, 'serving I-%d, going east/west.' %
(highway_num%100))

#else statement to distinuish odd highway_num
 else:
  print('I-' + str(highway_num), auxiliary, 'serving I-%d, going north/south.' %
(highway_num%100))

#2nd if statement to distinguish auxiliary highway_num (201-999)
if highway_num >= 201 and highway_num <= 999:
 auxiliary = 'is auxiliary,'

#if statement to distinguish even highway_num
 if (highway_num % 2) == 0:
  print('I-' + str(highway_num), auxiliary, 'serving I-%d, going east/west.' % (highway_num%100))

#else statement to distinguish odd highway_num
 else:
  print('I-' + str(highway_num), auxiliary, 'serving I-%d, going north/south.' %
(highway_num%100))