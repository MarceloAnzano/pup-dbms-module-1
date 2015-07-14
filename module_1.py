import sys
import csv


#1. Which Region have the most State Universities?
def get_region_with_most_suc():
  csvFile =  open('suc_ph.csv','r')
  data = csv.reader(csvFile)
  dic = {}
  for row in data:
    if dic.has_key(row[0]):
      dic[row[0]] += 1
    else:
      dic[row[0]] = 1
  print("1. The region with the most SUC is %s") % ((sorted(dic.items(), key=lambda n: n[1]))[-1][0])

#2. Which Region have the most enrollees?
def get_region_with_most_enrollees_by_school_year(school_year):
  csvFile = open('suc_ph.csv','r')
  data = csv.reader(csvFile)
  dic = {}
  if school_year == "2010-2011":
    col = 2
  elif school_year == "2011-2012":
    col = 3
  elif school_year == "2012-2013":
    col = 4
  else:
    print "2. ERROR! Not included in tha database"
    return 0
  for row in data:
    if dic.has_key(row[0]):
      try: 
        dic[row[0]] += int(row[col])
      except Exception:
        dic[row[0]] += 0
    else:
      try: 
        dic[row[0]] = int(row[col])
      except Exception:
        dic[row[0]] = 0
  print("2. The region with the most SUC enrollees in school year %s is %s") % (school_year, (sorted(dic.items(), key=lambda n: n[1]))[-1][0])

#3. Which Region have the most graduates?
def get_region_with_most_graduates_by_school_year(school_year):
  csvFile = open('suc_ph.csv','r')
  data = csv.reader(csvFile)
  dic = {}
  if school_year == "2009-2010":
    col = 5
  elif school_year == "2010-2011":
    col = 6
  elif school_year == "2011-2012":
    col = 7
  else:
    print "3. ERROR! Not included in tha database"
    return 0
  for row in data:
    if dic.has_key(row[0]):
      try: 
        dic[row[0]] += int(row[col])
      except Exception:
        dic[row[0]] += 0
    else:
      try: 
        dic[row[0]] = int(row[col])
      except Exception:
        dic[row[0]] = 0
  print("3. The region with the most SUC graduates in school year %s is %s") % (school_year, (sorted(dic.items(), key=lambda n: n[1]))[-1][0])

#4 top 3 SUC who has the chepeast tuition fee by schoolyear
def get_top_3_cheapest_by_school_year(level, school_year):
  csvFile = open('tuitionfeeperunitsucproglevel20102013.csv','r')
  data = csv.reader(csvFile)
  level = level.upper()
  dic = {}
  if school_year == "2010-2011":
    col = 2
  elif school_year == "2011-2012":
    col = 5
  elif school_year == "2012-2013":
    col = 8
  else:
    print "4. ERROR! Not included in tha database"
    return 0
  
  if level == "AB" or level == "BS":
    col += 0
  elif level == "MS" or level == "MA":
    col += 1
  elif level == "PHD":
    col += 2
  else:
    print "4. ERROR! Not included in tha database"
    return 0

  for row in data:
    try:
      if int(row[col]) > 0:
        dic[row[1]] = int(row[col])
    except Exception:
      pass

  #print ((sorted(dic.items(), key=lambda n: n[1]))[0])

  print("4. Top 3 cheapest SUC for %s level in school year %s") % (level, school_year)
  print ("  1. %s") % ((sorted(dic.items(), key=lambda (n,m): (m,n)))[0][0])
  print ("  2. %s") % ((sorted(dic.items(), key=lambda (n,m): (m,n)))[1][0])
  print ("  3. %s") % ((sorted(dic.items(), key=lambda (n,m): (m,n)))[2][0])

#5 top 3 SUC who has the most expensive tuition fee by schoolyear
def get_top_3_most_expensive_by_school_year(level, school_year):
  csvFile = open('tuitionfeeperunitsucproglevel20102013.csv','r')
  data = csv.reader(csvFile)
  level = level.upper()
  dic = {}
  if school_year == "2010-2011":
    col = 2
  elif school_year == "2011-2012":
    col = 5
  elif school_year == "2012-2013":
    col = 8
  else:
    print "5. ERROR! Not included in tha database"
    return 0
  
  if level == "AB" or level == "BS":
    col += 0
  elif level == "MS" or level == "MA":
    col += 1
  elif level == "PHD":
    col += 2
  else:
    print "5. ERROR! Not included in tha database"
    return 0

  for row in data:
    try:
      if int(row[col]) > 0:
        dic[row[1]] = int(row[col])
    except Exception:
      pass

  print("5. Top 3 expensive SUC for %s level in school year %s") % (level, school_year)
  print ("  1. %s") % ((sorted(dic.items(), key=lambda (n,m): (m,n)))[-1][0])
  print ("  2. %s") % ((sorted(dic.items(), key=lambda (n,m): (m,n)))[-2][0])
  print ("  3. %s") % ((sorted(dic.items(), key=lambda (n,m): (m,n)))[-3][0])

