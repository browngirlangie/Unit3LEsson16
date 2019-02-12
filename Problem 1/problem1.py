import random
import time

print()
print('*' * 100)

print("A wild Eevee appears!")
print()
time.sleep(1)

print('You only have one Pokemon, Squirtle.')
print()
time.sleep(1)

squirtle_hp = 300
eevee_hp = 100

print(">> squirtle has " + str(squirtle_hp) + " HP.")
print(">> eevee has " + str(eevee_hp) + " HP.")

print()

while squirtle_hp > 0 and eevee_hp > 0:
	print("Battle Options:")
	time.sleep(1)

	print("> [1] Sparkling Aria")
	print("> [2] Fury Swipes")
	print("> [3] Ice Spin")
	print("> [4] Slash")
	print("> [5] Capture")

	time.sleep(2)

	print()

	print(">> What should squirtle do?") 
	playermove = input(">> Choose a move using the corresponding number: ")

	if playermove == "1":
		print()
		eevee_hp = eevee_hp - 20
		print(">> squirtle used sparkling aria.")
		print()
		time.sleep(1)
		print(">> eevee is hit!")
		time.sleep(1)
		print(">> eevee's HP is decreased to " + str(eevee_hp) + ".")
		print()

	elif playermove == "2":
		print()
		eevee_hp = eevee_hp - 30
		print(">> squirtle used Fury Swipes.")
		print()
		time.sleep(1)
		print(">> eevee is hit!")
		time.sleep(1)
		print(">> eevee's HP is decreased to " + str(squirtle_hp) + ".")
		print()

	elif playermove == "3":
		print()
		eevee_hp = eevee_hp - 20
		print(">> squirtle used Ice Spin.")
		print()
		time.sleep(1)
		print(">> eevee is hit!")
		time.sleep(1)
		print(">> eevee's HP is decreased to " + str(eevee_hp) + ".")
		print()

	elif playermove == "4": 
		print()
		eevee_hp = eevee_hp - 15
		print(">> squirtle used Slash.")
		print()
		time.sleep(1)
		print(">> eevee is hit!")
		time.sleep(1)
		print(">> eevee's HP is decreased to " + str(eevee_hp) + ".")
		print()

	elif playermove == "5": 
		capture = random.randint(1,125)
	
		if capture > eevee_hp: 
			print()
			time.sleep(2)
			print("...")

			print()
			time.sleep(2)
			print("...")

			print()
			time.sleep(2)
			print("...")
			print()
			
			print("You captured eevee!")
			break

		else: 
			print()
			time.sleep(2)
			print("...")

			print()
			time.sleep(2)
			print("...")

			print()
			time.sleep(2)
			print("...")
			print()

			print("eevee escaped!")

	
	
