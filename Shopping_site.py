shoppingCart = {}
print("WELCOME TO THE AMANDO SHOPPING SITE")
a = print("A.Add product to the cart")
b = print("B.Search the product")
c = print("C.Delete the product from the cart")
d = print("D.Quit")
while True:
    choice = (input("Enter your choice: "))
    if choice == 'A':
      products = int(input("Enter the number of items to be added in the stationary shop: "))
      if products<5:
        for i in range(products):
           item = input("Enter an item: ")
           brand = input("Enter the brand name: ")
           shoppingCart['product_name'] = item
           shoppingCart['Brand'] = brand
        print("You added following items to the cart ")
        print(shoppingCart["product_name":"Brand"])
       
       
      else:
        print("You can add max 5 items")
    elif choice == 'B':
       search = input("Enter the items to be searched")
       if search in shoppingCart:
          print(f"{search}:{shoppingCart[search]}")
       else:
          print("Items does not exist")
    elif choice == 'C':
        delit = input("Enter the item to be removed:")
        if delit in shoppingCart:
            shoppingCart.pop(delit)
            print("Product removed from cart")
        else:
            print("items does not exist")
    elif choice == 'D':
        print("Thank you for using this shopping site")
        break

    else:
        print("Wrong option Entered")