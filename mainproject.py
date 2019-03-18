print("welcome to movie success predictor")
print("please enter the name of movie")
movie=raw_input()
#for director
print("please enter the name of the director")
print("Do you want to skip this parameter(Y/N)")
ans= raw_input()
if (ans=='Y' or ans=='y'):
	print("please enter the name of the hero")
	print("Do you want to skip this parameter(Y/N)")
	ans1= raw_input()
	if (ans1=='Y' or ans1=='y'):
		print("please enter the name of the herione")
		print("Do you want to skip this parameter(Y/N)")
		ans2= raw_input()
		if (ans2=='Y' or ans2=='y'):
			print("please enter the name of the music director")
			print("Do you want to skip this parameter(Y/N)")
			ans3= raw_input()
			if (ans3=='Y' or ans3=='y'):
				count = 0

				from director import m_director
				dire = 0

				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				heroine = 0

				from musicfile import music_director
				md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				ans1=raw_input("do u want to access admin login y/n")
				print "\n"
				if(ans1=='y' or ans1=='Y') :
						admin=raw_input("Admin Login:\t ") ##main menu
						print "\n"
						if admin=="1":
							passw=raw_input("Enter the password: \t")				##login
							if passw=="iiitn":
								option=raw_input("Press 1 to display the entries.\nPress 3 to exit:\t")	 ##admin functions
								print "\n"
							 
							if option=="1":
							    print(movie)
							    print(name)
							    print(name_h)
							    print(name_he)
							    print(name_md)
							elif option=="3":
							    quit()
					

			elif (ans3=='N' or ans3=='n'):
				print("please enter the name of the music director")
				name_md = raw_input()
				count = 0

				from director import m_director
				dire = 0


				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				heroine = 0

				from musicfile import music_director
				if name_md in music_director:

					md = music_director[name_md]
					count = count +1
				else :

					md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				ans1=raw_input("do u want to access admin login y/n")
				print "\n"
				if(ans1=='y' or ans1=='Y') :
						admin=raw_input("Admin Login:\t ") ##main menu
						print "\n"
						if admin=="1":
							passw=raw_input("Enter the password: \t")				##login
							if passw=="iiitn":
								option=raw_input("Press 1 to display the entries.\nPress 3 to exit:\t")	 ##admin functions
								print "\n"
							 
							if option=="1":
							    print(movie)
							    print(name)
							    print(name_h)
							    print(name_he)
							    print(name_md)
							elif option=="3":
							    quit()
				        
					

		#for heroine
		elif (ans2=='n' or ans2=='N'):
			print("please enter the name of the heroine")
			name_he = raw_input()
			print("please enter the name of the music director")
			print("Do you want to skip this parameter(Y/N)")
			ans3= raw_input()
			if (ans3=='Y' or ans3=='y'):
				count = 0

				from director import m_director
				dire = 0

				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				if name_he in heroines:	 
					heroine = heroines[name_he]
					count = count +1
				else :
					heroine = 0
				from musicfile import music_director
				md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				        quit()
					

			elif (ans3=='N' or ans3=='n'):
				print("please enter the name of the music director")
				name_md = raw_input()
				count = 0

				from director import m_director
				dire = 0


				from herofile import heroes
				hero = 0

				from heroinefile import heroines

				if name_he in heroines: 
					heroine = heroines[name_he]
					count = count +1
				else :
					heroine = 0

				from musicfile import music_director
				if name_md in music_director:

					md = music_director[name_md]
					count = count +1
				else :
					md = 0
				rating = [dire, hero, heroine, md]
				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				ans1=raw_input("do u want to access admin login y/n")
				print "\n"
				if(ans1=='y' or ans1=='Y') :
						admin=raw_input("Admin Login:\t ") ##main menu
						print "\n"
						if admin=="1":
							passw=raw_input("Enter the password: \t")				##login
							if passw=="iiitn":
								option=raw_input("Press 1 to display the entries.\nPress 3 to exit:\t")	 ##admin functions
								print "\n"
							 
							if option=="1":
							    print(movie)
							    print(name)
							    print(name_h)
							    print(name_he)
							    print(name_md)
							elif option=="3":
							    quit()
					
					


	#for hero
	elif (ans1=='n' or ans1=='N'):
		print("please enter the name of the hero")
		name_h=raw_input()
		print("please enter the name of the herione")
		print("Do you want to skip this parameter(Y/N)")
		ans2= raw_input()
		if (ans2=='Y' or ans2=='y'):
			print("please enter the name of the music director")
			print("Do you want to skip this parameter(Y/N)")
			ans3= raw_input()
			if (ans3=='Y' or ans3=='y'):
				count = 0

				from director import m_director
				dire = 0

				from herofile import heroes
				if name_h in heroes:
					hero = heroes[name_h]
					count = count +1
				else :
					hero = 0

				from heroinefile import heroines
				heroine = 0

				from musicfile import music_director
				md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				        quit()
					

			elif (ans3=='N' or ans3=='n'):
				print("please enter the name of the music director")
				name_md = raw_input()
				count = 0

				from director import m_director
				dire = 0


				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				heroine = 0

				from musicfile import music_director
				if name_md in music_director:

					md = music_director[name_md]
					count = count +1
				else :

					md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				ans1=raw_input("do u want to access admin login y/n")
				print "\n"
				if(ans1=='y' or ans1=='Y') :
						admin=raw_input("Admin Login:\t ") ##main menu
						print "\n"
						if admin=="1":
							passw=raw_input("Enter the password: \t")				##login
							if passw=="iiitn":
								option=raw_input("Press 1 to display the entries.\nPress 3 to exit:\t")	 ##admin functions
								print "\n"
							 
							if option=="1":
							    print(movie)
							    print(name)
							    print(name_h)
							    print(name_he)
							    print(name_md)
							elif option=="3":
							    quit()
				        
					

		#for heroine
		elif (ans2=='n' or ans2=='N'):
			print("please enter the name of the heroine")
			name_he = raw_input()
			print("please enter the name of the music director")
			print("Do you want to skip this parameter(Y/N)")
			ans3= raw_input()
			if (ans3=='Y' or ans3=='y'):
				count = 0

				from director import m_director
				dire = 0

				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				if name_he in heroines:	 
					heroine = heroines[name_he]
					count = count +1
				else :
					heroine = 0
				from musicfile import music_director
				md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				        quit()
					

			elif (ans3=='N' or ans3=='n'):
				print("please enter the name of the music director")
				name_md = raw_input()
				count = 0

				from director import m_director
				dire = 0


				from herofile import heroes
				hero = 0

				from heroinefile import heroines

				if name_he in heroines: 
					heroine = heroines[name_he]
					count = count +1
				else :
					heroine = 0

				from musicfile import music_director
				if name_md in music_director:

					md = music_director[name_md]
					count = count +1
				else :
					md = 0
				rating = [dire, hero, heroine, md]
				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				ans1=raw_input("do u want to access admin login y/n")
				print "\n"
				if(ans1=='y' or ans1=='Y') :
						admin=raw_input("Admin Login:\t ") ##main menu
						print "\n"
						if admin=="1":
							passw=raw_input("Enter the password: \t")				##login
							if passw=="iiitn":
								option=raw_input("Press 1 to display the entries.\nPress 3 to exit:\t")	 ##admin functions
								print "\n"
							 
							if option=="1":
							    print(movie)
							    print(name)
							    print(name_h)
							    print(name_he)
							    print(name_md)
							elif option=="3":
							    quit()
				        
					

