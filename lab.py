documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}
def p():
 num=input("Write document number ")
 for i in documents:
  if num in i["number"]:
    k= i["name"]
    break
  else:
   k= "There isn't document with this number "
 return print(k)

def p1(num:str):
 for i in documents:
  if num in i["number"]:
    k= i["name"]
    break
  else:
   k= " "
 return k

def s():
 num = input("Write document number ")
 for i in directories:
  if num in directories[i]:
   k = i
   break
  else:
   k = "Document isn't in the base "
 return print(k)


def s1(num: str):
 for i in directories:
  if num in directories[i]:
   k = i
   break
  else:
   k = "Document isn't in the base "
 return k


def palka():
 for i in documents:
  print("N: ", i["number"]+",", " type: ", i["type"]+",", " Owner: ", i["name"]+",", " shelf storage: ", s1(i["number"]) )
 return


def ads():
 num= input("Write new shelf ")
 if num in directories:
  print("Shelf with this number is existing", )
 else:
  directories.setdefault(num,[])
  print("Shelf added successfully")
 dir=[i for i in directories]
 dir=", ".join(dir)
 return print( "Available shelfs: ", dir)


def ds():
 num= input("Write shelf you want to delete ")
 if num in directories:
  for i in directories:
   if num==i:
    if directories[i]==[]:
     print("Shelf deleted successfully")
     directories.pop(i)
     break
    else:
     print("There are documents on this shelf ")
     break
 else:
   print("This shelf doesn't exist")
 dir=[i for i in directories]
 dir=", ".join(dir)
 return print( "Available shelfs: ", dir)

def ad():
 num=input("Write new number of the document ")
 own=input("Write owner of the document ")
 typ=input("Write type of the document ")
 she=input("Write shelf of the document ")
 if she in directories:
  directories[she].append(num)
 else:
  print("Use command ads to add this shelf")
  print("Current list of documents: ")
  palka()
  return
 documents.append({'type': typ, 'number': num, 'name': own})
 print("Current list of documents: ")
 palka()
 return

def d():
 num=input("Write number of the document ")
 for i in documents:
  if num == i["number"]:
    print("Document deleted")
    documents.remove(i)
    break
  elif p1(num)==" ":
   print("There is no document with this number")
   break
 print("Current list of documents: ")
 palka()
 return


def m():
 num = input("Write number of the document ")
 she = input("Write shelf of the document ")
 if she in directories and p1(num)!=" ":
  directories[s1(num)].remove(num)
  directories[she].append(num)
 elif p1(num)==" ":
  print("There is no document with this number")
 elif not she in directories:
  print("Use command ads to add this shelf")
 print("Current list of documents: ")
 palka()
 return
def commands():
 com=input("Write command ")
 if com=="p":
  return p()
 elif com=="s":
  return s()
 elif com=="|":
  return palka()
 elif com=="ds":
  return ds()
 elif com=="ads":
  return ads()
 elif com=="ad":
  return ad()
 elif com=="d":
  return d()
 elif com=="m":
  return m()
 else:
  return print("Unknown command")
commands()