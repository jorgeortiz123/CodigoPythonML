#Simple Loop
people= ['Andres','Alejandra','Benito','Jose']
print ('****SIMPLE LOOP****')
for person in people:
 print ('Current Person: {0}'.format(person))


#Break
print('***Break Loop***')
for person in people:
  if person == 'Benito':
    break
  print('Current Person: {0}'.format(person))

#Continue
print('****CONTINUE LOOP****')
for person in people:
  if person == 'Benito':
   continue
  print('Current oerson') 