elif (ans=='N' or ans=='n'):
	print("please enter the name of the director")
	name=raw_input()
	print("please enter the name of the hero")
	print("Do you want to skip this parameter(Y/N)")
	ans1= raw_input()
	if (ans1=='Y' or ans1=='y'):
		print("please enter the name of the herione")
		print("Do you want to skip this parameter(Y/N)")
		ans2= raw_input()
		if (ans2=='Y' or ans2=='y'):
			print("please enter the name of the music director")
			print("Do you want to skip this parameter(Y/N)")
			ans3= raw_input()
			if (ans3=='Y' or ans3=='y'):
				count = 0

				from director import m_director
				if name in m_director :
                                   dire = m_director[name]
                                   count = count +1
				else :
				   dire = 0

				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				heroine = 0

				from musicfile import music_director
				md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				        quit()
					

			elif (ans3=='N' or ans3=='n'):
				print("please enter the name of the music director")
				name_md = raw_input()
				count = 0

				from director import m_director
				dire = 0


				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				heroine = 0

				from musicfile import music_director
				if name_md in music_director:

					md = music_director[name_md]
					count = count +1
				else :

					md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				ans1=raw_input("do u want to access admin login y/n")
				print "\n"
				if(ans1=='y' or ans1=='Y') :
						admin=raw_input("Admin Login:\t ") ##main menu
						print "\n"
						if admin=="1":
							passw=raw_input("Enter the password: \t")				##login
							if passw=="iiitn":
								option=raw_input("Press 1 to display the entries.\nPress 3 to exit:\t")	 ##admin functions
								print "\n"
							 
							if option=="1":
							    print(movie)
							    print(name)
							    print(name_h)
							    print(name_he)
							    print(name_md)
							elif option=="3":
							    quit()
				        

		#for heroine
		elif (ans2=='n' or ans2=='N'):
			print("please enter the name of the heroine")
			name_he = raw_input()
			print("please enter the name of the music director")
			print("Do you want to skip this parameter(Y/N)")
			ans3= raw_input()
			if (ans3=='Y' or ans3=='y'):
				count = 0

				from director import m_director
				dire = 0

				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				if name_he in heroines:	 
					heroine = heroines[name_he]
					count = count +1
				else :
					heroine = 0
				from musicfile import music_director
				md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				        quit()
					

			elif (ans3=='N' or ans3=='n'):
				print("please enter the name of the music director")
				name_md = raw_input()
				count = 0

				from director import m_director
				dire = 0


				from herofile import heroes
				hero = 0

				from heroinefile import heroines

				if name_he in heroines: 
					heroine = heroines[name_he]
					count = count +1
				else :
					heroine = 0

				from musicfile import music_director
				if name_md in music_director:

					md = music_director[name_md]
					count = count +1
				else :
					md = 0
				rating = [dire, hero, heroine, md]
				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				ans1=raw_input("do u want to access admin login y/n")
				print "\n"
				if(ans1=='y' or ans1=='Y') :
						admin=raw_input("Admin Login:\t ") ##main menu
						print "\n"
						if admin=="1":
							passw=raw_input("Enter the password: \t")				##login
							if passw=="iiitn":
								option=raw_input("Press 1 to display the entries.\nPress 3 to exit:\t")	 ##admin functions
								print "\n"
							 
							if option=="1":
							    print(movie)
							    print(name)
							    print(name_h)
							    print(name_he)
							    print(name_md)
							elif option=="3":
							    quit()
				        


	#for hero
	elif (ans1=='n' or ans1=='N'):
		print("please enter the name of the hero")
		name_h=raw_input()
		print("please enter the name of the herione")
		print("Do you want to skip this parameter(Y/N)")
		ans2= raw_input()
		if (ans2=='Y' or ans2=='y'):
			print("please enter the name of the music director")
			print("Do you want to skip this parameter(Y/N)")
			ans3= raw_input()
			if (ans3=='Y' or ans3=='y'):
				count = 0

				from director import m_director
				if name in m_director :
                                   dire = m_director[name]
                                   count = count +1
				else :
				   dire = 0

				from herofile import heroes
				if name_h in heroes:
					hero = heroes[name_h]
					count = count +1
				else :
					hero = 0

				from heroinefile import heroines
				heroine = 0

				from musicfile import music_director
				md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				        quit()

			elif (ans3=='N' or ans3=='n'):
				print("please enter the name of the music director")
				name_md = raw_input()
				count = 0

				from director import m_director
				dire = 0


				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				heroine = 0

				from musicfile import music_director
				if name_md in music_director:

					md = music_director[name_md]
					count = count +1
				else :

					md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				        quit()
					

		#for heroine
		elif (ans2=='n' or ans2=='N'):
			print("please enter the name of the heroine")
			name_he = raw_input()
			print("please enter the name of the music director")
			print("Do you want to skip this parameter(Y/N)")
			ans3= raw_input()
			if (ans3=='Y' or ans3=='y'):
				count = 0

				from director import m_director
				dire = 0

				from herofile import heroes
				hero = 0

				from heroinefile import heroines
				if name_he in heroines:	 
					heroine = heroines[name_he]
					count = count +1
				else :
					heroine = 0
				from musicfile import music_director
				md = 0

				rating = [dire, hero, heroine, md]

				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				        quit()

			elif (ans3=='N' or ans3=='n'):
				print("please enter the name of the music director")
				name_md = raw_input()
				count = 0

				from director import m_director
				dire = 0


				from herofile import heroes
				hero = 0

				from heroinefile import heroines

				if name_he in heroines: 
					heroine = heroines[name_he]
					count = count +1
				else :
					heroine = 0

				from musicfile import music_director
				if name_md in music_director:

					md = music_director[name_md]
					count = count +1
				else :
					md = 0
				rating = [dire, hero, heroine, md]
				if (count > 0):
					n=(sum(rating) / count )
				else: 
					print("sorry!! Not found in dictionary")
					n=-1 

				if (n > 0 and n < 4):
					print("FLOP")

				elif (n > 4 and n <= 6) :
					print("AVERAGE")

				elif (n > 6 and n < 8) :
					print("HIT")

				elif(n >=8 and n <= 10) :
					print("SUPERHIT")
				ans1=raw_input("do u want to access admin login y/n")
				print "\n"
				if(ans1=='y' or ans1=='Y') :
						admin=raw_input("Admin Login:\t ") ##main menu
						print "\n"
						if admin=="1":
							passw=raw_input("Enter the password: \t")				##login
							if passw=="iiitn":
								option=raw_input("Press 1 to display the entries.\nPress 3 to exit:\t")	 ##admin functions
								print "\n"
							 
							if option=="1":
							    print(movie)
							    print(name)
							    print(name_h)
							    print(name_he)
							    print(name_md)
							elif option=="3":
							    quit()
                                        

				