#6 list all SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013
def all_suc_who_have_increased_tuition_fee():
  csvFile = open('tuitionfeeperunitsucproglevel20102013.csv','r')
  data = csv.reader(csvFile)
  dic = []
  col = 2
  for row in data:
    try:
      if int(row[col+3]) > int(row[col]):
        dic.append(row[col-1])
      elif int(row[col+4]) > int(row[col+1]):
        dic.append(row[col-1])
      elif int(row[col+5]) > int(row[col+2]):
        dic.append(row[col-1])
      elif int(row[col+6]) > int(row[col]):
        dic.append(row[col-1])
      elif int(row[col+7]) > int(row[col+1]):
        dic.append(row[col-1])
      elif int(row[col+8]) > int(row[col+2]):
        dic.append(row[col-1])
      elif int(row[col+6]) > int(row[col]+3):
        dic.append(row[col-1])
      elif int(row[col+7]) > int(row[col+4]):
        dic.append(row[col-1])
      elif int(row[col+8]) > int(row[col+5]):
        dic.append(row[col-1])
    except Exception:
      pass

  print "6. List of SUC who have increased their tuition fee from school year 2010-2011 to 2012-2013"
  ctr = 1
  for item in dic:
    print("  %d. %s") % (ctr, item)
    ctr += 1



#7 which discipline has the highest passing rate?
def get_discipline_with_highest_passing_rate_by_shool_year(school_year):
  csvFile = open('performancesucprclicensureexam20102012.csv','r')
  data = csv.reader(csvFile)
  dicPass = {}
  dicTake = {}
  dicRate  = {}
  if school_year == "2010-2011":
    col = 3
  elif school_year == "2011-2012":
    col = 4
  elif school_year == "2012-2013":
    col = 5
  else:
    print "7. ERROR! Not included in tha database"
    return 0

  for row in data:
    try:
      if dicPass.has_key(row[2]) and row[2] != "Total" and row[2] != "-":
        dicPass[row[2]] += int(row[col])
        dicTake[row[2]] += int(row[col+4])
      else:
        dicPass[row[2]] = int(row[col])
        dicTake[row[2]] = int(row[col+4])
    except Exception:
      pass
  #print dicPass
  #print dicTake

  for d in dicPass:
    try:
      if d != "-":
        dicRate[d] = (float(dicTake[d] -  float(dicPass[d]))/float(dicTake[d]))
    except Exception:
      pass
  print("7. The discipline which has the highest passing rate is %s") % ((sorted(dicRate.items(), key=lambda (n,m): (-m,n)))[0][0])

#8 list top 3 SUC with the most passing rate by discipline by school year
def get_top_3_suc_performer_by_discipline_by_year(discipline, school_year):
  csvFile = open('performancesucprclicensureexam20102012.csv','r')
  data = csv.reader(csvFile)
  dicPass = {}
  dicTake = {}
  dicRate  = {}
  if school_year == "2010":
    col = 3
  elif school_year == "2011":
    col = 4
  elif school_year == "2012":
    col = 5
  else:
    print "8. ERROR! Not included in tha database"
    return 0

  for row in data:
    try:
      if row[2] == discipline:
        if dicPass.has_key(row[1]):
          dicPass[row[1]] += int(row[col])
          dicTake[row[1]] += int(row[col+4])
        else:
          dicPass[row[1]] = int(row[col])
          dicTake[row[1]] = int(row[col+4])
    except Exception:
      pass
  #print dicPass
  #print dicTake

  for d in dicPass:
    try:
      if d != "-":
        dicRate[d] = (float(dicTake[d] -  float(dicPass[d]))/float(dicTake[d]))
    except Exception:
      pass
  print("8. list top 3 SUC with the most passing rate by discipline by school year")
  print(" 1. %s") % ((sorted(dicRate.items(), key=lambda (n,m): (-m,n)))[0][0])
  print(" 2. %s") % ((sorted(dicRate.items(), key=lambda (n,m): (-m,n)))[1][0])
  print(" 3. %s") % ((sorted(dicRate.items(), key=lambda (n,m): (-m,n)))[2][0])

def main():
  get_region_with_most_suc()
  get_region_with_most_enrollees_by_school_year('2010-2011')
  get_region_with_most_graduates_by_school_year('2010-2011')
  get_top_3_cheapest_by_school_year('BS', '2010-2011')
  get_top_3_most_expensive_by_school_year('BS', '2010-2011')
  all_suc_who_have_increased_tuition_fee()
  get_discipline_with_highest_passing_rate_by_shool_year('2010-2011')
  get_top_3_suc_performer_by_discipline_by_year('Accountancy', '2011')


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()