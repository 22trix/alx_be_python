weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny":
  print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
  message = " Don't forget your umbrella and a raincoat."
elif weather == "cold":
  message = "Make sure to wear a warm coat and a scarf."
else:
  message = "Sorry, I don't have recommendations for this weather."
print(message)